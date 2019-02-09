#! /usr/bin/env bash

import random
from random import randrange

from util.prints import print_indexed_list, print_moves


def get_random_monster(monsters, first_opponent):
    random_index = randrange(len(monsters))
    monster = monsters.pop(random_index)
    set_random_level(monster, first_opponent)
    set_health(monster)
    return monster


def select_monster(monsters):
    print_indexed_list(monsters, 'name')

    # TODO: Perform input validation on monster!
    selected_monster_input = input(
        '\n Pick a number (0-{monsters_length}) to select a monster: '.format(monsters_length=len(monsters)-1)
    )
    try:
        selected_monster_idx = int(selected_monster_input)
        if selected_monster_idx > len(monsters) or selected_monster_idx < 0:
            print("\n Woops! Couldn't find a monster with that number. \n")
            select_monster(monsters)
        selected_level = int(input('\n Select your monsters level (1+): '))
        if selected_level <= 0:
            selected_level = 1
        selected_monster = monsters.pop(selected_monster_idx)
        selected_monster['level'] = selected_level
        set_health(selected_monster)
        return selected_monster
    except ValueError:
        print("\n Woops! That wasn't expected. \n")
        select_monster(monsters)


def select_move(monster):
    attack_type_selected = 1
    if len(monster['healing_moves']):
        print('(0) Heal')
        print('(1) Attack opponent')
        try:
            attack_type_selected = int(input('\n Choose an action: '))
        except ValueError:
            print("\n That move option wasn't found (expected 0 or 1). \n")
            return select_move(monster)

    if attack_type_selected == 1:
        print_moves(monster['attack_moves'], 'damage', 'base_damage')
        print('\n')
    elif attack_type_selected == 0:
        print_moves(monster['healing_moves'], 'healing', 'base_healing')
        print('\n')
    else:
        print("\n That move option wasn't found (expected 0 or 1). \n")
        return select_move(monster)

    try:
        selected_idx = int(input('\n Choose an ability: '))
        if attack_type_selected == 1:
            if selected_idx > len(monster['attack_moves'])-1 or selected_idx < 0:
                print("\n That attack was not found. \n")
                return select_move(monster)
            else:
                selected_move = monster['attack_moves'][selected_idx]
                if selected_move['charges'] > 0:
                    monster['attack_moves'][selected_idx]['charges'] = selected_move['charges'] - 1
                    return selected_move, 'attack'
                else:
                    print("\n That move has no charges left! \n")
                    return select_move(monster)
        elif attack_type_selected == 0:
            if selected_idx > len(monster['healing_moves'])-1 or selected_idx < 0:
                print("\n That healing ability was not found. \n")
                return select_move(monster)
            else:
                selected_move = monster['healing_moves'][selected_idx]
                if selected_move['charges'] > 0:
                    monster['healing_moves'][selected_idx]['charges'] = selected_move['charges'] - 1
                    return selected_move, 'heal'
                else:
                    print("\n That move has no charges left! \n")
                    return select_move(monster)
    except ValueError:
        print("\n Dude, that's not an option! \n")
        return select_move(monster)


def set_random_level(monster, user_selected_monster):
    min_level = user_selected_monster['level'] - 5 if user_selected_monster['level'] > 5 else 1
    monster['level'] = random.randint(min_level, user_selected_monster['level'] + 5)
    return monster


def set_health(monster):
    full_health = (monster['stamina'] * 2) * monster['level']
    monster['health'] = full_health
    monster['max_health'] = full_health
    return monster


def get_next_attack(monster):
    all_attacks = monster['attack_moves']
    attacks_with_charges = [x for x in all_attacks if x['charges'] > 0]

    if not attacks_with_charges:
        return None

    return random.choice(attacks_with_charges)


def get_next_healing(monster):
    all_healings = monster['healing_moves']

    if not all_healings:
        return None

    healing_with_charges = [x for x in all_healings if x['charges'] > 0]

    if not healing_with_charges:
        return None

    return random.choice(healing_with_charges)


def determine_initial_turn(first_opponent, second_opponent):
    first_opponent_speed = first_opponent['speed'] * first_opponent['level']
    second_opponent_speed = second_opponent['speed'] * second_opponent['level']
    return 1 if first_opponent_speed > second_opponent_speed else 2
