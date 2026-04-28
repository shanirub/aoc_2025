def solve_second_challenge(fresh_ranges, _):
    total_ingredients = 0
    sorted_ranges = merge_ranges([x.split("-") for x in fresh_ranges])
    for start, end in sorted_ranges:
        total_ingredients += end - start + 1

    return total_ingredients


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []

    ranges_int = []
    for start, end in ranges:
        ranges_int.append((int(start), int(end)))
    sorted_ranges = sorted(ranges_int, key=lambda r: int(r[0]))
    merged = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        current_start, current_end = merged[-1]
        if start <= current_end + 1:
            merged[-1] = (current_start, max(current_end, end))
        else:
            merged.append((start, end))

    return merged


def solve_first_challenge(fresh_ranges, available_ingredients):

    total_fresh = 0

    sorted_ranges = merge_ranges([x.split("-") for x in fresh_ranges])

    for i in available_ingredients:
        for start, end in sorted_ranges:
            if start <= int(i) <= end:
                total_fresh += 1
                break

    return total_fresh


def read_input(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    lines = text.split('\n')

    fresh_ranges = [line for line in lines if '-' in line]
    available_ingredients = [
        line for line in lines if '-' not in line and len(line) > 0
    ]
    return fresh_ranges, available_ingredients


if __name__ == "__main__":
    file_path = 'input.txt'
    fresh_ranges, available_ingredients = read_input(file_path)
    print(solve_second_challenge(fresh_ranges, available_ingredients))