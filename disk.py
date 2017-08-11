##item_dictionary
######split line at comma
######split transformations at /
######split requirements at /
######split seperate requirements at -
#########ex. Wood, 0, Timber/Tools/Fence, Dagger-10 Energy/Dagger-10 Energy/Rope-20 Energy
#########Timber transformation takes a dagger and 10 energy
#########Tools transformation takes a dagger and 10 energy
#########Fence transformation takes rope and 20 energy


def open_item_dictionary():
    item_dictionary = {}
    with open('item_dictionary.txt', 'r') as file1:
        file1.readline()
        dictionary = file1.readlines()
    for line in dictionary:
        item, effect, trans, requ, found, rarity, extra = line.split(' = ')
        trans = trans.split(', ')  #list
        requ = requ.split(', ')  #list
        trans1 = {}
        for i in range(1, len(trans)):
            trans1[str(trans[i])] = requ[i - 1]
        item_dictionary[item] = {
            'name': item,
            'effect': effect,
            "transformations": trans1,
            'found': found,
            'rarity': rarity,
            'extra': extra.strip()
        }
    return item_dictionary
