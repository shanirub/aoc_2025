
def expensive_second_challenge(power_supply):

    total_joltage = 0
    battery_length = 12 # number of cells in a row

    def find_max_value_index(start, end, bank):
        # helper for finding max in a slice of row from start index to end index
        max_value = -1
        max_index = None

        for i in range(start, end):
            if int(bank[i]) > max_value:
                max_value = int(bank[i])
                max_index = i

        return max_index, max_value


    for row in power_supply:
        row_max_value = []
        latest_index = -1
        for b in range(battery_length - 1, -1, -1):
            latest_index, latest_value =find_max_value_index(
                start=latest_index + 1,
                end=len(row) - b,
                bank=row
            )
            row_max_value.append(str(latest_value))

        total_joltage += int(''.join(row_max_value))

    return total_joltage


def solve_first_challenge(power_supply):
    total_joltage = 0

    for bank in power_supply:
        bank_length = len(bank)
        if bank_length <= 2:
            total_joltage += int(bank)
            continue

        ones_value = int(bank[1])
        tens_value = int(bank[0])

        i = 1

        while i < bank_length - 1:
            if int(bank[i]) > tens_value:
                tens_value = int(bank[i])
                ones_value = int(bank[i + 1])
            elif int(bank[i]) > ones_value:
                ones_value = int(bank[i])

            i += 1

        # loop end, i points to before last digit
        # only ones_value needs to be checked

        if int(bank[-1]) > ones_value:
            ones_value = int(bank[-1])

        bank_max_value = tens_value * 10 + ones_value
        total_joltage += bank_max_value

        print(f"found max value {bank_max_value} from bank {bank}")

    print(f"total joltage {total_joltage}")
    return total_joltage

def read_input(file_path):
    power_supply = []
    with open(file_path, 'r') as file:
        for line in file:
            power_supply.append(line.strip('\n'))

    return power_supply


if __name__ == '__main__':
    input_file_path = 'input.txt'
    print(expensive_second_challenge(read_input(input_file_path)))