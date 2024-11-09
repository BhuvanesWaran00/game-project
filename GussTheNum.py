from random import choice



you = computer = game_count= 0

def play():
    print("Welcome to Guss The Number Game")
    start()


def player(rag,i):


        try:
            
            print(f"\nEnter the number between {rag[0]} -{rag[i]} \n")
            op = int(input())
        except:
            print("input value must be number")
            return 0
        

        return op

def pc(rag):
    return choice(rag)

def start():
    
    while True:
        try:
            level=int(input("\nPlese Selact the level \n1.Easy \n2.medium \n3.Hard\n"))
        
        

            if level == 1:
                rag = [0, 1]
                break
            elif level == 2:
                rag = [0, 1, 2, 3, 4, 5]
                break
            elif level == 3:
                rag = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                break
            else:
                print("Please enter the number between 1 and 3.")
        except:
            print("input value must be number")
    
    rag_last_index = len(rag)-1
    wrong_op = True

    while wrong_op:
        player_1 = player(rag,rag_last_index)
        if player_1 <0 or player_1 > rag[rag_last_index]:
            print(f"Please enter the number between 0 and {rag[rag_last_index]}.")
        else:
            wrong_op=False 
    
    player_2 =pc(rag)

    print(f"your choice is{player_1} \ncomputer choice is{player_2}")

    if player_1 == player_2:
        print("player is win")
        result(1)
    
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
