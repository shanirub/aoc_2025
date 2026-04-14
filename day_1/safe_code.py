DIAL_SIZE = 100

zero_count = 0


def move_dial(current_position, steps, direction):
    global zero_count
    if direction == 'R':
        new_position = current_position
        for i in range(steps):
            new_position = (new_position + 1) % DIAL_SIZE
            if new_position == 0:
                zero_count += 1
        print(f"Moving clockwise from {current_position} by {steps} steps to {new_position}")
    elif direction == 'L':
        new_position = current_position
        for i in range(steps):
            new_position = (new_position - 1) % DIAL_SIZE
            if new_position == 0:
                zero_count += 1
        print(f"Moving counterclockwise from {current_position} by {steps} steps to {new_position}")
    else:
        raise ValueError("Direction must be 'clockwise' or 'counterclockwise'")

    return new_position

def read_instructions(file_path):
    with open(file_path, 'r') as file:
        instructions = []
        for line in file:
            direction = line[0]
            steps = int(line[1:].strip())
            instructions.append((direction, steps))

    return instructions

if __name__ == "__main__":
    current_position = 50
    for direction, steps in read_instructions('input.txt'):
        current_position = move_dial(current_position, steps, direction)

    print(f"Final position: {current_position}")
    print(f"Number of times dial landed on 0: {zero_count}")