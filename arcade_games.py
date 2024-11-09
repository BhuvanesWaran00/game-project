import RockPaperScissor as rsp
import GussTheNum as gtn
from sys import exit

def games():
    print("\nSelect game \n1.Rock Paper scissor \n2.Guss the Number")
    op = int(input())
    if op == 1:
        rsp.play()
    elif op == 2:
        gtn.play()

def other_games():
    while True:
        ans = input("\nyou want play other games \nyes - 1 \nno - press any key \n")
        print(ans)
        if ans == "1":
            games()
        else:
            exit("Thank you for Playing \nSee you again")            

if __name__=="__main__":
    print("\nWelcome to arcade games\n")
    games()
