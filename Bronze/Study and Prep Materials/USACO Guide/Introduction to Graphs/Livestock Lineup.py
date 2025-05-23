# i was really close to solving this but unfortunately i lost my train of thought, althrough i know that i prob could get this given a second try
# PSEUDOCODE(v1):
# read N
# array constraints[]
# array cows_order[]
# array alphabetical_order[]
# for i in range(N):
#     read line
#     split line into array
#     constraints[i] = [array[0], array[5]]
# cows_order = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']
# alphabetical_order = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']
# for i in range(N):
#   replace = constraints[i][0].index()
#   current = constraints[i][1].index()
#   alpha1 = alphabetical_order.index(replace)
#   alpha2 = alphabetical_order.index(current)
#   if alpha1 > alpha2:
#       index = 1
#   else:
#       index = -1
#   cows_order.insert(current+index, constraints[i][0])
#   cows_order.pop(replace)
###NEW IDEA:
# original capsule: [['Beatrice'], ['Belinda'], ['Bella'], ['Bessie'], ['Betsy'], ['Blue'], ['Buttercup'], ['Sue']]
# new capsule: [['Beatrice', 'Sue'], ['Belinda'], ['Blue', 'Bella', 'Buttercup'], ['Bessie'], ['Betsy']]
### PSUEDOCODE(v3, works on all)
# read N
# array constraints[]
# array cows_order = [['Beatrice'], ['Belinda'], ['Bella'], ['Bessie'], ['Betsy'], ['Blue'], ['Buttercup'], ['Sue']]
# for i in range(N):
#     read line
#     split line into array
#     constraints[i] = [array[0], array[5]]
# for i in constraints:
#   alphabetically order them(ex. buttercup, blue becomes blue, buttercup but things like sue just stay sue)
# for i in range(N):
#   replace = contraints[i][0].index()
#   current = constraints[i][1].index()
#   alpha1 = alphabetical_order.index(replace)
#   alpha2 = alphabetical_order.index(current)
#   if alpha1 > alpha2:
#       index = 1
#   else:
#       index = -1
#   cows_order.insert(current+index, constraints[i][0])
#   cows_order.pop(replace)
# finally alphabetical_order of cows_order
# print each part of the cows_order in a new line