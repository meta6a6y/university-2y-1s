import math

T_MIN = 283.15  # в кельвинах
T_MAX = 353.15  # в кельвинах
T_STEP = 2.5
STEP_COUNT = int((T_MAX - T_MIN) / T_STEP) + 1


# Формула Гольдгаммера
def goldgammer(Tc: float, T: float, M: float, p1: float = 1.0) -> float:
    Tr = T / Tc

    def get_ppk() -> float:  # Вычисление плотности(пк)
        return M / (82.06 * Tc)

    def get_pp() -> float:  # Вычисление плотности(п)
        return math.pow(10, 1 / (5 * (Tr - 1))) * get_ppk()

    return get_pp() + p1 * math.pow(1 - Tr, 0.3)  # Вычисление по фромуле Гольдгаммера


def calculate_density(Tc: float, M: float, p1: float = 1.0) -> dict:    # Вычисление плотности
    result = dict()
    for i in range(STEP_COUNT):
        t = T_MIN + T_STEP * i
        result[t] = goldgammer(Tc=Tc, T=t, M=M, p1=p1)
    return result


def calc_delta(calculated_value: float, experimental_value: float) -> float:
    return (abs(calculated_value - experimental_value) / experimental_value) * 100


def input_parameters():
    Tc = float(input("Введите критическую температуру (К): "))
    M = float(input("Введите молярную массу вещества (г/моль): "))
    p1 = float(input("Введите p1: "))
    return Tc, M, p1


def read_input_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            Tc = float(lines[1].strip())
            M = float(lines[3].strip())
            p1 = float(lines[5].strip())
            return Tc, M, p1
    except FileNotFoundError:
        print("Ошибка: файл не найден.")
    except IndexError:
        print("Ошибка: некорректный формат файла.")
    except ValueError:
        print("Ошибка: некорректные данные в файле.")
    return None


def write_output_file(file_path, result, substance_name):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(f"Результаты расчета для {substance_name}:\n")
            file.write(f"{'T (°C)':<10}{'Плотность (г/см^3)':<15}\n")
            if result:
                for temp, density in result.items():
                    file.write(f"{temp - 273.15:<10.2f}{density:<15.4f}\n")
                print(f"Результаты записаны в файл: {file_path}")
            else:
                print(f"Ошибка: Параметры из файла не были считаны корректно.")
    except Exception as e:
        print(f"Ошибка записи в файл: {e}")


if __name__ == "__main__":
    choice = input("Ввод с консоли(1) или из файла(2): ")
    substance_name = input("Введите название вещества (этанол/бензол): ").lower()
    if choice == '1':
        if substance_name == "этанол" or "бензол":
            Tc, M, p1 = input_parameters()
            result = calculate_density(Tc, M, p1)
    elif choice == '2':
        if substance_name == "бензол":
            input_file_path = input("Введите путь к файлу с параметрами (например, input_benzol.txt): ")
            file_parameters = read_input_file(input_file_path)
            if file_parameters:
                Tc, M, p1 = file_parameters
                result = calculate_density(Tc, M, p1)
            else:
                exit()
        elif substance_name == "этанол":
            input_file_path = input("Введите путь к файлу с параметрами (например, input_etanol.txt): ")
            file_parameters = read_input_file(input_file_path)
            if file_parameters:
                Tc, M, p1 = file_parameters
                result = calculate_density(Tc, M, p1)
            else:
                exit()

    output_file_path = input("Введите путь для сохранения результатов (например, output.txt): ")
    write_output_file(output_file_path, result, substance_name)
