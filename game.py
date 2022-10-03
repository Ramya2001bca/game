number=23
running=True
while running:
     guess=int(input("enter an integer:"))
     if guess==number:
         print("congratulation,you guessed it.")
         running=False
     elif guess<number:
         print("No,it is a little higher than that.")
     else:
           print("No,it is a little lower than that.")
print("Done")
