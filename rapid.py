import time
start_time = time.clock()

file = raw_input("### File to clan: ") #Prompt for file to be opened
if file == "":
	exit("### Program EXIT: No file selected ###")

keyword = ['gov.au', '.jpg', '.png', '.gif', 'disqus.com','gov']

def reading(): #Read the file and close it
	x = open(file, 'r')
	lines = x.readlines()
	x.close()
	return lines	

def gov_au():
	lines = reading()
	x = open(file, 'w')
	for line in lines:
		line = line.split(keyword[0])
		for z in line:
			pass
		x.write(z)

def jpg():
	lines = reading()
	x = open(file, 'w')
	for line in lines:
		line = line.split(keyword[1])
		for z in line:
			pass
		x.write(z)

def png():
	lines = reading()
	x = open(file, 'w')
	for line in lines:
		line = line.split(keyword[2])
		for z in line:
			pass
		x.write(z)

def gif():
	lines = reading()
	x = open(file, 'w')
	for line in lines:
		line = line.split(keyword[3])
		for z in line:
			pass
		x.write(z)

def disqus():
	lines = reading()
	x = open(file, 'w')
	for line in lines:
		line = line.split(keyword[4])
		for z in line:
			pass
		x.write(z)

def gov():
	lines = reading()
	x = open(file, 'w')
	for line in lines:
		line = line.split(keyword[-1])
		for z in line:
			pass
		x.write(z)

print '*'*20
print '--> Reading the file "%s"' % file
reading()
print '*'*20
print '--> Roving keywords: %s' % keyword
gov_au()
jpg()
png()
gif()
disqus()
gov()
print '*'*20,'\n### Finished: time to complete: %s seconds ###' % (time.clock() - start_time)