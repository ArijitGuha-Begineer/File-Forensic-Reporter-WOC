import subprocess

loc="/home/arijit/Downloads/weird.docm"

def olevba(loc):
    st=subprocess.Popen(['olevba','-c',loc],stdout=subprocess.PIPE)
    output=st.communicate()[0]
    print(output)

def main(loc):
    olevba(loc)

if __name__ == '__main__':
	main(loc)