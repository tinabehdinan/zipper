### display length of each line of input from file
###	in shell: cat file | python std.py

import sys
# stdin is standard input (wired to keyboard i.e. reads from keyboard); stdout is standard output (wired to screen i.e. prints to screen)
for line in sys.stdin:
	temp = line.strip()
	print len(temp)


