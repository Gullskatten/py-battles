#! /usr/bin/env bash
import json

from battle.battle import get_random_monster, determine_initial_turn, select_monster, select_move
from events.attacks import attack
from events.heal import heal
from util.prints import print_indexed_list

INITIAL_WELCOME_TEXT = "\t\t\tWelcome to Monster Battle!"
TEMPLATE_BATTLE_VS = "\t{first_opponent} (lvl {first_opponent_level})\t" \
                     " vs \t{second_opponent} (lvl {second_opponent_level})"

TEMPLATE_OPPONENT_STARTS = "\n {opponent} starts!"
DELIMITER = "\n_______________________________________________________\n"

TEMPLATE_REMAINING_HEALTH = " {opponent} (HP {opponent_health}/{opponent_max_health}) \t"
ABILITY_ACTION_TEMPLATE = "\n {action} \n"

if __name__ == '__main__':
    with open('./data/monsters.json', 'r') as f:
        all_monsters = json.load(f)
    print()
    print(INITIAL_WELCOME_TEXT)
    print(DELIMITER)
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

    while first_opponent['health'] > 0 and second_opponent['health'] > 0:

        print(TEMPLATE_REMAINING_HEALTH.format(
            opponent=second_opponent['name'],
            opponent_health=second_opponent['health'],
            opponent_max_health=second_opponent['max_health'])
              + TEMPLATE_REMAINING_HEALTH.format(
            opponent=first_opponent['name'],
            opponent_health=first_opponent['health'],
            opponent_max_health=first_opponent['max_health'])
              )
        if turn_counter == 0:
            print('\n Opponents turn. \n')

            first_opponent['health'] = first_opponent['health'] - 100
            turn_counter = 1

        else:
            print('\n Your turn. \n')

            selected_move_tuple = select_move(first_opponent)

            if selected_move_tuple[1] == 'heal':
                healing_done = heal(first_opponent,
                                    selected_move_tuple[0]['base_healing'],
                                    selected_move_tuple[0]['name'])
                first_opponent['health'] = first_opponent['health'] + healing_done[0]
                print(ABILITY_ACTION_TEMPLATE.format(action=healing_done[1]))

            elif selected_move_tuple[1] == 'attack':
                damage_done = attack(
                    first_opponent,
                    second_opponent,
                    selected_move_tuple[0]['base_damage'],
                    selected_move_tuple[0]['name'])
                second_opponent['health'] = second_opponent['health'] - damage_done[0]
                print(ABILITY_ACTION_TEMPLATE.format(action=damage_done[1]))

            turn_counter = 0

    if first_opponent['health'] > 0:
        print('You won!')
    else:
        print('Oh no, you lost!')
