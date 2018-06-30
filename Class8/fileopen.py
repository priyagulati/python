#for loop
filename='class-concept.txt'
with open(filename)as file_content:
	for line in file_content:
		print (line)
		
		
# read line by line
filename='class-concept.txt'
with open(filename)as file_content:
	contents=file_content.read()
print(contents)

# write the file
# w mode when u r writing
# appending adding more stuff

filename='pythonclass.txt'
with open(filename,'w')as file_content:
	file_content.write("This is my 8 th Python class")
	file_content.write("\nNext week is last python class")

