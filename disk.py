##found_items
######split line at comma
######split transformations at /
######split requirements at /
######split seperate requirements at -
#########ex. Wood, 0, Timber/Tools/Fence, Dagger-10 Energy/Dagger-10 Energy/Rope-20 Energy
#########Timber transformation takes a dagger and 10 energy
#########Tools transformation takes a dagger and 10 energy
#########Fence transformation takes rope and 20 energy
import core


def convert_found_items(items):
    converted_items = {}
    for line in items:
        item, effect, found, rarity, extra = line.split(' = ')
        converted_items[item] = {
            'name': item,
            'effect': effect,
            'found': found,
            'rarity': rarity,
            'extra': extra.strip()
        }
    return converted_items


def convert_start_items(items):
    converted_items = {}
    for line in items:
        item, effect, cons, rarity, extra = line.split(' = ')
        converted_items[item] = {
            'name': item,
            'effect': effect,
            'consumable': cons,
            'rarity': rarity,
            'extra': extra.strip()
        }
    return converted_items


def convert_crafting_items(items):
    count = 0
    converted_items = {}
    for line in items:
        count += 1
        item, requ, extra = line.split(' = ')
        requ = requ.split(', ')  #list
        converted_items[count] = {
            'number': count,
            'name': item,
            'requirements': requ,
            'extra': extra.strip()
        }
    return converted_items


def open_found_items():
    with open('found_items.txt', 'r') as file1:
        file1.readline()
        dictionary = file1.readlines()
    return convert_found_items(dictionary)


def open_start_items():
    with open('start_items.txt', 'r') as file2:
        file2.readline()
        dictionary = file2.readlines()
    return convert_start_items(dictionary)


def open_crafting_items():
    with open('crafting_items.txt', 'r') as file3:
        file3.readline()
        dictionary = file3.readlines()
    return convert_crafting_items(dictionary)


def open_inventory(name):
    with open('Users/{}inventory.txt'.format(name), 'r') as file4:
        file4.readline()
        dictionary = file4.readlines()
    return dictionary


def append_inventory(text, name):
    with open('Users/{}inventory.txt'.format(name), 'a') as file6:
        file6.write(text)


def make_new_file(name):
    with open('Users/{}inventory.txt'.format(name), 'w') as file7:
        file7.write("")


def write_over_file(name, text):
    with open('Users/{}inventory.txt'.format(name), 'w') as file8:
        file8.write(core.convert_inventory_to_str(text))