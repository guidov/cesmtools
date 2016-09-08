import os, sys


def check_machine_is_GPC():
    if (os.environ["MACH"] != "gpc"):
        print("ERROR: THIS SCRIPT IS ONLY DESIGNED FOR *** GPC *** MACHINES")
        sys.exit(-1)
