#!/usr/bin/env python3
"""Understanding dictionaries
   {key: value, key:value, ...} """

def main():
    """runtime function"""

    ## create a dictionary with 4 key:value pairs
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    ## display the entire dictionary
    print(switch)

    ## proove that switch is indeed a dictionary
    print(type(switch))

    ## display parts of the dictionary
    print( switch["hostname"] )    # displays "sw1"
    print( switch["ip"] )          # displays "10.0.1.1"

    ## request a 'fake' key
    print( switch["lynx"] )  # this will cause the program to FAIL  


# call our main function
if __name__ == "__main__":
    main()






# for question in quiz_bank:
#     attempts= 3
#     while attempts > 0:
#                 print(quiz_bank[question]['question'])
#     answer = input("Please type answer here: ")
#     check = check_ans(question, answer, attempts)
#     if check:
#             attempts-= 1

# def check_ans(question, ans, attempts):
#     if quiz_bank[question]['answer'].lower() == ans.lower():
#         return True
#     else:
#         return False
    

# answer= " "

# tries= 0
# while tries < 3 and answer != "days":
#     tries += 1
#     answer= input('Finish the lyrics to this theme song\n "In West Philadelphia born and raised. On the playground is where I spent most of my _____"\n>').lower()
#     if answer == "days":
#         print("Correct!")
        
#     elif tries == 3:
#         print(f'The answer is "days", not {answer}')   
        
#     else:
#         print("Sorry, try again")
    
# while tries < 3 and answer != "girls":
#     tries += 1
#     answer= input('Finish the lyrics to this theme song\n "We are livinggggg single, Ohhh in a 90s kinda world Im glad I got my _____"\n>').lower()
#     if answer == "girls":
#         print("Correct!")

#     elif tries == 3:
#         print(f'The answer is "girls", not {answer}') 

#     else:
#         print("Sorry, try again")  




#show theme song guessing game using if, elif, and else



#print out the question
#print out the possible answers

#use input to get the player's answer
# if the value of answer is equal to A, +1 to the correct variable
#elif answer == "b" +1 to the wrong variable

# after severalquestions you could print out all the scores

# themesongs= [
#     {"Fresh Prince of BelAir": "on the playground is where I spent most of my days"},
#     {}
      

#   ]
# correct= 0
# wrong= 0
# quiz_bank= {
#     1 : {"question" : "In West Philadelphia born and raised. On the playground is where I spent most of my _____", 
#          "answer" : "days"},
#     2 : {"question" : "We are livinggggg single, Ohhh in a 90s kinda world Im glad I got my _____",
#     "answer" : "girls" },
#     3 : {"question" : "It's a rare condition, this day and age, to read any good news on the newspaper page. Love and tradition of the grand design, some people say it's even harder   to ____.", "answer" : "find"},
#     4 : {"question" : "I know my parents love me, Stand behind me come what may. I know now that I'm ready, Because I finally heard them say It's a _____ world than where you come from", "answer" : "different"},
#     5 : {"question" : "Sister, sister Never knew how much I ____ ya Now that everybody knows I ain't ever gonna let you go", "answer" : "missed"} }
