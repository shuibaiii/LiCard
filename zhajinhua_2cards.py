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


def judge_win_for_two_card_lists(card_1: CardList, card_2: CardList, matrix):
    x_1, y_1 = judge_relationship_for_two_cards(card_1[0], card_1[1])
    x_2, y_2 = judge_relationship_for_two_cards(card_2[0], card_2[1])
    if matrix[x_1][y_1] > matrix[x_2][y_2]:
        return -1
    elif matrix[x_1][y_1] < matrix[x_2][y_2]:
        return 1
    else:
        return 0


def generate_text_by_result(card_1: CardList, card_2: CardList, result) -> str:
    structure_matrix = ['无重复牌', '弱姊妹牌', '强姊妹牌', '相同牌']
    content_matrix = ['非同系牌', '同系牌']
    relationship_1 = structure_matrix[judge_relationship_for_two_cards(card_1[0], card_1[1])[0]] \
                     + '且' + content_matrix[judge_relationship_for_two_cards(card_1[0], card_1[1])[1]]
    relationship_2 = structure_matrix[judge_relationship_for_two_cards(card_2[0], card_2[1])[0]] \
                     + '且' + content_matrix[judge_relationship_for_two_cards(card_2[0], card_2[1])[1]]
    text_1 = ' '.join(card_1.get_name_list()) + ' ' + relationship_1
    text_2 = ' '.join(card_2.get_name_list()) + ' ' + relationship_2
    if result == 1:
        text = text_1 + ' PK ' + text_2 + ' 胜'
    elif result == -1:
        text = text_1 + ' PK ' + text_2 + ' 负'
    else:
        text = text_1 + ' PK ' + text_2 + ' 平'
    return text


def calc_cards_relationship_prob(test_number, all_name_list, the_number_of_all_name):
    # 计算各种牌型出现的概率
    matrix = np.zeros([4, 2])
    for j in range(test_number):
        name_iter = random.sample(range(0, the_number_of_all_name), 2)
        card_list1 = CardList([all_name_list[name_iter[0]], all_name_list[name_iter[1]]])
        x, y = judge_relationship_for_two_cards(card_list1[0], card_list1[1])
        matrix[x][y] = matrix[x][y] + 1
    pass
    matrix = matrix / tests_number
    print(matrix)
    print(matrix.sum())


def generate_prob_matrix():
    matrix = np.zeros([4, 2])
    matrix[0][0] = 0.789
    matrix[0][1] = 0.044
    matrix[1][0] = 0.054
    matrix[1][1] = 0.050
    matrix[2][1] = 0.048
    matrix[3][1] = 0.015
    # print(matrix.sum())
    return matrix


if __name__ == '__main__':
    # 自动化测试
    settings = Settings()
    all_name_list = settings.get_all_name_list()
    all_name_list = all_name_list + all_name_list
    the_number_of_all_name = len(all_name_list)
    print('牌总数：')
    print(the_number_of_all_name)
    tests_number = 403200
    # calc_cards_relationship_prob(tests_number, all_name_list, the_number_of_all_name)
    prob_matrix = generate_prob_matrix()
    observation_matrix = np.zeros([4, 2])
    win_number = 0
    equal_number = 0
    lose_number = 0
    with open('zhajinhua_2cards_result.txt', 'w', encoding='UTF-8') as f:
        for i in range(tests_number):
            name_iter = random.sample(range(0, the_number_of_all_name), 4)
            card_list1 = CardList([all_name_list[name_iter[0]], all_name_list[name_iter[1]]])
            x, y = judge_relationship_for_two_cards(card_list1[0], card_list1[1])
            observation_matrix[x][y] += 1
            card_list2 = CardList([all_name_list[name_iter[2]], all_name_list[name_iter[3]]])
            x, y = judge_relationship_for_two_cards(card_list2[0], card_list2[1])
            observation_matrix[x][y] += 1
            result = judge_win_for_two_card_lists(card_list1, card_list2, prob_matrix)
            if result == 1:
                win_number += 1
            elif result == 0:
                equal_number += 1
            else:
                lose_number += 1
            text_to_write = str(i + 1) + ': ' + generate_text_by_result(card_list1, card_list2, result)

            print(text_to_write, file=f)

    with open('zhajinhua_2cards_result_analysis.txt', 'w', encoding='UTF-8') as f:
        print('总对局次数： ' + str(tests_number), file=f)
        print('胜局次数为： ' + str(win_number) + ' 比例为：' + str(win_number / tests_number), file=f)
        print('平局次数为： ' + str(equal_number) + ' 比例为：' + str(equal_number / tests_number), file=f)
        print('负局次数为： ' + str(lose_number) + ' 比例为：' + str(lose_number / tests_number), file=f)
        print('', file=f)
        print('总手牌数为：' + str(tests_number * 2), file=f)
        print('相同牌出现次数： ' + str(observation_matrix[3][1]) + ' 比例为：' + str(observation_matrix[3][1] / tests_number / 2), file=f)
        print('强姊妹牌出现次数： ' + str(observation_matrix[2][1]) + ' 比例为：' + str(observation_matrix[2][1] / tests_number / 2), file=f)
        print('弱姊妹牌且非同系牌出现次数： ' + str(observation_matrix[1][0]) + ' 比例为：' + str(observation_matrix[1][0] / tests_number / 2), file=f)
        print('弱姊妹牌且同系牌出现次数： ' + str(observation_matrix[1][1]) + ' 比例为：' + str(observation_matrix[1][1] / tests_number / 2), file=f)
        print('无重复牌且非同系牌出现次数： ' + str(observation_matrix[0][0]) + ' 比例为：' + str(observation_matrix[0][0] / tests_number / 2), file=f)
        print('无重复牌且同系牌出现次数： ' + str(observation_matrix[0][1]) + ' 比例为：' + str(observation_matrix[0][1] / tests_number / 2), file=f)
