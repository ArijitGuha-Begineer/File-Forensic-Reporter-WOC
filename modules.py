import subprocess
import re
from PIL import Image
def cat(loc):
  st=subprocess.Popen(['cat',loc],stdout=subprocess.PIPE)
  output=st.communicate()[0]
  with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n******output from cat *******\n\n")
      f.close()
  with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()
  

def strings(loc):   #calling strings command for PNG and JPG files
   st=subprocess.Popen(['head',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*****output head of strings*****\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close() 
   st=subprocess.Popen(['tail',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*****output tail of strings*****\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()

def exiftool(loc):  #calling exiftool for PNG and JPG files
    st=subprocess.Popen([f'exiftool {loc} | grep -v -E "Permissions|MIME|Subject|Title|Image Size|File Type|File Type Extension|File Name|Exiftool Version Number|Directory"'],stdout=subprocess.PIPE,shell=True)
    output=st.communicate()[0]
    
    with open("/home/arijit/Downloads/Report.md","a")as f:
       f.write("\n\n*****output from exiftool******\n\n")
       f.close()
    with open("/home/arijit/Downloads/Report.md","a+b")as f:
       f.write(output)
       f.close()


def zsteg(loc):     #calling zsteg for PNG files
   st=subprocess.Popen(['zsteg',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n******output from zsteg*******\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()

def binwalk(loc):   #reveals metadata stored in the image
   st=subprocess.Popen(['binwalk',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*******output from binwalk*******\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()


def stegseek(loc):
   st=subprocess.Popen(['stegseek',loc,'/home/arijit/Downloads/rockyou.txt'],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*******output from zsteg******\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()


def imagemagick(loc):
   st=subprocess.Popen(['identify','-verbose',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n********output from imagemagick*******\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()

def xxd(loc):
   st=subprocess.Popen(['xxd','-a',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
  
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*********output from xxd *******\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()

def outguess(loc):
   st=subprocess.Popen(['outguess','-r',loc,'output.txt'],stdout=subprocess.PIPE)
   output=st.communicate()[0]

   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*******output from outguess*******\n\n")
      f.close
   try:
      with open("/home/arijit/Downloads/output.txt","r")as l:
         text=l.read()
         l.close()
      with open("/home/arijit/Downloads/Report.md","a")as f:
         f.write(text)
         f.close()
   except:
      with open("/home/arijit/Downloads/Report.md","a")as f:
         f.write("No Output")
         f.close()

def foremost(loc):
   st=subprocess.Popen(['foremost','-T',loc,'-v'],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*********output from foremost *******\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()

def wavsteg(loc):
  st=subprocess.Popen(['stegolsb','wavsteg','-r','-i',loc,'-o','output.txt','-b','1000'],stdout=subprocess.PIPE)
  output=st.communicate()[0]
  with open('output.txt','r')as f1:
	  text=f1.read()
	  f1.close()
  with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*********output from wavesteg*******\n\n")
      f.close()
  with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      


def pdfid(loc):  #finding any hidden hash within the pdf file
  text=subprocess.Popen([f'pdfid {loc} | grep -v -E "xref|trailer|/AA|/OpenAction|/Acroform|/XFA|/RichMedia|startxref" '],shell=True,stdout=subprocess.PIPE)
  output=text.communicate()[0]
  with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*********output from pdfid******\n\n")
      f.close()
  with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()

def olevba(loc):
    st=subprocess.Popen(['olevba','-c',loc],stdout=subprocess.PIPE)
    output=st.communicate()[0]
    with open("/home/arijit/Downloads/Report.md","a")as f:
        f.write("\n\n********output from olevba******\n\n")
        f.close()
    with open("/home/arijit/Downloads/Report.md","a+b")as f:
        f.write(output)
        f.close()

def mraptor(loc):
    st=subprocess.run(['mraptor',loc],capture_output=True,text=True)
    ans=re.search('SUSPICIOUS',st.stdout)
    if ans==None:
        with open("/home/arijit/Downloads/Report.md","a")as f:
         f.write("\n\n******NO SUSPICIOUS FILES*******\n\n")
         f.close()
    else:
        with open("/home/arijit/Downloads/Report.md","a")as f:
         f.write("\n\n******SUSPICIOUS FILES PRESENT*******\n\n")
         f.close()


def pyxswf(loc):
    st=subprocess.Popen(['pyxswf','-x',loc],stdout=subprocess.PIPE)
    output=st.communicate()[0]
    with open("/home/arijit/Downloads/Report.md","a")as f:
        f.write("\n\n******output from pyxswf*******\n\n")
        f.close()
    with open("/home/arijit/Downloads/Report.md","a+b")as f:
        f.write(output)
        f.close()

def msodde(loc):
    st=subprocess.Popen(['msodde','-a',loc],stdout=subprocess.PIPE)
    output=st.communicate()[0]
    with open("/home/arijit/Downloads/Report.md","a")as f:
        f.write("\n\n******output from msodde*******\n\n")
        f.close()
    with open("/home/arijit/Downloads/Report.md","a+b")as f:
        f.write(output)
        f.close()

def stegsnow(loc):
   st=subprocess.Popen(['stegsnow',loc,'/home/arijit/Downloads/snowoutput.txt'],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*******output from stegsnow*******\n\n")
      f.close
   try:
      with open("/home/arijit/Downloads/snowoutput.txt","r")as l:
         text=l.read()
      with open("/home/arijit/Downloads/Report.md","a")as f:
         f.write(text)
         f.close()
   except:
      with open("/home/arijit/Downloads/Report.md","a")as f:
         f.write("No Output")
         f.close()

def spectrogram(loc):
   st=subprocess.Popen(['sox',loc,'-n','spectrogram'],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   im=Image.open("/home/arijit/spectrogram.png")
   image=im.show()
