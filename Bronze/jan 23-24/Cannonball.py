## PSEUDOCODE
# read N, S
# types = []
# values = []
# for _ in range(N):
#    type, value = input().split()
#    types.append(type)
#    values.append(int(value))
# targets_hit = 0
# bessie_pos = S
# direction = 1
# while 1 <= bessie_pos <= N:
#    if types[bessie_pos - 1] == 1:
#        if power >= values[bessie_pos - 1]:
#            if values[bessie_pos - 1] != 0:
#               targets_hit += 1
#        values[bessie_pos - 1] = 0
#    elif types[bessie+pos - 1] == 0:
#        power += values[bessie_pos - 1]
#        direction *= -1
# bessie_pos += power * direction

N, S = map(int, input().split())
types = []
values = []
for _ in range(N):
    type, value = map(int, input().split())
    types.append(type)
    values.append(value)

targets_hit = 0
bessie_pos = S
power = 1
direction = 1
visited = set()
no_new_target_counter = 0  # counter for position changes without a new target hit

repeats = 0 # technically this is unncesary but i just added it to make sure that the program doesn't run forever
while 1 <= bessie_pos <= N and repeats < 3*N:
    repeats += 1
    current_state = (bessie_pos, power, direction)
    if current_state in visited:
        break
    visited.add(current_state)
    if types[bessie_pos - 1] == 1:
        if power >= values[bessie_pos - 1]:
            targets_hit += 1
            types[bessie_pos - 1] = -1
            #if values[bessie_pos - 1] != 0: :(((( this was so sad, i just had to edit this a lil to get 20/20 testcases
            #    targets_hit += 1
            #    values[bessie_pos - 1] = 0
    elif types[bessie_pos - 1] == 0:
        power += values[bessie_pos - 1]
        direction *= -1

    bessie_pos += power * direction

print(targets_hit)
