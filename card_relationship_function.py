from card import Card


def judge_win_for_two_cards(card_1: Card, card_2: Card):
    if card_1.is_trump and card_2.is_trump:
        return 0
    elif card_1.is_trump and not card_2.is_trump:
        return 1
    elif not card_1.is_trump and card_2.is_trump:
        return -1
    else:
        if card_1.level > card_2.level:
            return 1
        elif card_1.level < card_2.level:
            return -1
        else:
            return 0


def judge_relationship_for_two_cards(card_1: Card, card_2: Card):
    same_char_num = get_the_num_of_same_char(card_1, card_2)
    if same_char_num == 3:
        return '相同牌'
    elif same_char_num == 2:
        return '强姊妹牌'
    elif same_char_num == 1:
        return '弱姊妹牌'
    else:
        if check_if_same_family(card_1, card_2):
            return '同系牌'
        else:
            return '无关牌'


def check_if_same_family(card_1: Card, card_2: Card):
    # 检查两张牌是否是同系牌
    if card_1.family_number == card_2.family_number:
        return True
    else:
        return False


def check_if_strong_sister(card_1: Card, card_2: Card):
    # 检查两张牌是否是强姊妹牌
    name_1_set = set(card_1.name)
    name_2_set = set(card_2.name)
    if len(name_1_set & name_2_set) == 2:  # 名字中有两个相同的字
        return True
    else:
        return False


def check_if_weak_sister(card_1: Card, card_2: Card):
    # 检查两张牌是否是弱姊妹牌
    name_1_set = set(card_1.name)
    name_2_set = set(card_2.name)
    if len(name_1_set & name_2_set) == 1:  # 名字中有一个相同的字
        return True
    else:
        return False


def get_the_num_of_same_char(card_1: Card, card_2: Card):
    # 返回两张牌的相同字的数量
    name_1_set = set(card_1.name)
    name_2_set = set(card_2.name)
    return len(name_1_set & name_2_set)