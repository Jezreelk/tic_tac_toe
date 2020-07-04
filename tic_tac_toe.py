
import itertools

def win(current_game):

    def all_same(lis):
        if lis.count(lis[0]) == len(lis) and lis[0] != 0:
            return True
        else:
            return False

    # Horizontal
    for row in game:
        print(row)
        if all_same(row):
            #row.count(row[0]) == len(row) and row[0] !=0:
            Print(f"Player {row[0]} is The Winner horizontally !") #row[0])
            return True
     # Vertical
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):#check.count(check[0]) == len(check) and check[0] !=0:
            print(f"Player{check[0]} is the winner vertically! ")
            return True
      #/ Diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])
    if all_same(diags):#diags.count(diags[0]) ==  len(diags) and diags[0] !=0:
        print(f"player {check[0]} has won diagonally (/) ")
        return True


    # Diagonal (\)
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if all_same(diags): #diags.count(diags[0]) == len(diags) and diags[0] !=0:
        print(f"player {diags[o]} has won Diagonally (\)")

    if all_same(diags):
        print(f"Player {diags[0]} has won diagonally(\\)")
        return True

    return False

def game_board(game_map, player=0, row=0, column=0, just_display= False):

    try:
        if game_map [row][column] !=0:
            print("This space is occupied, try another!")
            return False

        print("   "+"   ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError:
        print("Error make sure you enter row column as 0 1 or 2")
        return False
    except Exception as e:
        print(str(e))
        return False

#Play until someone has won
play = True
players = [1,2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

#(" game_size = int(input(\"What size game of TicTacToe?\"))\n"
# "    game = [[0 for i in range (game_size)] for i in range(game_size)]\n"
# "    print(game)\n")

    game_won = False
    player_cycle = itertools.cycle([1,2])
    game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_cycle)
        played = False
        while not played:
            print(f"Player: {current_player}")
            column_choice = int(input("Which column?"))
            row_choice = int(input("Which row?"))
            played = game_board(game,player =current_player,row = row_choice, column = column_choice)

        if win(game):
            game_won = True
            again = input ("The game is over, would you like to play again? (y/n)")
            if again.lower() == "y":
                print("Restarting")
            elif again.lower() == "n":
                print("Bye!")
                play = False
            else:
                print("Not a valid answer, goodbye")
                play = False








