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

list_lig = []

for lig in data.split('\n'):
    list_nb = []
    nb = ""
    for character in lig:
        try:
            int(character)
            nb = nb + character
        except ValueError:
            if nb != "":
                list_nb.append(nb)
                nb = ""
    list_lig.append(list_nb)
print(list_lig)