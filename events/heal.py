#!  /usr/bin/env bash

import random
import math

HEAL_CRITICAL_TEMPLATE = "{healer}'s {heal_name} healed for {amount_healing}!"
HEAL_NORMAL_TEMPLATE = "{healer}'s {heal_name} healed for {amount_healing}."
HEAL_FULL_TEMPLATE = "{healer} is now at full health."
ALREADY_FULL_TEMPLATE = "{healer} is already at full health."


def heal(healer, base_modifier, heal_name):
    max_health = healer['max_health']
    current_health = healer['health']

    if current_health == max_health:
        return 0, ALREADY_FULL_TEMPLATE.format(healer=healer['name'])

    random_roll = random.randint(1, 100)
    base_matrix = random_roll * base_modifier

    if random_roll > 85:
        healing_done = determine_healing_done(healer, base_matrix, 1.3)

        if healing_done + current_health >= max_health:
            return max_health - current_health, HEAL_FULL_TEMPLATE.format(healer=healer['name'])

        return healing_done, HEAL_CRITICAL_TEMPLATE.format(
            healer=healer['name'],
            heal_name=heal_name,
            amount_healing=healing_done)

    else:
        healing_done = determine_healing_done(healer, base_matrix, 1)

        if healing_done + current_health >= max_health:
            return max_health - current_health, HEAL_FULL_TEMPLATE.format(healer=healer['name'])

        return healing_done, HEAL_NORMAL_TEMPLATE.format(
            healer=healer['name'],
            heal_name=heal_name,
            amount_healing=healing_done)


def determine_healing_done(healer, base_matrix, critical_modifier):
    return math.ceil((healer['intellect'] * healer['level']) * (base_matrix / 100) * critical_modifier)

