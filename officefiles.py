import subprocess
import re

loc="/home/arijit/Downloads/weird.docm"

def olevba(loc):
    st=subprocess.Popen(['olevba','-c',loc],stdout=subprocess.PIPE)
    output=st.communicate()[0]
    with open("/home/arijit/Downloads/Report.md","a")as f:
        f.write("output")
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
        f.write("\n\n******output*******\n\n")
        f.close()
    with open("/home/arijit/Downloads/Report.md","a+b")as f:
        f.write(output)
        f.close()

def msodde(loc):
    st=subprocess.Popen(['msodde','-a',loc],stdout=subprocess.PIPE)
    output=st.communicate()[0]
    with open("/home/arijit/Downloads/Report.md","a")as f:
        f.write("\n\n******output*******\n\n")
        f.close()
    with open("/home/arijit/Downloads/Report.md","a+b")as f:
        f.write(output)
        f.close()

    
        

def main(loc):
    olevba(loc)
    mraptor(loc)
    pyxswf(loc)
    msodde(loc)

if __name__ == '__main__':
	main(loc)
