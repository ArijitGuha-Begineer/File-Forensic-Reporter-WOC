import subprocess


loc='/home/arijit/Downloads/flag1.wav'

def strings(loc):
	import image
	image.strings(loc)

def exiftool(loc):
	import image
	image.exiftool(loc)

def xxd(loc):
	import image
	image.xxd(loc)

def wavsteg(loc):
	st=subprocess.Popen(['stegolsb','wavsteg','-r','-i',loc,'-o','output.txt','-n','2','-b','5589889'],stdout=subprocess.PIPE)
	output=st.communicate()
	


def outputsteg(loc):
    file=loc+'/ouput/audit.txt'
	
	st=subprocess.Popen(['cat',file],stdout=subprocess.PIPE)
	output=st.communicate()
	print(output)



def main(loc):
	strings(loc)
	exiftool(loc)
	xxd(loc)
	wavsteg(loc)
	outputsteg(loc)

if __name__ == '__main__':
	main(loc)
  