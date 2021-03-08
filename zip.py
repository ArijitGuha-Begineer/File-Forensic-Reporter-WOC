import zipfile

loc='/home/arijit/Downloads/task.zip'

with zipfile.ZipFile(loc,'r') as my_zip:
	print(my_zip.namelist())


	

