#!/usr/bin/env python3

quiz_bank= {
    "In West Philadelphia born and raised. On the playground is where I spent most of my _____" : "A",
    "We are livinggggg single, Ohhh in a 90s kinda world Im glad I got my _____" : "B",
    "It's a rare condition, this day and age, to read any good news on the newspaper page. Love and tradition of the grand design, some people say it's even harder to ____." : "C",
    "I know my parents love me, Stand behind me come what may. I know now that I'm ready, Because I finally heard them say It's a _____ world than where you come from" : "A",
    "Sister, sister Never knew how much I ____ ya Now that everybody knows I ain't ever gonna let you go" :"B",
    "Boy, the way Glenn Miller played, songs that made the hit parade. Guys like me we had it made. _____ were the days" : "D",
    "Flintstones, meet the Flintstones They're the _____ Stone Age Family From the town of Bedrock They're a page right out of history" : "C",
    "So no one told you life was going to be this way. Your job's a joke, you're broke, you're love life's _____." : "A"
}

options = [["A. days, B. nights, C. dreams D. afternoons"],
        ["A. boys, B. girls, C. parents D. friends"],
        ["A. know, B. see, C. find D. search"],
        ["A. different, B. similar, C. cold D. cruel"],
        ["A. loved, B. missed, C. adored D. noticed"],
        ["A. they, B. 1950s, C. these D. those"],
        ["A. interesting, B. darndest, C. modern D. coolest"],
        ["A. DOA, B. A-Okay, C. Okay-Jose D. Ok"]
]
tries = 0
quiz_options = 1


while tries < 2:
    
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
            
             
        elif tries == 2:
            print("Sorry you've exhausted your attempts") 
            print(f"You have incorrectly answered {tries+1} questions. You can only get 3 incorrect!")
            print("*************************")
            break
        else:
            tries += 1
            
            print("*************************")
            print(f"Sorry the answer was {quiz_bank.get(key)} not {guess}")
            print(f"You have incorrectly answered {tries} question(s). You can only get 3 incorrect!")
            print("*************************")
            #quiz_options-1
            #print(temp[temp.index(test_key)-1])
            
            
        
        quiz_options += 1   
        #print(quiz_bank.get(key))


