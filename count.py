### how many lines are there in my animals.txt file?

# open the animals.txt file (r means read mode) into reader variable (like reader <- read.csv function)
reader = open('animals.txt', 'r')
count = 0

for line in reader:
# add 1 to count for each new line that's read
	count = count + 1
# close file
reader.close()
print count, 'lines'
