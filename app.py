#! /usr/bin/env bash
import json

from battle.battle import get_random_monster, determine_initial_turn, select_monster

INITIAL_WELCOME_TEXT = "\t\t\tWelcome to Monster Battle!"
TEMPLATE_BATTLE_VS = "\t{first_opponent} (lvl {first_opponent_level})\t" \
                     " vs \t{second_opponent} (lvl {second_opponent_level})"

TEMPLATE_OPPONENT_STARTS = "{opponent} starts!"
DELIMITER = "\n_______________________________________________________\n"

TEMPLATE_REMAINING_HEALTH = "\t{opponent} (HP {opponent_health}/{opponent_max_health})"

if __name__ == '__main__':
    with open('./data/monsters.json', 'r') as f:
        all_monsters = json.load(f)
    print()
    print(INITIAL_WELCOME_TEXT)

    first_opponent = select_monster(all_monsters)
    second_opponent = get_random_monster(all_monsters, first_opponent)

    print(DELIMITER)
    print(TEMPLATE_BATTLE_VS.format(
        first_opponent=first_opponent['name'],
        second_opponent=second_opponent['name'],
        first_opponent_level=first_opponent['level'],
        second_opponent_level=second_opponent['level']
    ))
    print(DELIMITER)
    turn_counter = determine_initial_turn(first_opponent, second_opponent)

    print(TEMPLATE_REMAINING_HEALTH.format(
        opponent=first_opponent['name'],
        opponent_health=first_opponent['health'],
        opponent_max_health=first_opponent['max_health']))

    print(TEMPLATE_REMAINING_HEALTH.format(
        opponent=second_opponent['name'],
        opponent_health=second_opponent['health'],
        opponent_max_health=second_opponent['max_health'])
    )

    print(TEMPLATE_OPPONENT_STARTS.format(opponent=first_opponent['name'])) if turn_counter == 1 else print(
        TEMPLATE_OPPONENT_STARTS.format(opponent=second_opponent['name']))

