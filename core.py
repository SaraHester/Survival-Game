##TOOLS

##TRANSFORMATIONS

##RANDOM

##HEALTH
import random


def convert_inventory_to_str(inventory):
    new = ''
    for item in inventory:
        new += convert_found_into_string(inventory[item])
    return new


def convert_found_into_string(found):
    string = '\n' + str(found['name']) + ' = ' + str(
        found['effect']) + ' = ' + str(found['found']) + ' = ' + str(
            found['rarity']) + ' = ' + str(found['extra'])
    return string


def convert_start_into_string(start):
    string1 = '\n' + str(start['name']) + ' = ' + str(
        start['effect']) + ' = ' + start['consumable'] + ' = ' + str(
            start['rarity']) + ' = ' + str(start['extra'])
    return string1


def random_bag(start_items):
    bag = ''
    choices = []
    items = ''
    for line in start_items:
        if start_items[line]['rarity'] != 'Always':
            choices.append(start_items[line])
        else:
            items += "\n" + line
    for i in range(0, 6):
        item = convert_start_into_string(random.choice(choices))
        bag += "\n" + item
    return bag, items


def rest(player):
    if player['health'] <= 950:
        player['health'] += 50
    else:
        player['health'] = 1000

    if player['energy'] <= 950:
        player['energy'] += 50
    else:
        player['energy'] = 1000
    return player


def scavage(player, found_items):
    if player['energy'] >= 20:
        choices = []
        for line in found_items:
            choices.append(found_items[line])
        return random.choice(choices)


def time_effect(count, player):
    if count % 5 == 0:
        player['energy'] -= 10
        player['health'] -= 10
    return player


def not_dead(player):
    if player['health'] > 0 and player['energy'] > 0:
        return True
    elif player['health'] <= 0 or player['energy'] <= 0:
        return False
    else:
        print("I slipped through")