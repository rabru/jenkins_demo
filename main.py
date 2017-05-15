# This script is called by Jenkins and checks what changes were made during the last git commit and will then deploy,
# redeploy or delete an iApp. The file to be deployed/redeployed needs to end with .json.deploy. For the delete
# to work you need to make sure the name in the json.deploy file (for example "name":"my_https_sample2") is the same
# as the name of the file (For example my_https_sample2.json.deploy)

import os
import glob
from subprocess import check_output

bigipaddr = "10.10.86.12"

p = check_output(["git", "log", "--name-status", "-1"])

print("List of services to Add/Modify/Remove")
for line in p.splitlines():
    parse = line.split("\t")
    if len(parse) >= 2:
        if parse[1].endswith(".json.deploy"):
            print(parse)

for line in p.splitlines():
    if len(parse) >= 2:
        if parse[1].endswith(".json.deploy"):
            if parse[0] == "M":
                os.system("./scripts/deploy_iapp_bigip.py -r " + bigipaddr + " " + parse[1])
            elif parse[0] == "A":
                os.system("./scripts/deploy_iapp_bigip.py " + bigipaddr + " " + parse[1])
            elif parse[0] == "D":
                os.system("./scripts/delete_iapp_bigip.py " + bigipaddr + " " + "-n" + " " + parse[1].split(".")[0])
