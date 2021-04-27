import random
number=random.randint(1,9)
chances=0
while chances<5:
    guess=int(input("Enter Your Guess:"))
    if guess== number:
        print("Congrats You Won")
        break
    elif guess<number:
        print("Your Guess Was To Low, Guess A Higher Number Than", guess)
    else:
        print("Your Guess Was To High, Guess A Number Lower Than", guess)
    chances+=1
if not chances<5:
    print("You Lose")