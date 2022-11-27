#!/usr/bin/env python3

quiz_bank= {
    "In West Philadelphia born and raised. On the playground is where I spent most of my _____" : "A",
    "We are livinggggg single, Ohhh in a 90s kinda world Im glad I got my _____" : "B",
    "It's a rare condition, this day and age, to read any good news on the newspaper page. Love and tradition of the grand design, some people say it's even harder to ____." : "C",
    "I know my parents love me, Stand behind me come what may. I know now that I'm ready, Because I finally heard them say It's a _____ world than where you come from" : "A",
    "Sister, sister Never knew how much I ____ ya Now that everybody knows I ain't ever gonna let you go" :"B"
}

options = [["A. days, B. nights, C. dreams D. afternoons"],
        ["A. boys, B. girls, C. parents D. friends"],
        ["A. know, B. see, C. find D. search"],
        ["A. different, B. similar, C. cold D. cruel"],
        ["A. loved, B. missed, C. adored D. noticed"]
]
tries = 0
quiz_options = 1
ans = " "
key = " "

while tries < 3:
    
    for key in quiz_bank:
       
        print("__________________________")
        print(key)
        for i in options[quiz_options-1]:
            print(i)
        guess = input("Please enter (A, B, C, or D): ")
        guess = guess.upper()
        if guess == quiz_bank.get(key):
            print("*************************")
            print("**** CORRECT! YOU DA BOMB! ****")
            print("*************************")
             
        elif tries == 3:
            print(f"Sorry the answer was {quiz_bank.get(key)} not {guess}") 
            print("*************************")
               
        else:
            tries += 1
            
            print("*************************")
            print("**** WRONG. TRY AGAIN! YOU GOT THIS! ****")
            print("*************************")
            quiz_options-1
            
            break
        
        quiz_options += 1   
        print(quiz_bank.get(key))


