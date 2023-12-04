data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


content = {"red": 12, "green": 13, "blue": 14}

for game in data.split('\n'):
    for results in game[7:].split(";"):
        colors = {"red": None, "green": None, "blue": None}
        for color in results.split(","):
            if "red" in color:
                for i in range(len(color)):
                    try:
                        int(color[i])
                        try:
                            print(f"{int(color[i])}{int(color[i + 1])}")
                            i += 1
                        except:
                            print(int(color[i]))
                    except:
                        pass
            elif "green" in color:
                for i in range(len(color)):
                    try:
                        int(color[i])
                        try:
                            print(f"{int(color[i])}{int(color[i+1])}")
                            i += 1
                        except:
                            print(int(color[i]))
                    except:
                        pass
            else:
                for i in range(len(color)):
                    try:
                        int(color[i])
                        try:
                            print(f"{int(color[i])}{int(color[i + 1])}")
                            i += 1
                        except:
                            print(int(color[i]))
                    except:
                        pass

