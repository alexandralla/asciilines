import fileinput
  
lineNumber = 0;

for line in fileinput.input():
    print(line)
    lineNumber += 1;

print('the size of this file is', lineNumber)
