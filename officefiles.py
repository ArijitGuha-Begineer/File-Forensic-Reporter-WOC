import subprocess
import re

loc="/home/arijit/Downloads/weird.docm"

def olevba(loc):
    st=subprocess.Popen(['olevba','-c',loc],stdout=subprocess.PIPE)
    output=st.communicate()[0]
    with open("Report.md","a")as f:
        f.write("output")
        f.close()
    with open("Report.md","a+b")as f:
        f.write(output)
        f.close()

def mraptor(loc):
    st=subprocess.Popen(['mraptor',loc],stdout=subprocess.PIPE)
    output=st.communicate()[0]
    with open("Report.md","a")as f:
        f.write("output")
        f.close()
    with open("Report.md","a+b")as f:
        f.write(output)
        f.close()
    
        

def main(loc):
    olevba(loc)
    mraptor(loc)

if __name__ == '__main__':
	main(loc)
