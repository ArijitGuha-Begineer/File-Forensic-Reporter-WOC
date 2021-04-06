import subprocess
import modules


def main(loc):
    modules.strings(loc)
    modules.binwalk(loc)
    modules.cat(loc)
    modules.xxd(loc)
    modules.exiftool(loc)