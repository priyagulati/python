filename='python_class.txt'
try:
	with open(filename)as file_content:
	 contents=file_content.read()
except FileNotFoundError:
	msg="Sorry,the file " +filename +"does not exist."
	print(msg)
else:
	print(contents)