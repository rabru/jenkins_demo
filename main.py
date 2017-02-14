import os
import glob
import subprocess

bigipaddr = "10.1.1.4"

#for f in glob.glob('./*.json.deploy'):
#    print f
#    os.system("./scripts/deploy_iapp_bigip.py -r " + bigipaddr + " " + f)

cmd = "git log --name-status -1"
p = subprocess.Popen(cmd, stdout=PIPE)

for line in p.stdout:
    print l