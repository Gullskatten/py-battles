#! /usr/bin/env bash

import random
from random import randrange

from util.prints import print_indexed_list


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
        'Pick a number (0-{monsters_length}) to select a monster: '.format(monsters_length=len(monsters)-1)
    )
    try:
        selected_monster_idx = int(selected_monster_input)
        selected_monster = monsters.pop(selected_monster_idx)
        selected_level = int(input('Select your monsters level: '))
        selected_monster['level'] = selected_level
        set_health(selected_monster)
        return selected_monster
    except ValueError:
        print("Woops! Couldn't find that a monster with that number.")
        select_monster(monsters)


def set_random_level(monster, user_selected_monster):
    monster['level'] = random.randint(user_selected_monster['level'] - 5, user_selected_monster['level'] + 5)
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
