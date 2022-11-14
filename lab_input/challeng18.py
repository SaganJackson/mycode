#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   CHALLENGE 18 - Attempt"""    

def main():

    user_name = input("What is your name?")
    
    ## the line below creates a single string that is passed to print()
    
    
    ## print() can be given a series of objects separated by a comma
    print("You told me your name is", user_name)
    
    # asking user for 'day of the week'
    weekday = input("What day of the week is it?")
    print(f"Hello, {user_name}! Happy {weekday}!")

main() 
