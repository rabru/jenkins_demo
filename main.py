import os
import glob

bigipaddr = "10.1.1.4"

for f in glob.glob('./*.json.deploy'):
    print f
    os.system("./scripts/deploy_iapp_bigip.py " + bigipaddr + " " + f)