#!/usr/bin/python

#Prompt for file to be opened

file = raw_input("File to read and write: ")
if file == "":
	exit("Program EXIT: No file selected")

#Prompt for string to be removed

remove = raw_input("Line matching string to remove (end of the file): ")
if remove == "":
	exit("Program EXIT: String is empty")

#Read the file and close it
x = open(file, 'r')
lines = x.readlines()
x.close()


#Write the file and close it
x = open(file, 'w')

for line in lines:
	line = line.split(remove)

	#Reiterate the lines so they can be written
	for z in line:
		pass

	x.write(z)

x.close()

#ARRANGE THE FILE WITH EMPTY SPACE AT THE END OF THE FILE

x = open(file, 'r')
lines = x.readlines()
x.close()

x = open(file, 'w')
for line in sorted(lines, key=lambda lines: len(lines), reverse=True):
	line = line.split(remove)

	#Reiterate the lines so they can be written
	for z in line:
		pass

	x.write(z)
x.close()
print '''Removed everything in every line up to
	"%s" from the file "%s" and:
- empty space was placed at the end of the file
- lines were arranged by size''' % (remove, file)