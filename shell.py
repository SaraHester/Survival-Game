import core, disk, random, time, sys


def input_choice(number, string):
    while True:
        choice = input(string).strip()
        if choice.lower() == 'q':
            print("\n\t\t\t\tExiting...")
            # time.sleep(2)
            sys.exit()
        for i in range(1, number):
            if choice == str(i):
                return choice
        else:
            print(
                '\t\t\t----------------',
                '\n\t\t\t!Invalid Input!\n',
                '\t\t\t----------------',
                sep='')


def checker(string):
    choice = input_choice(
        3, "\n\t\tAre you sure you want to {}?\n\t\t1.Yes\n\t\t2.No\n\t\t\t->".
        format(string))
    if choice == '1':
        return True
    elif choice == '2':
        return False
    else:
        return None


def pretty_found(found_items):
    print("\n\t\tItems that can be FOUND")
    for item in found_items:
        print(found_items[item]['name'], ", Health effect:",
              found_items[item]['effect'], ", \n\tFound:",
              found_items[item]['found'], ", Rarity:",
              found_items[item]['rarity'], ", Extra: ",
              found_items[item]['extra'])


def pretty_start(start_items):
    print("\n\t\tItems that can be aquired at START")
    for item in start_items:
        print(start_items[item]['name'], ", Health effect:",
              start_items[item]['effect'], ", Rarity:",
              start_items[item]['rarity'], ", \n\t\tExtra: ",
              start_items[item]['extra'])


def pretty_crafting(crafting_items):
    print("-" * 26)
    for item in crafting_items:
        print(
            "\n\t\t",
            crafting_items[item]['number'],
            ". ",
            crafting_items[item]['name'],
            '\trequires - ',
            sep='',
            end='')
        for i in range(0, len(crafting_items[item]['requirements'])):
            print(crafting_items[item]['requirements'][i], end='')
    print("-" * 26)


def scavage(player, found_items, inventory):
    if player['energy'] > 20 and checker("scavage"):
        found = core.scavage(player, found_items)
        disk.append_inventory(core.convert_item_to_str(found), player['name'])
        player['energy'] -= 20
        inventory.append(found)
        print("\t\t\tYou have found", found['name'])
        print("\n\t\tYour energy is now:", player['energy'])
    else:
        print("\n\t\t\tYou dont have enough energy to do this\n")


def craft(inventory, crafting_items, player):
    leave = ''
    while leave != '2':
        print("\n\t\t\tCraft Menu. ")
        if len(inventory) == 0:
            print("\n\t\t\tINVENTORY EMPTY\n\n")
        else:
            pretty_crafting(crafting_items)
            choice = input_choice(
                len(crafting_items) + 1,
                "\n\t\tWhat do you want to craft?\n\t\t\t->")
            if choice != 'q' and choice.isdigit():
                print('\t\tRequirements : ')
                for i in range(
                        0, len(crafting_items[int(choice)]['requirements'])):
                    print("\t\t" +
                          crafting_items[int(choice)]['requirements'][i])
                if checker("craft this") and choice in inventory:
                    print(inventory)
            leave = input_choice(
                3, "\n\t\t1.Keep Crafting\n\t\t2.Go back\n\t\t\t->")
            print("\n\t\t\t\tHaven't got this far")
    return player


def print_inventory(inventory):
    # for item in inventory:
    print(inventory)
    print("\n")


def choose_start_package(start_items, inventory, player):
    if len(inventory) == 0:
        number = input_choice(
            4,
            '\n\t\tWhat bag would you like to start with?\n\t\t1, 2, or 3\n\t\t\t->'
        )
        disk.append_inventory(core.always_items(start_items), player['name'])
        bag = core.random_bag(core.convert_inventory_to_str(start_items))
        disk.append_inventory(bag, player['name'])
        print("\n\t\tBag", number, "Chosen\n\nYou have acquired", bag)
    else:
        return None


def returning_player():
    player = {'health': 100, 'energy': 100}
    player['name'] = input("\n\t\tWhat is your username?\n\t\t\t->")
    play(player)


def play(player):
    found_items = disk.open_found_items()
    start_items = disk.open_start_items()
    crafting_items = disk.open_crafting_items()
    inventory = disk.open_inventory(player['name'])
    choose_start_package(start_items, inventory, player)
    count = 0
    start = ''
    while core.not_dead(player):
        inventory = disk.open_inventory(player['name'])
        count += 1
        start = input_choice(
            6, "\n\n\t\t" + "-" * 25 +
            "\n\t\tWhat are you going to do?\n\t\t1.Rest\n\t\t2.Scavage\n\t\t3.Craft\n\t\t4.Look at inventory\n\t\t5.Clear game\n\t\tq.quit"
            + "\n\t\t" + "-" * 25 + "\n\t\t\t->")
        if start == '1':
            core.rest(player)
            print("\t\t\tEnergy restored")
            count += 1
        elif start == '2':
            scavage(player, found_items, inventory)
        elif start == '3':
            craft(inventory, crafting_items, player)
        elif start == '4':
            print_inventory(inventory)
        elif start == '5':
            if checker("clear the inventory. THIS WILL RESET THE GAME"):
                disk.make_new_file(player['name'])
                print("\t\t\tExiting...")
                # time.sleep(2)
                sys.exit()
        core.time_effect(count, player)
        print("\t\tHealth: ", player['health'])
        print("\t\tEnergy:", player['energy'])
    print("\n\n")
    if player['energy'] == 0:
        print('\t\t\tEnergy is at 0. You are Dead.')
    if player['health'] == 0:
        print("\t\t\tHealth is at 0. You are Dead.")


def new_player():
    player = {'health': 100, 'energy': 100}
    player['name'] = input("\t\tEnter your username\n\t\t\t->")
    disk.make_new_file(player['name'])
    play(player)


# possible items = map, compass, flashlight, duct tape
def main():
    new_or_returning = input_choice(
        3, "\t\tAre you\n\t\t1.New Player\n\t\t2.Returning Player\n\t\t\t->")
    if new_or_returning == '2':
        returning_player()
    elif new_or_returning == '1':
        new_player()


if __name__ == '__main__':
    main()