import os

bigipaddr = "10.1.1.4"

for f in glob.glob('./*.json'):
    print f
    os.system("./scripts/deploy_iapp_bigip.py " + bigipaddr + " " + f)