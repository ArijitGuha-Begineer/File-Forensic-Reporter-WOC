import subprocess
import re

loc='/home/arijit/Downloads/rocks.jpg'

def strings(loc):   #calling strings command for PNG and JPG files
   st=subprocess.Popen(['strings',loc],stdout=subprocess.PIPE)
   output=st.communicate()
   print(output)

def exiftool(loc):  #calling exiftool for PNG and JPG files
    st=subprocess.run(['exiftool',loc],capture_output=True,text=True)
    output=re.findall(r'[0-9]{4}\:[0-9]{2}\:[0-9]{2}\ [0-9]{2}\:[0-9]{2}\:[0-9]{2}\+[0-9]{2}\:[0-9]{2}',st.stdout)
    modificationdate=output[0]
    print('Modification date and time of the file: '+modificationdate)
    accessdate=output[1]
    print('Access date and time of the file: '+accessdate)
   

def zsteg(loc):     #calling zsteg for PNG files
   st=subprocess.Popen(['zsteg',loc],stdout=subprocess.PIPE)
   output=st.communicate()
   print(output)

def binwalk(loc):   #reveals metadata stored in the image
   st=subprocess.Popen(['binwalk',loc],stdout=subprocess.PIPE)
   output=st.communicate()
   print(output)


def stegseek(loc):
   st=subprocess.Popen(['stegseek',loc,'/home/arijit/Downloads/rockyou.txt'],stdout=subprocess.PIPE)
   output=st.communicate()
   print(output)


def imagemagick(loc):
   st=subprocess.Popen(['identify','-verbose',loc],stdout=subprocess.PIPE)
   output=st.communicate()
   print(output)

def xxd(loc):
   st=subprocess.Popen(['xxd','-a',loc],stdout=subprocess.PIPE)
   output=st.communicate()
   print(output)

def main(loc):
	strings(loc)
	exiftool(loc)
	zsteg(loc)
	binwalk(loc)
	stegseek(loc)
	imagemagick(loc)
	xxd(loc)
	

if __name__ == '__main__':
	main(loc)







