import random

print("Welcome To The Cow Bull Game")

a=random.randint(100,999)

attempts=5

def make_number():
    global attempts
    
    while True:
        bulls=0
        cows=0
        num=str(a)
        while True:
            attempts=attempts-1
            ch=input("enter a 3 digits number :")
            if num==ch:
                print("You guessed it right \n You got 3 bulls \n You WON the game")
            elif attempts==0:
                print("you have lost all attempts answer is "+str(num))
                break
            else:
                for i in range(len(num)):
                    if num[i]==ch[i]:
                        bulls=bulls+1
                    count=0
                for j in ch:
                    if j in num:
                        count=count+1
                cows=count-bulls
                print("The number of cows are",cows)
                print("The number of bulls are",bulls)
make_number()

    
