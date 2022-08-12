from card_relationship_function import *


class CardList:
    # 手牌/被淹没的牌
    def __init__(self, name_list):
        self.card_list = []
        for name in name_list:
            this_card = Card(name)
            self.card_list.append(this_card)
        self.the_number_of_cards = len(self.card_list)

    def delete_card(self, card):
        if card in self.card_list:
            self.card_list.remove(card)
            self.the_number_of_cards = len(self.card_list)
            return True
        else:
            return False

    def append_card(self, card: Card):
        self.card_list.append(card)
        self.the_number_of_cards = len(self.card_list)

    def get_max_card(self):
        return sorted(self.card_list)[-1]

    def get_min_card(self):
        return sorted(self.card_list)[0]

    def get_name_list(self):
        name_list = []
        for card in self.card_list:
            name_list.append(card.name)
        return name_list

    def get_trump_number(self):
        number = 0
        for card in self.card_list:
            if card.is_trump:
                number = number + 1
        return number

    def __str__(self):
        # 重载print运算符
        name_string = ''
        for card in self.card_list:
            name_string = name_string + ' ' + card.name
        return name_string[1:]

    def __getitem__(self, index: int):
        if index < self.the_number_of_cards:
            return self.card_list[index]
        else:
            return None


if __name__ == '__main__':
    name_list = ['好家伙', '确实嗷', '真牛蛙', '白开水']
    card_list = CardList(name_list)
    max_card = card_list.get_max_card()
    print(max_card)
    card_1 = Card('离大谱')
    card_2 = Card('离大谱')
    print(get_the_num_of_same_char(card_1, card_2))
    print(judge_win_for_two_cards(card_list[0], card_list[1]))
    print(judge_win_for_two_cards(card_list[-1], card_list[1]))