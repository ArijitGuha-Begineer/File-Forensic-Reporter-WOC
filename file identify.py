import subprocess


def fileidentification(loc):
	command=subprocess.run(['file',loc],capture_output=True,text=True)
	print(command.stdout)

fileidentification('/home/arijit/Downloads/rocks.jpg')