data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

for lig in data.split('\n'):
    for character in lig:
        try:
            int(character)
        except ValueError:
            pass
