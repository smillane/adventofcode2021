with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    increased = 0
    new_array = []
    for row in lines:
        previous = sum(new_array)
        value = int(row)
        length = len(new_array)
        if length < 3:
            new_array.append(value)
        if length == 3:
            del new_array[0]
            new_array.append(value)
            current = sum(new_array)
            if current > previous:
                increased += 1

    """previous = int(lines[0])

    for row in lines:
        row = int(row)
        if row < previous or row == previous:
            previous = row
        else:
            increased += 1
            previous = row"""

print(increased)
