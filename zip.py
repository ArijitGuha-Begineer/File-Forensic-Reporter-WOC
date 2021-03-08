import zipfile

loc='/home/arijit/Downloads/task.zip'

def main(loc):
	with zipfile.ZipFile(loc,'r') as my_zip:
	print(my_zip.namelist())

if __name__ == '__main__':
	main(loc)

	

