TEMPLATE_MONSTER_INFO = "({idx}) {item_name}"
TEMPLATE_MONSTER_MOVE = "({idx}) name: {move} {type}: {base} charges left: {charges}"


def print_indexed_list(item_list, selector):
    print(
        '\n'.join([
            TEMPLATE_MONSTER_INFO.format(idx=idx, item_name=item[selector]) for idx, item in enumerate(item_list)
        ]))


def print_moves(monster_moves, move_type, base_name):
    print(
        '\n'.join([
            TEMPLATE_MONSTER_MOVE.format(idx=idx, move=move['name'], type=move_type, base=move[base_name],
                                         charges=move['charges'])
            for idx, move in enumerate(monster_moves)
        ]))
