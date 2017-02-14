import os
import glob
from subprocess import check_output

bigipaddr = "10.1.1.4"

#for f in glob.glob('./*.json.deploy'):
#    print f
#    os.system("./scripts/deploy_iapp_bigip.py -r " + bigipaddr + " " + f)

cmd = "git log --name-status -1"
p = check_output(["git", "log", "--name-status", "-1"])

for line in p.splitlines():
    parse = line.split("\t")
    if parse:
        if parse[0].endswith(".json.deploy"):
            if parse[0].startswith("M"):
                os.system("./scripts/deploy_iapp_bigip.py -r " + bigipaddr + " " + parse[1])
            if parse[0].startswith("A"):
                os.system("./scripts/deploy_iapp_bigip.py " + bigipaddr + " " + parse[1])