import subprocess
import re

loc='/home/arijit/Downloads/rocks.jpg'

def strings(loc):   #calling strings command for PNG and JPG files
   st=subprocess.Popen(['strings',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   with open("Report.md","a")as f:
      f.write("*****output*****")
      f.close()
   with open("Report.md","a+b")as f:
      f.write(output)
      f.close() 

def exiftool(loc):  #calling exiftool for PNG and JPG files
    st=subprocess.Popen(['exiftool',loc],stdout=subprocess.PIPE)
    output=st.communicate()[0]
    with open("Report.md","a")as f:
       f.write("*****output******")
       f.close()
    with open("Report.md","a+b")as f:
       f.write(output)
       f.close()


def zsteg(loc):     #calling zsteg for PNG files
   st=subprocess.Popen(['zsteg',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   
   with open("Report2.md","a")as f:
      f.write("******output*******")
      f.close()
   with open("Report2.md","a+b")as f:
      f.write(output)
      f.close()

def binwalk(loc):   #reveals metadata stored in the image
   st=subprocess.Popen(['binwalk',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   
   with open("Report2.md","a")as f:
      f.write("output")
      f.close()
   with open("Report2.md","a+b")as f:
      f.write(output)
      f.close()


def stegseek(loc):
   st=subprocess.Popen(['stegseek',loc,'/home/arijit/Downloads/rockyou.txt'],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   
   with open("Report2.md","a")as f:
      f.write("output")
      f.close()
   with open("Report2.md","a+b")as f:
      f.write(output)
      f.close()


def imagemagick(loc):
   st=subprocess.Popen(['identify','-verbose',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   
   with open("Report2.md","a")as f:
      f.write("output")
      f.close()
   with open("Report2.md","a+b")as f:
      f.write(output)
      f.close()

def xxd(loc):
   st=subprocess.Popen(['xxd','-a',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
  
   with open("Report2.md","a")as f:
      f.write("output")
      f.close()
   with open("Report2.md","a+b")as f:
      f.write(output)
      f.close()


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








