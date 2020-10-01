#!/usr/bin/python3

# This is a script that takes in a prefix and connects to the RIPE's RIS 
# to get info about what ASN is announcing the prefix and get its RPKI validation state

import sys
import requests
import json
import argparse
import urllib3
import pprint

# Check to see if we are running in python 3, exit if not
if sys.version_info<(3,0,0):
   sys.stderr.write("You need python 3.0+ or later to run this script\n")
   exit(1)

# Get command line arguments and parse them
parser = argparse.ArgumentParser(description='This is a script that takes in a prefix and connects to the RIPE\'s RIS to get info about what ASN is announcing the prefix and get its RPKI validation state.')
parser.add_argument('-p','--prefix', help='Specify an IP Prefix',required=True)

args = parser.parse_args()

# Disable the SSL Cert warnings on a self signed cert (Not recommended!)
# urllib3.disable_warnings()

# Construct the payload
payload = {'resource': args.prefix}

# Construct the URL
url = "https://stat.ripe.net/data/routing-status/data.json"


# Attempt to retrieve data from API or error out
try:
    response = requests.get(url, params=payload)

except requests.exceptions.HTTPError as e:
    if debug:
        print("Uh oh we got an http error! ")
    print (e)
    sys.exit(1)
except requests.exceptions as e:
    if debug:
        print("Uh oh we got a requests error! ")
    print (e)
    sys.exit(1)

# Put the data into a dictionary
data = response.json()

# Construct the payload
payload = {'resource': data['data']['last_seen']['origin'], 'prefix': args.prefix}

# Construct the URL
url = "https://stat.ripe.net/data/rpki-validation/data.json"


# Attempt to retrieve data from API or error out
try:
    response = requests.get(url, params=payload)

except requests.exceptions.HTTPError as e:
    if debug:
        print("Uh oh we got an http error! ")
    print (e)
    sys.exit(1)
except requests.exceptions as e:
    if debug:
        print("Uh oh we got a requests error! ")
    print (e)
    sys.exit(1)

# Put the data into a dictionary
data2 = response.json()


print('Prefix:',data['data']['last_seen']['prefix'],'was last seen announced by ASN:',data['data']['last_seen']['origin'],'at:',data['data']['last_seen']['time'],'by',data['data']['visibility']['v4']['total_ris_peers'],'IPv4 peers and',data['data']['visibility']['v6']['total_ris_peers'],'IPv6 peers and its RPKI Validation status is:',data2['data']['status'])
