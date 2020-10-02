# Check RPKI Status
Python3 script that takes in an IPv4 or IPv6 prefix and connects to the RIPE's RIS (Routing Information Service) API to get info about what ASN is announcing the prefix and get its RPKI validation state

You can run it on a text file with a bunch of prefixes like this: 
```
while read -r line; do ./check_rpki_status.py -p $line; done < prefixes.txt
```
The output looks like this:
```
Prefix: 107.14.0.0/21 was last seen announced by ASN: 16787 at: 2020-10-01T08:00:00 by 325 IPv4 peers and 0 IPv6 peers and its RPKI Validation status is: valid
Prefix: 107.14.104.0/21 was last seen announced by ASN: 16787 at: 2020-10-01T08:00:00 by 325 IPv4 peers and 0 IPv6 peers and its RPKI Validation status is: valid
```

If the RPKI Validation status is invalid, then the route for that prefix is being filtered by providers that do Route Origin Validation (https://tools.ietf.org/html/rfc6811) and the ROA for that prefix needs to be deleted and recreated.

