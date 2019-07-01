import fileinput

inFile = fileinput.input()
width = 0
height = 0


def main():

    lineNumber = 0
    global width
    global height

    for line in inFile:

        if (lineNumber == 0):

            size = line.split(" ")
            width = int(size[0])
            height = int(size[1])

            canvas = buildCanvas(width, height)
            lineNumber += 1

        else:

            render = line.split(" ")
            char = render[0]
            rowPos = int(render[1])
            colPos = int(render[2])
            direction = render[3]
            length = int(render[4])

            canvas = renderLine(char, rowPos, colPos, direction, length, canvas)

    show(canvas)


def buildCanvas(width, height):
    
    canvas = [[0 for x in range(height)] for y in range(width)] 

#    print('\nOriginal canvas:')
    for i in range(width):
        for j in range(height):
            canvas[i][j] = '.'
#            print(canvas[i][j], end=' ')
#        print()


    return canvas

def renderLine(char, rowPos, colPos, direction, length, canvas):

    count = 0
#    print('\nRendering new line:')


    if (rowPos < 0):
        rowPos = 0

    if (rowPos > height):
        rowPos = height

    if (colPos < 0):
        colPos = 0

    if (colPos > width):
        colPos = width

    if (length < 0):
        length = 0

    if (direction == 'h' and length > width):
        length = width

    if (direction == 'v' and length > height):
        length = height

    for i in range(width):
        for j in range(height):
            if (i == rowPos and j == colPos):
                canvas[i][j] = char
                
                a = 1

                if (direction == 'h'):

                    if (height > length + 1):
                        length = length - 1

                    for a in range(length):
                        if (j in range(height - 1)):
                            j += 1
                            canvas[i][j] = char
                    a = 0

                if (direction == 'v'):

                    if (width > length):
                        length = length - 1

                    for a in range(length):
                        if (i in range(width - 1)):
                            i += 1
                            canvas[i][j] = char
                    a = 0

    return canvas

def show(canvas):

    print('\nFinal result:')
    for i in range(width):
        for j in range(height):
            print(canvas[i][j], end=' ')
        print()


if __name__ == "__main__":
    main()
