#  Вычислить плотность этилового спирта (C2H5OH) и бензола (C6H6) по методу Гольдгаммера в диапазоне
# температур 10 – 70°С с шагом 2,5 °С и оценить относительную погрешность расчёта, сравнив с табличными
# данными.



# Лабораторная №5
import math

T_MIN = 283.15        # в кельвинах
T_MAX = 353.15        # в кельвинах
T_STEP = 2.5
STEP_COUNT = int((T_MAX - T_MIN) / T_STEP) + 1

p_etanol = [0.7979, 0.7895, 0.7810, 0.7722, 0.7633, 0.7541, 0.7446, 0.7348]
t_etanol = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0]
t_etanol_kelvin = [t + 273.15 for t in t_etanol]
p_benzol = [0.8896, 0.8790, 0.8737, 0.8684, 0.8576, 0.8468, 0.8358, 0.8248, 0.8137]
t_benzol = [10.0, 20.0, 25.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0]
t_benzol_kelvin = [t + 273.15 for t in t_benzol]


# Формула Гольдгаммера
def goldgammer(Tc: float, T: float, M: float, p1: float = 1.0) -> float:
    Tr = T / Tc

    def get_ppk() -> float:         # Вычисление плотности(пк)
        return M / (82.06 * Tc)

    def get_pp() -> float:          # Вычисление плотности(п)
        return math.pow(10, 1 / (5 * (Tr - 1))) * get_ppk()

    return get_pp() + p1 * math.pow(1 - Tr, 0.3)        # Вычисление по фромуле Гольдгаммера


def calculate_density(Tc: float, M: float, p1: float = 1.0) -> dict:        # Вычисление плотности
    result = dict()
    for i in range(STEP_COUNT):
        t = T_MIN + T_STEP * i
        result[t] = goldgammer(Tc=Tc, T=t, M=M, p1=p1)

    return result


def calc_delta(calculated_value: float, experimental_value: float) -> float:        # Вычисление дельты
    return (abs(calculated_value - experimental_value) / experimental_value) * 100


if __name__ == "__main__":
    # Критические температуры веществ (К)
    Tc_etanol = 516.2
    Tc_benzol = 562.1

    # Молярные массы веществ (г/моль)
    M_etanol = 46.069
    M_benzol = 78.114

    # p1 - табличные значения, иначе слишком большая погрешность для бензола
    p1_benzol = 1.09

    result_etanol = calculate_density(Tc_etanol, M_etanol)
    result_benzol = calculate_density(Tc_benzol, M_benzol, p1_benzol)

    print(f"Результаты рассчета:\n\t{'T':10}{'etanol':10}{'benzol':10}")
    for temp in result_benzol:
        print(f'{temp:10}{result_etanol[temp]:10.4}{result_benzol[temp]:10.4}')

    delta_etanol = list(map(lambda t, p: calc_delta(result_etanol[t], p), t_etanol_kelvin, p_etanol))
    # delta_etanol = [calc_delta(result_etanol[t], p) for t, p in zip(t_etanol_kelvin, p_etanol)]
    DELTA_etanol = zip(t_etanol, t_etanol_kelvin, p_etanol, delta_etanol)
    print('\n\nРасхождение в расчетах для эталола')
    for delt in DELTA_etanol:
        print(delt)

    delta_benzol = list(map(lambda t, p: calc_delta(result_benzol[t], p), t_benzol_kelvin, p_benzol))
    # delta_benzol = [calc_delta(result_benzol[t], p) for t, p in zip(t_benzol_kelvin, p_benzol)]
    DELTA_benzol = zip(t_benzol, t_benzol_kelvin, p_benzol, delta_benzol)
    print('\n\nРасхождение в расчетах для бензола')
    for delt in DELTA_benzol:
        print(delt)