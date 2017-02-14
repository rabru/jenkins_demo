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
    parse = line.split( )
    if parse:
        if parse.pop(0) is "M":
            print(parse.[1])
            #os.system("./scripts/deploy_iapp_bigip.py -r " + bigipaddr + " " + parse.pop())