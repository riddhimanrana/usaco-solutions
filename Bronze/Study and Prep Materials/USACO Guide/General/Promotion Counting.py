import sys
sys.stdin = open('promote.in', 'r')
sys.stdout = open('promote.out', 'w')

# we need to count promotions for bronze to silver, silver to gold, and gold to platinum
# for example for sample input:
# 1 2
# 1 1
# 1 1
# 1 2
# we can see that before the contest started there were 1 bronze, 1 silver, 1 gold, and 1 platinum. Afterwards, we see that our total cowcount increased by 2, which means 2 people joined in
# so 1 person who joined stayed in bronze, the other promoted all the way to silver
# so we have 1 bronze to bronze(that one guy), and the other guy has 1 bronze to silver, 1 silver to gold, and 1 gold to platinum
# that outputs:
# 1
# 1
# 1

# we can use a 2d array to store the promotions
bronze = [int(a) for a in input().split(" ")]
silver = [int(b) for b in input().split(" ")]
gold = [int(c) for c in input().split(" ")]
platinum = [int(d) for d in input().split(" ")]

platinum_promotions = platinum[1] - platinum[0]
gold_promotions = platinum_promotions + gold[1] - gold[0]
silver_promotions = gold_promotions + silver[1] - silver[0]

print(silver_promotions)
print(gold_promotions)
print(platinum_promotions)

# if there is an increase in 1 platinum promotion:
# then, we add 1 bronze to silver promotion, 1 silver to gold promotion, and 1 gold to platinum promotion
# if there is an increase in 1 gold promotion:
# then, we add 1 bronze to silver promotion, and 1 silver to gold promotion
# lastly if there is an increase in 1 silver promotion:
# then, we add 1 bronze to silver promotion