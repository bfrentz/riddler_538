# Problem:
"""
I have 10 chocolates in a bag: Two are milk chocolate, while the other eight are dark chocolate. One at a time, I randomly pull chocolates from the bag and eat them — that is, until I pick a chocolate of the other kind. When I get to the other type of chocolate, I put it back in the bag and draw again with the remaining chocolates. I don't stop until I have eaten all 10 chocolates.

For example, if I first pull out a dark chocolate, I eat it. (I always eat the first chocolate I pulled out.) If I pull out a second dark chocolate, I eat that as well. If the third one is milk chocolate, I do not eat it (yet), and instead put it back in the bag. Then I start again, eating the first chocolate I pull out.

What are the chances that the last chocolate I eat will be milk chocolate?

"""

import random

# Create a bag of 10 chocolates with 2 milk and 8 dark
def new_bag():
    bag = ['m', 'm', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd']
    return bag


# Simulate the eating of a bag of chocolate according to the rules
# I should really try this out in person...
# But probably not, I am trying to lose weight.
def eat_bag(bag):
    eaten = False

    while bag != []:
        # If new chocolate type
        # Always true for first pull
        # So I always eat the first chocolate
        if not eaten:
            bag_len = len(bag)-1
            pick = random.randint(0, bag_len)
            # eat it
            chocolate = bag.pop(pick)
            # remember what I ate
            last_chocolate = chocolate
            eaten = True
        # If I have eaten a chocolate last pull
        else:
            bag_len = len(bag)-1
            pick = random.randint(0, bag_len)
            # New pull
            chocolate = bag[pick]

            # Does it match previous pull?
            if chocolate == last_chocolate:
                last_chocolate = bag.pop(pick)
                # Reduce bag size so that we can empty array for while loop
                bag_len = len(bag)-1
            else:
                eaten = False

    # Last chocolate
    return last_chocolate



# Number of simulations
runs = 100000

# Number of final chocolates being milk or dark
d = 0
m = 0

# Let's eat a lot
for run in range(runs):
    # Buy a new bag of chocolate
    bag = new_bag()

    # EAT
    last_chocolate = eat_bag(bag)

    if last_chocolate == 'd':
        d += 1
    elif last_chocolate == 'm':
        m += 1

#######
# Results
print('Dark\tMilk')
print(d, '\t', m)

percent = m / (m+d)
print('\nPercentage final chocolates aren\'t real chocolate:')
print(100*percent,'%')


# Solution approaches 1/2 as you increase the number of simulations!


