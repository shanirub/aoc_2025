def read_input(file_path):
    with open(file_path, 'r') as file:
        raw_data = file.read()

    ranges = raw_data.split(',')
    print(f"found {len(ranges)} ranges")
    return ranges

def solve(ranges):
    # part 1
    sum_of_invalid_ids = 0

    for r in ranges:
        begin, end = r.split('-')
        for i in range(int(begin), int(end) + 1):
            if len(str(i)) % 2 != 0:
                continue
            print(f'checking: {i}')

            i_str = str(i)
            i_len = len(i_str)

            if i_str[:i_len // 2] == i_str[i_len // 2:]:
                sum_of_invalid_ids += i
                print(f'{i} is invalid')

    return sum_of_invalid_ids

def is_invalid(i_str, chunk_size):
    chunks = [ i_str[x : x + chunk_size] for x in range(0, len(i_str), chunk_size) ]

    return all([x == chunks[0] for x in chunks])

def solve_second_challenge(ranges):
    # part 2
    sum_of_invalid_ids = 0
    for r in ranges:
        # processing range
        begin, end = r.split('-')

        for i in range(int(begin), int(end) + 1):
            i_str = str(i)
            i_len = len(i_str)
            should_skip = False

            for chunk_size in range(1, i_len // 2 + 1):
                if should_skip:
                    should_skip = False
                    break
                if i_len % chunk_size == 0 and is_invalid(i_str, chunk_size):
                    sum_of_invalid_ids += i
                    should_skip = True
                    print(f"adding invalid id {i} with chunk size {chunk_size}")

    return sum_of_invalid_ids

if __name__ == "__main__":
    file_path = 'input.txt'
    result = solve_second_challenge(read_input(file_path))
    print(f"result: {result}")