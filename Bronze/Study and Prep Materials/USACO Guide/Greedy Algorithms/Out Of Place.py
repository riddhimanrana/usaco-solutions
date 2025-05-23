### PSEUDOCODE
# read N
# current_list = [read N lines]
# correct_list = sorted(current_list)
# #now we want to find the out of place number
# bessie = 0
# for i in range(len(correct_list)):
#   if correct_list[i] != current_list[i]
#       bessie = correct_list[i]
# bessie_correct_index = correct_list.index(bessie)
# bessie_current_index = current_list.index(bessie)
# direction = True #this means backwards
# if bessie_current_index > bessie_correct_index:
#   direction = False #this means backwards
# consecutive_movement = 0
# swaps = 0
# pointer = bessie_current_index
# while current_list != correct_list:
#   new_pointer = pointer +=1
#   current_list[pointer] = current_list[new_pointer]
#   current_list[new_pointer] = current_list[pointer]
#   swaps += 1
# print(swaps)

N = int(input())
current_list = []
for _ in range(N):
    current_list.append(int(input()))

correct_list = sorted(current_list)
bessie = 0
for i in range(len(correct_list)):
    if correct_list[i] != current_list[i]:
        bessie = correct_list[i]
        break
        
bessie_correct_index = correct_list.index(bessie)
bessie_current_index = current_list.index(bessie)

direction = True # by default we go forwards
if bessie_current_index > bessie_correct_index:
    direction = False # this means backwards

print(direction)
if direction == False:
    correct_list.reverse()
    current_list.reverse()

consecutive_movement = 0
swaps = 0
pointer = bessie_current_index
while current_list != correct_list:
    new_pointer = pointer + 1
    if new_pointer < len(current_list):
        print("here")
        current_list[pointer], current_list[new_pointer] = current_list[new_pointer], current_list[pointer]
        if current_list[new_pointer] == current_list[pointer]:
            if consecutive_movement == 0:
                swaps += 1
            consecutive_movement += 1
        else:
            consecutive_movement = 0
            swaps += 1
    else:
        break

print(swaps)