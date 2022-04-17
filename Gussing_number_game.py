import random
print("Welcome to the number guessing")
print("I am thinking of number betwwen 1 and 100 ")
x=input("choose the difficulty.Type 'easy' or 'hard' : ")
j = random.randint(1, 100)
global p
def hard ():
        if x=="hard" :
             print("you have 5 attempts remaining to guess the number")
             t = 5
             while t != 0:
                p = int(input("make a guess : "))
                if p == j:
                    print("You get it my brother ")
                    print(f"You have {t - 1} attempts remaining to guess the number ")
                    break
                elif p > j:
                    print('Too high\nTry again ')
                    print(f"You have {t - 1} attempts remaining to guess the number ")
                elif p < j:
                    print('Too low\nTry again ')
                    print(f"You have {t - 1} attempts remaining to guess the number ")
                t -= 1

def easy ():

        if x=="easy":
            print("you have 10 attempts remaining to guess the number")
            k= 10
            while k != 0:
                p = int(input("make a guess : "))
                if  p==  j:
                    print("You get it my brother ")
                    print(f"You have {k - 1} attempts remaining to guess the number ")
                    break
                elif   p > j:
                    print('Too high\nTry again ')
                    print(f"You have {k - 1} attempts remaining to guess the number ")
                elif   p < j:
                    print('Too low\nTry again ')
                    print(f"You have {k - 1} attempts remaining to guess the number ")
                k-= 1
hard()
easy()
