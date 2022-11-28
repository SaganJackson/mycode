#!/usr/bin/env python3
import requests

API = 'http://127.0.0.1:2224/api'

# resp= requests.get(URL).json()

# pprint(resp)

def main():
    ## first grab credentials
    ##nasacreds = returncreds()

    ## make a call to NASAAPI with our key
    apodresp = requests.get(API)

    ## strip off json
    apod = apodresp.json()

    print(apod)

    print()

    print(f"Activity Description:", apod["activity"] + "\n")

    print(f"Type of activity:", apod["type"] + "\n")

    print(f"Number of Participants:", apod["participants"])

    print(apod["key"])

if __name__ == "__main__":
    main()

