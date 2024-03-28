import fileinput


def stageAnalyzer():
    road_pieces = [10, 14, 23, 13, 12, 11, 45, 46]
    offroad_pieces = [15, 17, 24, 16, 44, 43]
    road = 0
    offroad = 0

    filename = "stage.txt"

    for line in fileinput.input(files=filename):
        if line.startswith("set("):
            number = int(line.split("(")[1].split(",")[0])  
            if number in road_pieces:
                road += 1
            elif number in offroad_pieces:
                offroad += 1
            else:
                pass
    return road, offroad



if __name__ == "__main__":
    print(stageAnalyzer())
