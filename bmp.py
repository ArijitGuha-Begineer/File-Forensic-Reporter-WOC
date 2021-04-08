import subprocess
import modules

def main(loc):
    modules.strings(loc)
    modules.exiftool(loc)
    modules.binwalk(loc)
    modules.xxd(loc)
    modules.foremost(loc)
    modules.stegseek(loc)