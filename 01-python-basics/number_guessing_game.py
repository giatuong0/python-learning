from random import randint
secret=randint(0, 10)

print("Welcome!")
guess = -1
while guess !=secret:    
 g = input("Guess the number: ")
 guess = int(g)
 if guess == secret:
  print("you win")
 else:
     if guess > secret:
         print("too high")
     else:
         print("too low")
print("Game over!")
   
