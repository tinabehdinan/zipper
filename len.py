reader = open('animals.txt', 'r')
for line in reader:
# .strip will clean up the line
	temp = line.strip()
# print length of each line
	print len(line)
reader.close()

# can test if this program worked correctly by running the script on a test file with known number of characters per line
