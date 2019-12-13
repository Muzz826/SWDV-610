# Developed by: Ben Muzzy

"""
Three missionaries and three cannibals come to a river and find a boat that holds two people. Everyone must get across the river to continue on the journey. However, if the cannibals ever outnumber the missionaries on either bank, the missionaries will be eaten.
"""

def main():
    # Start with 3 missionaries and 3 cannibals on bank 1
    left_bank = {'cannibals': 3, 'missionaries': 3}
    right_bank = {'cannibals': 0, 'missionaries': 0}
    boat = {'cannibals': 0, 'missionaries': 0}
    boat_ride(left_bank, right_bank, boat)

def boat_ride(left_bank, right_bank, boat):
    '''
    Function "boat_ride" moves and keeps track
    of all the missionaries & cannibals as they move
    through each checkpoint.
    '''
    # all() method validates if all elements are true
    if all(empty == 0 for empty in right_bank.values()):
        # values() method returns the list of values in the right_bank
        cp_status(left_bank, boat, right_bank)
    # Each ride 1 missionary leaves "left_bank" and enters the boat
        left_bank['cannibals'] -= 1
        boat['cannibals'] += 1

    left_bank['missionaries'] -= 1
    boat['missionaries'] += 1
    cp_status(left_bank, right_bank, boat)

    if all(empty == 0 for empty in left_bank.values()):
        # 1 cannibal and 1 missionary ride the boat
        boat['cannibals'], boat['missionaries'] = 0, 0
        # 1 cannibal and 1 missionary enter "right_bank"
        right_bank['cannibals'] += 1
        right_bank['missionaries'] += 1
        cp_status(left_bank, right_bank, boat)
        return

    # 1 missionary moves to right_bank
    boat['missionaries'] -= 1 
    right_bank['missionaries'] += 1
    cp_status(left_bank, right_bank, boat)

    # 1 cannibal leaves the left_bank
    left_bank['cannibals'] -= 1
    # 1 cannibal moves to the boat
    boat['cannibals'] += 1 
    cp_status(left_bank, right_bank, boat)

    # 1 cannibal leaves the boat
    boat['cannibals'] -= 1
    # 1 cannibal moves to the right_bank
    right_bank['cannibals'] += 1 
    cp_status(left_bank, right_bank, boat)
    boat_ride(left_bank, right_bank, boat)


def cp_status(cp1, cp2, cp3):
    '''Function "cp_status" stores and displays what checkpoint
    each of the cannibals and missionairies are at after each boat ride.

    Variable cp means checkpoint. There are 3 checkpoints(left_bank, boat, right_bank)'''

    # using triple double-quotes for mult-line string
    curr_stage = """
    Left Bank: {} cannibals, {} missionaries
    Right Bank: {} cannibals, {} missionaries
    Boat: {} cannibals, {} missionaries
    """
# Ouputs where each cannibal & missionary are after each boat ride
    print(curr_stage.format(cp1['cannibals'], cp1['missionaries'], cp2['cannibals'], cp2['missionaries'],
    cp3['cannibals'], cp3['missionaries']))


main()