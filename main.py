import fileinput
import matplotlib.pyplot as plt


def stageAnalyzer():
    road_pieces = [10, 14, 23, 13, 12, 11, 45, 46,47]
    offroad_pieces = [15, 17, 24, 16, 44, 43,48]
    road = 0
    offroad = 0
    name = ''

    filename = "stage.txt"

    for line in fileinput.input(files=filename):
        if line.startswith("name"):
            name = line.split("(")[1].split(")")[0]
        elif line.startswith("set("):
            number = int(line.split("(")[1].split(",")[0])
            if number in road_pieces:
                road += 1
            elif number in offroad_pieces:
                offroad += 1
            else:
                pass

    stageGrapher(road,offroad,name)


def stageGrapher(r, o, n):
    # r is road, o is offroad, n is name
    labels = ['Road', 'Offroad']
    sizes = [r, o]

    # Create a pie chart
    plt.figure(figsize=(5,5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f'Distribution of Road and Offroad Pieces\n for {n}')
    # plt.axis('equal')
    plt.show()



if __name__ == "__main__":
    print(stageAnalyzer())
