# N cows before Bessie, so she is the N + 1th cow
# There are K farmers and they're interviewing the cows
# each cow i's interview time is t_i
# Bessie wants to find what time she is going to be interviewed and which farmers can interview her
# if multiple farmers finish at the same time, then the next cow can choose to be interviewed by any of the available farmers according to their preference
# one more thing: at time 0, farmer i will stasrt interviewing cow i(so like based on the cows array), for the first K cows, they don't have a choice it's just the order of the farmers and order of the cows

## Sample:
# 6 3
# 3 1 4159 2 6 5
## steps:
# what happens here is first line tells us that there are 6 cows before bessie(that's the N variable), and there are 3 farmers(K variable)
# the second line tells us the interview times of the cows
# so the first cow takes 3 minutes to be interviewed, second cow will take 1 minute, and third cow will take 4159 minutes
# so farmer 1 will interview cow 1, farmer 2 will interview cow 2, and farmer 3 will interview cow 3
# time 0: farmer 1 interviews cow 1, farmer 2 interviews cow 2, farmer 3 interviews cow 3
# time 1: farmer 2 is finished with cow 2, so he can interview cow 4 now, and since he's the only available farmer, cow 4 must choose farmer 2
# time 3: there's 2 possibilities at this stage, since there are 2 available farmers, cow 5 can choose either farmer 1/farmer 2
# if cow 5 chooses farmer 1 and cow 6 then has to interview w/farmer 2 since he's the only available farmer:
    # time 8: farmer 2 is inished w/cow 6, so now bessie can choose farmer 2
    #(not significant but) at time 9: farmer 1 is finished w/cow 5
# if cow 5 chooses farmer 2 and cow 6 then has to interview w/farmer 1 since he's the only available farmer:
    # time 8: farmer 1 is finished w/cow 6, so now bessie can choose farmer 1
    #(not significant but) at time 9: farmer 2 is finished w/cow 5

# so this means that in the first possibility of events, at the end farmer 1 was the only available farmer
# in the second possibiliy of events, at the end farmer 2 was the only available farmer
# if we combine these together, this means that farmer 1 or 2 are coming to bessy so we put 110 as the output

## Plan
# we need to keep of each farmer, at each time interval, if they are interviewing a cow or not
# we can use a list of lists to keep track of this
# so we need to do a thing where
# when a cow has multiple farmers as possibilties, we need to sort of simulate every single possible event that could surround that, and it could get reaaaaly complicated
# basically when a cow has 3 possibilities, then the next cow has 2 possibiltiies, and finally the last cow has 1 possibility
# with this we neeed to try all the possibilities of possibilties and then we need to at the end of those calculations find out which farmers are available for bessy with each string of events
# at the end, we need to maybe take this giant list of possibiltiies, combine them together to finally output the right bit-wise string that is available for bessie

# iterate over the cows, and for each cow, iterate over the farmers and check if they are available
# if they are, then we can add them to a list of available farmers
# if they are not, then we can remove them from the list of available farmers
# we can keep track of the available farmers by using a list of booleans
# at the end, we can just iterate over the list of booleans and add the farmer to the output string if they are available


## Code
# inputs

N, K = map(int, input().split())  # _ is N, K is K
interview_times = list(map(int, input().split())) # interview times


available_farmers = [] # this stores the available farmers to each cow(used to find available farmers for bessie)
bessie_time = 0
farmer_position = list(range(K)) # farmer indexes from [0,1,2...K]
farmer_interviews = [] # store the interview times of the farmers(aka how long till they are available for neKt interview)


for i in range(K): # iterate over K farmers
    farmer_interviews.append(interview_times[i]) # current interview time of the farmer???
    available_farmers.append([i]) # this is the index of where each farmer is at in the interview process

# now we need to find time first, and thennnn do the values
while len(interview_times) not in farmer_position:#this shows there's a farmer ready to interview bessie, and we store that time # this is to find the TIME that bessie is going to be interviewed
    next_available = min(farmer_interviews) #find the minimum time it takes for the next farmer to be available and add those all together to find the time it takes for bessie to be interviewed
    bessie_time += next_available # add the time it takes for the next farmer to be available
    for i in range(K): # iterate over the number of farmers
        farmer_interviews[i] -= next_available
    if farmer_interviews.count(0) > 1: # if there are multiple farmers that are available, 0 denotes that the farmer has no other cows they're interviewing
        frmers = [] # store the indexes of the available farmers
        for i in range(K): # iterate over the number of farmers
            if farmer_interviews[i] == 0:
                frmers.append(i)
        available_farmers.append(frmers)
    for i in range(K): # iterate over the number of farmers
        if farmer_interviews[i] == 0: # if the farmer is available
            farmer_position[i] = max(farmer_position) + 1 # add the max farmer + 1
            if farmer_position[i] < len(interview_times):
                farmer_interviews[i] = interview_times[farmer_position[i]]
print(bessie_time) # print the time it takes for bessie to get a chance to be interviewed




last = 0 # previous value
current = len(available_farmers) # current value
# available_farmers is the combination of farmers that are available for each cow

while last != current: # this is to find the available farmers for bessie
    found = False # this is to break out of the loop for a certain condition
    for i in range(len(available_farmers)): # iterate over each cow

        for j in range(len(available_farmers[i])): # for each cow, iterate over the available farmers
            for k in range(len(available_farmers)): # iterate over each cow
                if available_farmers[i][j] in available_farmers[k] and i != k: # if a farmer is available for both cows then make a new list and combine the available farmers
                    available_farmers.append(available_farmers[i] + available_farmers[k]) # add the available farmers to the list
                    for l in range(len(available_farmers) - 1, -1, -1): #either reverse or not reverse, i think i'll try both on usaco server
                        if l == k or l == i: # remove farmers that are already in the list
                            available_farmers.pop(l)
                    found = True # we've found what we need for this iteration of the cow so we go to the next cow
                    break
            if found:
                break
        if found:
            break
    last = current
    current = len(available_farmers)


# duplicate handling and stuff
for i in range(len(available_farmers)): # remove duplicates from the list of available farmers
    available_farmers[i] = list(dict.fromkeys(available_farmers[i]))

possibleInterviewer = 0 # store the index of the farmer who can interview bessie
for i in range(len(available_farmers)): # find the available farmers for bessie
    if farmer_position.index(len(interview_times)) in available_farmers[i]: # if da farmer is in the list of hte current iterations
        possibleInterviewer = i # set the list to index i
        break

bessie_farmersFinal = [] # finding bitwise ops for the available farmers for bessie
for i in range(len(farmer_position)):
    if i in available_farmers[possibleInterviewer]:
        bessie_farmersFinal.append('1')
    else:
        bessie_farmersFinal.append('0')


print(''.join(bessie_farmersFinal))
