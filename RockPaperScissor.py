# Rock Paper scissors Game
from random import choice



you = computer = game_count= 0

def play():
    print("Welcome to Rock Paper scissors Game")
    start()

def player():


        try:
            op = int(input("\nEnter \n1. Rock \n2. paper \n3. scissor \n"))
        except:
            print("input value must be number")
            return 0
        

        return op

def pc():

    return int(choice("123"))


def start():
    wrong_op = True

    while wrong_op:
        player_1 = player()
        if player_1 < 1 or player_1 > 3:
            print("Please enter an option between 1 and 3.")
        else:
            wrong_op=False 
    
    player_2 =pc()

    print(f"your choice is{player_1} \ncomputer choice is{player_2}")   

    if player_1 == 1 and  player_2 == 3:
        print("player is win")
        result(1)
    elif player_1 == 2 and  player_2 == 1:
        print("player is win")
        result(1)
    elif player_1 == 3 and  player_2 == 2:
        print("player is win")
        result(1)
    elif player_2 == player_1:
        print("tie")
        result(2)
    else:
        print("computer win")
        result(0)
    
def result(x):
    global you,computer

    if x == 1:
        you += 1
    elif x== 0:
        computer += 1

    print(f"your score is: {you} \ncomputer score is: {computer} \n  ")
    play_again()

def play_again():
    from arcade_games import other_games 
    while True:
        global game_count
        game_count += 1
        ans = input("you want play again \nyes - 1 \nno - press any key \n")
        print(ans)
        if ans == "1":
            start()
        else:
            break

    print(f"\nTotal game count: {game_count} \nyour score is: {you} \ncomputer score is: {computer} \nOverall winner: {"you" if you > computer else "computer"}")
    other_games()    
    
# main

if __name__=="__main__":
    

    play()
    