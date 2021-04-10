import subprocess
import modules


def main(loc):
   modules.strings(loc)
   modules.exiftool(loc)
   modules.binwalk(loc)
   modules.xxd(loc)
   modules.outguess(loc)
   modules.foremost(loc)
   modules.stegseek(loc)
   modules.imagemagick(loc)
   modules.stegsnow(loc)


