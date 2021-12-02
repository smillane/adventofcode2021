with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    horizontal = 0
    vertical = 0
    aim = 0
    for row in lines:
        row = row.split(" ")
        value = int(row[1])
        if 'forward' in row[0]:
            horizontal += value
            vertical += (aim * value)
        if 'down' in row[0]:
            aim += value
        if 'up' in row[0]:
            aim -= value

    final = horizontal * vertical
print(final)
