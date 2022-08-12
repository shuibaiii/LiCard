from card_list import CardList
from card_relationship_function import get_the_num_of_same_char, \
    judge_win_for_two_cards, judge_relationship_for_two_cards, \
    judge_relationship_in_content_for_two_cards
from settings import Settings
import random
import numpy as np


# 两张牌的炸金花
# 关系一共有五种。首先按照关系高低来结算：
# 相同牌 > 强姊妹牌 > 弱姊妹牌 > 同系牌 > 无关牌
# 其中，相同牌可以用一个函数来判断
# 相同牌里的比较：两张相同王牌 > 两张相同普通牌（针对”白开水*2和笑拉了*2的情况“）；
#              按照所属系列的牌的多少(level)排大小，所属系列牌越多，越小；
#              （可以增加：按字典排序）
# 姊妹牌里的比较：强姊妹牌 > 弱姊妹牌；
#              如果都为强姊妹牌：所属系列牌越少，越大；
#              如果都为弱姊妹牌：同系和同系的比较，所属系列牌越多，越小（参照同系牌）；
#                            同系大于非同系；非同系里：两个系列的牌数量之和越少，越大
# 同系牌里的比较：按照所属系列的牌的多少排大小，所属系列牌越多，越小
# 无关牌里的比较：王牌 + 普通牌 > 两张普通牌；如果都是两张普通牌，结算较大的单张牌的level

# 高级玩法
# 1. 赌博玩法
# 2. 田忌赛马玩法（一次摸六张牌，每次出两张，三局两胜）


def judge_win_for_two_card_lists(card_1: CardList, card_2: CardList):
    same_char_num_1 = get_the_num_of_same_char(card_1[0], card_1[1])
    same_char_num_2 = get_the_num_of_same_char(card_2[0], card_2[1])
    if same_char_num_1 > same_char_num_2:
        return 1
    elif same_char_num_1 < same_char_num_2:
        return -1
    else:
        if judge_relationship_in_content_for_two_cards(card_1[0], card_1[1]) and \
                not judge_relationship_in_content_for_two_cards(card_2[0], card_2[1]):
            return 1
        elif not judge_relationship_in_content_for_two_cards(card_1[0], card_1[1]) and \
                judge_relationship_in_content_for_two_cards(card_2[0], card_2[1]):
            return -1
        else:
            return judge_win_for_two_cards(card_1.get_max_card(), card_2.get_max_card())


def generate_text_by_result(card_1: CardList, card_2: CardList, relationship_1, relationship_2, result) -> str:
    text_1 = ' '.join(card_1.get_name_list()) + ' ' + relationship_1
    text_2 = ' '.join(card_2.get_name_list()) + ' ' + relationship_2
    if result == 1:
        text = text_1 + ' PK ' + text_2 + ' 胜'
    elif result == -1:
        text = text_1 + ' PK ' + text_2 + ' 负'
    else:
        text = text_1 + ' PK ' + text_2 + ' 平'
    return text


# def calc_relationship(relationship, same_number, strong_number, weak_number, family_number, independent_number):
#     if relationship == '相同牌':
#         same_number += 1
#     elif relationship == '强姊妹牌':
#         strong_number += 1
#     elif relationship == '弱姊妹牌':
#         weak_number += 1
#     elif relationship == '同系牌':
#         family_number += 1
#     else:
#         independent_number += 1
#
#
# def calc_result(result, win_number, lose_number, equal_number):
#     if result == 1:
#         win_number += 1
#     elif result == 0:
#         equal_number += 1
#     else:
#         lose_number += 1


if __name__ == '__main__':
    # 自动化测试
    settings = Settings()
    all_name_list = settings.get_all_name_list()
    all_name_list = all_name_list + all_name_list
    the_number_of_all_name = len(all_name_list)
    print(the_number_of_all_name)
    tests_number = 10240000
    same_number = 0
    strong_number = 0
    weak_number = 0
    family_number = 0
    independent_number = 0
    win_number = 0
    lose_number = 0
    equal_number = 0
    # 先测试各种牌型出现的概率
    matrix = np.zeros([4, 2])
    for j in range(tests_number):
        name_iter = random.sample(range(0, the_number_of_all_name), 2)
        card_list1 = CardList([all_name_list[name_iter[0]], all_name_list[name_iter[1]]])
        x, y = judge_relationship_for_two_cards(card_list1[0], card_list1[1])
        matrix[x][y] = matrix[x][y] + 1
    pass
    matrix = matrix / tests_number
    print(matrix)
    print(matrix.sum())

    # all_name_list[random.randint(0, the_number_of_all_name - 1)
    # with open('zhajinhua_2cards_result.txt', 'w', encoding='UTF-8') as f:
    #     for i in range(tests_number):
    #         # random.randint(1, 10) # 产生[1, 10]的整数随机数
    #         name_list_1 = [all_name_list[random.randint(0, the_number_of_all_name-1)],
    #                        all_name_list[random.randint(0, the_number_of_all_name-1)]]
    #         name_list_2 = [all_name_list[random.randint(0, the_number_of_all_name-1)],
    #                        all_name_list[random.randint(0, the_number_of_all_name-1)]]
    #         card_list_1 = CardList(name_list_1)
    #         card_list_2 = CardList(name_list_2)
    #         relationship_1 = judge_relationship_for_two_cards(card_list_1[0], card_list_1[1])
    #         if relationship_1 == '相同牌':
    #             same_number += 1
    #         elif relationship_1 == '强姊妹牌':
    #             strong_number += 1
    #         elif relationship_1 == '弱姊妹牌':
    #             weak_number += 1
    #         elif relationship_1 == '同系牌':
    #             family_number += 1
    #         else:
    #             independent_number += 1
    #         relationship_2 = judge_relationship_for_two_cards(card_list_2[0], card_list_2[1])
    #         if relationship_2 == '相同牌':
    #             same_number += 1
    #         elif relationship_2 == '强姊妹牌':
    #             strong_number += 1
    #         elif relationship_2 == '弱姊妹牌':
    #             weak_number += 1
    #         elif relationship_2 == '同系牌':
    #             family_number += 1
    #         else:
    #             independent_number += 1
    #         result = judge_win_for_two_card_lists(card_list_1, card_list_2)
    #         if result == 1:
    #             win_number += 1
    #         elif result == 0:
    #             equal_number += 1
    #         else:
    #             lose_number += 1
    #         text_to_write = str(i+1) + ': ' + generate_text_by_result(card_list_1, card_list_2, relationship_1,
    #                                                                   relationship_2, result)
    #
    #         print(text_to_write, file=f)
    #
    # with open('zhajinhua_2cards_result_analysis.txt', 'w', encoding='UTF-8') as f:
    #     print('总对局次数： ' + str(tests_number), file=f)
    #     print('胜局次数为： ' + str(win_number) + ' 比例为：' + str(win_number / tests_number), file=f)
    #     print('平局次数为： ' + str(equal_number) + ' 比例为：' + str(equal_number / tests_number), file=f)
    #     print('负局次数为： ' + str(lose_number) + ' 比例为：' + str(lose_number / tests_number), file=f)
    #     print('', file=f)
    #     print('总手牌数为：' + str(tests_number*2), file=f)
    #     print('相同牌出现次数： ' + str(same_number) + ' 比例为：' + str(same_number / tests_number / 2), file=f)
    #     print('强姊妹牌出现次数： ' + str(strong_number) + ' 比例为：' + str(strong_number / tests_number / 2), file=f)
    #     print('弱姊妹牌出现次数： ' + str(weak_number) + ' 比例为：' + str(weak_number / tests_number / 2), file=f)
    #     print('同系牌出现次数： ' + str(family_number) + ' 比例为：' + str(family_number / tests_number / 2), file=f)
    #     print('无关牌出现次数： ' + str(independent_number) + ' 比例为：' + str(independent_number / tests_number / 2), file=f)