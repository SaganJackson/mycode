#!/usr/bin/env python3
import requests

NASAAPI = 'http://127.0.0.1:2224/api'

# resp= requests.get(URL).json()

# pprint(resp)

def main():
    ## first grab credentials
    ##nasacreds = returncreds()

    ## make a call to NASAAPI with our key
    apodresp = requests.get(NASAAPI)

    ## strip off json
    apod = apodresp.json()

    print(apod)

    print()

    print(apod["activity"] + "\n")

    print(apod["type"] + "\n")

    print(apod["participants"])

    print(apod["key"])

if __name__ == "__main__":
    main()

