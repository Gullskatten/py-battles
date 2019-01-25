#! /usr/bin/env bash

import json
import random
from random import randrange


def get_random_monster(monsters):
    random_index = randrange(len(monsters))
    return monsters.pop(random_index)


def set_random_level(opponent):
    opponent['level'] = random.randint(1, 100)


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


with open('../data/monsters.json', 'r') as f:
    all_monsters = json.load(f)

opponent1 = get_random_monster(all_monsters)
set_random_level(opponent1)
opponent2 = get_random_monster(all_monsters)
set_random_level(opponent2)

print(opponent1)
print(opponent2)
print(get_next_attack(opponent1))
print(get_next_attack(opponent2))





