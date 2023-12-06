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
    list_nb = []
    nb = ""
    for character in lig:
        try:
            nb = nb + character
        except ValueError:
            if nb != "":
                list_nb.append(nb)
                nb = ""

    print(list_nb)