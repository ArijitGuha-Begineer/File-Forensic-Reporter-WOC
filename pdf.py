import subprocess

loc='/home/arijit/Downloads/1.pdf'
def peepdf(loc):   #provides complete analysis of the file
   st=subprocess.Popen(['peepdf',loc],stdout=subprocess.PIPE,)
   output=st.communicate()
   print(output)

def hashfinder(loc):  #finding any hidden hash within the pdf file
	text=subprocess.run(['peepdf -c',loc],shell=True,capture_output=True,text=True)
	print(text.stdout)

def pdfparser(loc):
	text=subprocess.run(['pdf-parser -a',loc],shell=True,capture_output=True,text=True)
	print(text.stdout)

def main(loc):
	peepdf(loc)
	hashfinder(loc)



if __name__ == '__main__':
  main(loc)
