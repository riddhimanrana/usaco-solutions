#### 10/10 TESTCASES!!! double winssss ####

import sys
sys.stdin = open("hps.in", "r")
sys.stdout = open("hps.out", "w")

def move_check(move_a, move_b):
    wins = 0
    if move_a == "hoof" and move_b == "scissors":
        wins += 1
    elif move_a == "scissors" and move_b == "paper":
        wins += 1
    elif move_a == "paper" and move_b == "hoof":
        wins += 1
    return wins

N = int(input())
player1 = [0] * N
player2 = [0] * N
for i in range(N):
    player1[i], player2[i] = map(int, input().split())


max_wins = 0
moves = ["hoof", "paper", "scissors"]
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and i != k and j != k:
                move1 = moves[i]
                move2 = moves[j]
                move3 = moves[k]
                current_wins = 0
                for l in range(N):
                    move_a = player1[l]
                    move_b = player2[l]
                    
                    move_type = {1: move1, 2: move2, 3: move3}
                    if move_a in move_type:
                        move_a = move_type[move_a]
                    if move_b in move_type:
                        move_b = move_type[move_b]
                    
                    win = move_check(move_a, move_b)
                    current_wins += win
                if current_wins > max_wins:
                    max_wins = current_wins

print(max_wins)

