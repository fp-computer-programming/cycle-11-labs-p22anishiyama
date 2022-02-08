# Author: ATN 2/8/22

my_file = open("alma_mater.txt")
while True:
    line = my_file.readline()
    if len(line) == 0:
        break
    print (line, end="\n")
my_file.close()
