# This code takes a number of inputs and pick them randomly 
# The most pick per round wins the round
# The most rounds won becomes KING
# The second in line is the person with many(or most) picks but to not with the most rounds
# for sololearn reasons i have put the names, number of rounds and number of picks per round rather than 'input()'
# I noticed the code output is properly displayed how it should on solo learn mobile. Try using the web version or any IDE
# Suggestions on how to improve the code are most welcome

# Upvote and Share if you liked the code👍👍. Thank you 🙇‍♂️🙇‍♂️

def KingPredictor(_list):
    import random
    tot_rounds = 5000  # Total number of rounds played
    round_picks = 100  # Number of random picks per round
    _list.sort(key=len, reverse=True)
    _dict = {}
    for i in _list:
        _dict[i] = 0

    _dict2 = _dict.copy()
    # Forming a dictionary from this list where the item count are all zero

    for i in range(tot_rounds):
        # The code below represents a round of random picks
        _list2 = []
        for v in range(round_picks):
            picked = random.choice(_list)
            _dict[picked] += 1
            # This line always increase the picks in the original dictionary which was set to zero
            _list2.append(picked)
            # This line helps create another list which I count to know who won the round

        maxi = _list2[0]
        for item in _list2:
            if _list2.count(item) > _list2.count(maxi):
                maxi = item
        _dict2[maxi] += 1
    #   Gets the most picked item per loop and increases the count

    _dictsort = dict(sorted(_dict.items(), key=lambda x: x[1], reverse=True))
    _dict2sort = dict(sorted(_dict2.items(), key=lambda x: x[1], reverse=True))
    # These two lines sorts the dictionary by the values and returns a new dictionary
    print()
    
    sortedkeys1 = list(_dict2sort.keys())
    sortedkeys2 = list(_dictsort.keys())
    sortedvalues = list(sorted(_dictsort.values(), reverse=True))
    pos = ('1st', '2nd', '3rd', '4th', '5th', '6th', '7th')
    pos_dict = dict(zip(sortedvalues, pos))
    # These two lines sort the keys so i can print the first items as the KING
    # And also the positon based on number of total picks

    def length(name):
        return len(_list[0]) - len(name)
    # Helps to get the distance correctly

    col1, col2, col3 = 'NAMES', 'ROUND WINS', 'TOTAL PICKS'
    print(f"{col1}{length(col1) * ' '} | {col2} | {col3}")
    print()
    # Table header

    for key, value in _dict2sort.items():
        number = len(str(_dict2sort[sortedkeys1[0]])) - len(str(value))
        distance2 = number * ' '
        distance = length(key) * ' '
        print(
            f'{key}{distance} |    {value}    {distance2} |   {_dictsort[key]}({pos_dict.get(_dictsort[key], "unranked")})')
    #This loop help to show all the items with their number of round wins and their total number of picks

    print(f'\n{sortedkeys1[0].upper()} is KING👑 having won {_dict2[sortedkeys1[0]]} rounds')
    if sortedkeys1[0] == sortedkeys2[0]:
        num = 1
        print(f'{sortedkeys2[num].upper()} is KING\'S HAND with {_dict[sortedkeys2[num]]} total picks')
    else:
        num = 0
        print(f'{sortedkeys2[num].upper()} is the unlucky one despite {_dict[sortedkeys2[num]]}(most) total picks')
    # The lines above prints the winner and runner up
    print()
# End of function
#-------------------------------------------------------------------------------------------------------------------------------------

# First List
physicists = ['Albert Einstein', 'Isaac Newton', 'Gallileo Gallilie', 'Niel Bohr',
 'Marie Curie', 'Michael Faraday', 'Archimedes']

#Using the function first time
KingPredictor(physicists)

"""Run The code below to put your own list separated by comma (',') """

# Second List
another_list = ["KK", 'JANET', 'ELIJAH', 'ENGR. DICK', 'FORTUNE']

#Using the function on another list
KingPredictor(another_list)

print("TIPS: King's Hand is the person with the most total picks who isn't the winner")
#your_list = input().split(',')
#KingPredictor(your_list)

    
    # There were few things i wasn't able to achieve;

# 1.Where in the rare case, the same item has same total number of picks. I would like to sort it then by the number of rounds won before printing but that's not usually the case as the computer automatically picks who it likes the most lol

# 2. When print the names with their numbers, i would like all the numbers and the dash symbol to be on the same line for better readability but right now the depend on the length of the name used

#UPDATE!!
    # I was able to improve the readability which was stated in NO 2 above


