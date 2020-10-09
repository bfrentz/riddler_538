"""
Every weekend, I drive into town for contactless curbside pickup at a local restaurant. Across the street from the restaurant are six parking spots, lined up in a row.

While I can parallel park, it’s definitely not my preference. No parallel parking is required when the rearmost of the six spots is available or when there are two consecutive open spots. If there is a random arrangement of cars currently occupying four of the six spots, what’s the probability that I will have to parallel park?

"""


import random

# Create a street with 6 spaces (2 open, 4 cars)
def new_street():
    options = ['o', 'o', 'c', 'c', 'c', 'c']
    street = []
    while options != []:
        options_len = len(options)-1
        street.append(options.pop(random.randint(0, options_len)))
    return street


# Check to see if you have to parallel park
def park(street):

    # Check last spot
    if street[-1] == 'o':
        return False

    # Check for consecutive spots
    spot1 = street.index('o')
    spot2 = street.index('o', spot1+1, len(street))
    if spot2 == spot1+1:
        return False

    return True


# main
def main():

    # Number of simulations
    runs = 1000000

    # Number of times you have to parallel park
    p = 0

    for run in range(runs):
        street = new_street()
        parallel = park(street)
        if parallel:
            p += 1

    # Percent
    percent = p / runs

    # Results
    print('Simulations run:')
    print(runs, '\n')
    print('Percentage of time you have to parallel park:')
    print(100*percent, '%')


main()

