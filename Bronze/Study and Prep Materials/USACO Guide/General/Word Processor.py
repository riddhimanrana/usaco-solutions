# we are given 2 integers N and K
# next u get N lines seperated by single spaces
# pesudocode:
# read N, K
# store the words in a list
# for each word in the list:
# store nunber of characters

import sys
sys.stdin = open('word.in', 'r')
sys.stdout = open('word.out', 'w')

N, K = map(int, input().split())
words = list(input().split())
line = K
first_word = True
for word in words:
    wordchar = len(word)
    if line - wordchar >= 0:
        if not first_word:
            print(" ", end="")
        print(word, end="")
        line -= wordchar
        first_word = False
    else:
        print("\n" + word, end="")
        line = K - wordchar
        first_word = False