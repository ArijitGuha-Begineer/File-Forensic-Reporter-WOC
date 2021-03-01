import subprocess


def peepdf(loc):   #provides complete analysis of the file
	text=subprocess.run(['peepdf',loc],capture_output=True,text=True)
	print(text.stdout)

def hashfinder(loc):  #finding any hidden hash within the pdf file
	text=subprocess.run(['peepdf -c',loc],shell=True,capture_output=True,text=True)
	print(text.stdout)

def main(loc):
	peepdf(loc)
	hashfinder(loc)



if __name__ == '__main__':
  main(loc)