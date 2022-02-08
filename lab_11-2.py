# Author: ATN 2/8/22

my_file = open("alma_mater.txt")
contents = my_file.readlines()
contents.reverse()
print("".join(contents))
my_file.close()