#!  /usr/bin/env bash

import random
import math

__heal_critical_template = "{healer}'s {heal_name} healed for {amount_healing}!"
__heal_normal_template = "{healer}'s {heal_name} healed for {amount_healing}."


def heal(healer, base_modifier, heal_name):
    random_roll = random.randint(1, 100)
    base_matrix = random_roll * base_modifier

    if random_roll > 85:
        healing_done = determine_healing_done(healer, base_matrix, 1.3)

        return healing_done, __heal_critical_template.format(
            healer=healer['name'],
            heal_name=heal_name,
            amount_healing=healing_done)

    else:
        healing_done = determine_healing_done(healer, base_matrix, 1)

        return healing_done, __heal_normal_template.format(
            healer=healer['name'],
            heal_name=heal_name,
            amount_healing=healing_done)


def determine_healing_done(healer, base_matrix, critical_modifier):
    return math.ceil((healer['intellect'] * healer['level']) * (base_matrix / 100) * critical_modifier)

