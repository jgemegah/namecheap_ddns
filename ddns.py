#!/usr/bin/python3
# Script used for updating host records for namecheap.com domain names
# !) Set the Nameservers to "Namecheap BasicDNS"
# 2) In the Advanced DNS tab enable Dynamic DNS
# 3) Update the config dictonary below
# 4) Setup crontab "* * * * * <path-to-script>/ddns.py
config = {
    "<domain1.com>" : {
        "hosts" : ["@", "www"],
        "password" : "<dyanmic-DNS-password-for-domain1>"
    }
    "<domain2.com>" : {
        "hosts" : ["@", "www"],
        "password" : "<dynamic-DNS-password-for-domain2>"
    }
}

from requests import get
from subprocess import Popen, PIPE

for domain,data in config.items():
    hosts = data['hosts']
    password = data['password']
    ip = Popen("dig +short myip.opendns.com @resolver1.opendns.com",
                       stdout=PIPE, shell=True).communicate()[0].strip()

    for host in hosts:
        url = "https://dynamicdns.park-your-domain.com/update?host=" + \
              host + \
              "&domain=" + \
              domain + \
              "&password=" + \
              password + \
              "&ip=" + \
              ip.decode("utf-8")
        
        response = get(url)
        print(response.content)

