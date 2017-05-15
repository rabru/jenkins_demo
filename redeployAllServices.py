# This script will go through all the .json.deploy files and redeploy them (overwrite changes if they are already
# deployed or create a new iapp deployement if they are not deployed)

import os
import glob
from subprocess import check_output

bigipaddr = "10.10.10.12"

for f in glob.glob('./*.json.deploy'):
    print f
    os.system("./scripts/deploy_iapp_bigip.py -r " + bigipaddr + " " + f)
