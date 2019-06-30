import fileinput
import numpy as np

inFile = fileinput.input();


def main():

    lineNumber = 0
    width = 0
    height = 0

    for line in inFile:

        if (lineNumber == 0):

            size = line.split(" ")
            width = int(size[0])
            height = int(size[1])

            buildCanvas(width, height);


#        if (lineNumber == 1):
#            print('in line 1')
#
#        if (lineNumber == 2):
#            print('in line 2')
#
        lineNumber += 1

def buildCanvas(width, height):
    
    canvas = np.zeros([width, height]);

    for i in range(width):
        for j in range(height):
            print('.', end=' ')
        print()

#    print(canvas)


if __name__ == "__main__":
    main()
