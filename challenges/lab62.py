farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

NE_animals= farms[0]["agriculture"]



yuck= ["carrots", "celery"]

for farm in farms:
    print("-", farm["name"])

answer=input("Choose a farm: ")

for farm in farms:
    if farm["name"].lower() == answer.lower():
        # x= farm["agriculture"]
        # print(x)    
        for critter in farm["agriculture"]:
            if critter not in yuck:
                print(critter)
        break    

# for farm in farms:
#     print("-", farm)
#     input("choose a farm\n>")