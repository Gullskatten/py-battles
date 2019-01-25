#!  /usr/bin/env bash

import random
import math

ATTACK_MISSED_TEMPLATE = "Oh, no! {attacker}'s {attack_name} missed!"
ATTACK_CRITICAL_TEMPLATE = "{attacker}'s {attack_name} hit {target} for {amount_damage}! A critical hit!"
ATTACK_NORMAL_TEMPLATE = "{attacker}'s {attack_name} hit {target} for {amount_damage}."


def attack(attacker, target, base_modifier, attack_name):
    random_roll = random.randint(0, 100)
    base_matrix = 0 if random_roll < 10 else random_roll * base_modifier

    if base_matrix == 0:
        return 0, ATTACK_MISSED_TEMPLATE.format(attacker=attacker['name'], attack_name=attack_name)

    elif random_roll > 85:
        damage_done = _determine_damage_done(attacker, base_matrix, 1.5)

        return damage_done, ATTACK_CRITICAL_TEMPLATE.format(
            attacker=attacker['name'],
            attack_name=attack_name,
            target=target['name'],
            amount_damage=damage_done)

    else:
        damage_done = _determine_damage_done(attacker, base_matrix, 1)

        return damage_done, ATTACK_NORMAL_TEMPLATE.format(
            attacker=attacker['name'],
            attack_name=attack_name,
            target=target['name'],
            amount_damage=damage_done)


def _determine_damage_done(attacker, base_matrix, critical_modifier):
    return math.ceil((attacker['strength'] * attacker['level']) * (base_matrix / 85) * critical_modifier)


