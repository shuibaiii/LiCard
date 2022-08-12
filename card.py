from settings import Settings


class Card:
    # 单张牌
    def __init__(self, name):
        settings = Settings()
        self.name = name  # 牌的名字 比如“好的捏”
        self.family_number = settings.get_family_number_by_name(name)  # 牌的系列 比如2号系列中包含：好家伙，活久见，麻掉了，麻死了，震大惊，离大谱
        self.level = settings.get_level_by_name(name)  # 牌的等级 牌的等级与牌所属系列的总牌数成倒数关系
        self.is_trump = settings.get_is_trump_by_name(name)  # 牌的属性 分为王牌和普通牌 例子：is_normal = False，表示是王牌

    def __eq__(self, other):
        # 重载==运算符，判断两张牌是否是相同牌
        return self.name == other.name

    def __gt__(self, other):
        # 重载 > 运算符，判断两张牌的大小。可使用：self > other
        if self.is_trump and (not other.is_trump):
            return True
        elif (not self.is_trump) and other.is_trump:
            return False
        elif self.is_trump and other.is_trump:
            # 如果两张牌都是王牌
            return True
        else:
            # 如果两张牌都是普通牌，判断level大小
            return self.level > other.level

    def __lt__(self, other):
        # 重载 < 运算符，判断两张牌的大小。可使用：self < other
        if self.is_trump and (not other.is_trump):
            return False
        elif (not self.is_trump) and other.is_trump:
            return True
        elif self.is_trump and other.is_trump:
            # 如果两张牌都是王牌
            return False
        else:
            # 如果两张牌都是普通牌，判断level大小
            return self.level < other.level

    def __str__(self):
        # 重载print运算符
        return self.name


if __name__ == '__main__':
    name_1 = '臭宝贝'
    name_2 = '好的嘞'
    name_3 = '好的鸭'
    card_1 = Card(name_1)
    card_2 = Card(name_2)
    card_3 = Card(name_3)
    print(card_1)
    print(card_1 > card_2)
    print(card_2 < card_3)
    print(card_1 == card_2)

    pass