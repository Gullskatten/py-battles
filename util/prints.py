TEMPLATE_MONSTER_INFO = "({idx}) {item_name}"


def print_indexed_list(item_list, selector):
    print(
        '\n'.join([
            TEMPLATE_MONSTER_INFO.format(idx=idx, item_name=item[selector]) for idx, item in enumerate(item_list)
        ]))
