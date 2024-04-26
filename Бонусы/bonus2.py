def find_an():
    valid_numbers = []

    for i in range(2, 300):
        for j in range(2, 13):
            k = int(pow(i, j))
            if i == sum(map(int, str(k))) and k >= 10:
                valid_numbers.append((k, i, j))

    valid_numbers = sorted(valid_numbers)
    result = valid_numbers[29]
    return '{0}\n   ={1}**{2}'.format(result[0], result[1], result[2])


print(find_an())

