"""
this is for git practice
"""
name="Jannet"
no_of_Lives=4
no_of_Attempt=0


while no_of_Attempt < no_of_Lives:
     TRY=input("Guess the name?-->")
     if(name==TRY):
        print("Congratulations, you won this game")
        break
     elif(name!=TRY):
        no_of_Lives-=1
        print(f"you have {no_of_Lives} lives remaining, u won")