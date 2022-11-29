#!/usr/bin/env python3
import requests

API = 'http://127.0.0.1:2224/api'


def main():
    
    activityresp = requests.get(API)

    ## strip off json
    activity = activityresp.json()

    print(activity)

    print()

    print(f"Activity Description:", activity["activity"] + "\n")

    print(f"Type of activity:", activity["type"] + "\n")

    print(f"Number of Participants:", activity["participants"])

    print(activity["key"])

if __name__ == "__main__":
    main()

