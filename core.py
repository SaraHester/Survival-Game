##TOOLS

##TRANSFORMATIONS

##RANDOM

##HEALTH
import random


def convert_inventory_to_str(inventory):
    new = ''
    for item in inventory:
        new += convert_item_to_str(inventory[item])
    return new


def convert_item_to_str(item):
    return item['name'] + ', ' + str(1)


def convert_start_into_string(start):
    string1 = '\n' + str(start['name']) + ' = ' + str(
        start['effect']) + ' = ' + start['consumable'] + ' = ' + str(
            start['rarity']) + ' = ' + str(start['extra'])
    return string1


def always_items(start_items):
    items = ''
    for line in start_items:
        if start_items[line]['rarity'] == 'Always':
            items += "\n" + start_items[line]['name'] + ', ' + str(2)
    return items


def random_bag(start_items):
    bag = ''
    choices = []
    for line in start_items:
        if start_items[line]['rarity'] != 'Always':
            choices.append(start_items[line])
    for i in range(0, 6):
        item = random.choice(choices)
        bag += "\n" + start_items[line]['name'] + ', ' + str(2)
    return bag


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