# Cowntact Tracing 2 Problem
### PROBLEM:
# FJ has N cows in a line, and however there isa  sickness spreading throughout.
# Init, some cows start off infected. Then, every night an infected cow spreads the sickness to the cows on their left and right(if they do exist).
# Once a cow is infected, it stays infected forever.
# After some amt of nights, FJ realizes that the issue is out of controll, so he tests the cows to see who has the sickness.
# I need to find the minimum number of cows, that could have started with the sickness.

### INPUT:
# First we're given N, the number of cows that FJ has.
# Then, we're given an N character of 1s and 0s, 1 meaning infected, 0 meaning not infected after some number of nights.
### OUTPUT:
# Output a single integer being the minimum number of cows, that could have started with the sickness.

### Solution PATH:
# First read the input, get the number of cows, and store all the cows in a list.
# Then, we need to find the number of cows that are initially infected, so we make the main function.
# Start of with assuming that all the cows that are given to use currently infected, were the initially infected cows. So we set the initially infected cows to the number of cows that are currently infected
# Then, we reduce that by one, so we assume that there is one less initially infected cows, and try to justify that, and run all possible testcases on that(brute force).
# If we can't justify that, then we print out that the number of initially infected cows is the number of cows that are currently infected(or whatever is in that variable).
# We continue to loop down one by one until we find the minimum number of initially infected cows, such that it is possible given the input.

### CODE:
def find_initial_infected_cows(N, bitstring):
    infected_count = 0

    for i in range(N):
        if bitstring[i] == '1':
            infected_count += 1

    return max(1, infected_count)

N = int(input())
bitstring = input().strip()

print(find_initial_infected_cows(N, bitstring))
