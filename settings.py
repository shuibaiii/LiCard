class Settings:
    def __init__(self):
        self.name_list_1 = ['好的嘞', '好的捏', '好的鸭', '是的嘞', '是的捏', '是的鸭', '对的嘞', '对的捏', '对的鸭']
        self.name_list_2 = ['好家伙', '活久见', '麻掉了', '麻死了', '震大惊', '离大谱']
        self.name_list_3 = ['臭臭宝', '臭宝贝', '讨厌啵', '你快爬', '讨厌宝']
        self.name_list_4 = ['可以嗷', '确实嗷', '可以捏', '确实捏']
        self.name_list_5 = ['好滴叭', '没有叭', '没有鸭']
        self.name_list_6 = ['笑拉了', '我笑死']
        self.name_list_7 = ['咋了捏']
        self.name_list_8 = ['真牛蛙']
        self.name_list_9 = ['白开水']  # 王牌

    def get_the_number_of_name_list(self):
        return len(vars(self))

    def get_all_name_list(self):
        name_list = []
        for value in vars(self).values():
            name_list = name_list + value
        return name_list

    def get_family_number_by_name(self, name):
        name_dict = vars(self)
        family_number = 0
        for key, value in name_dict.items():
            if name in value:
                family_number = key[-1]
                break
        return family_number

    def get_family_list_by_name(self, name):
        name_dict = vars(self)
        family_list = []
        for value in name_dict.values():
            if name in value:
                family_list = family_list + value
                break
        return family_list

    def get_level_by_name(self, name):
        family_list = self.get_family_list_by_name(name)
        return 1/len(family_list)

    def get_is_trump_by_name(self, name):
        if name in self.name_list_9:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Settings()
    print(getattr(a, 'name_list_1'))
    print(vars(a))
    print(a.get_family_number_by_name('咋了捏'))
    print(a.get_family_number_by_name('啊呜呜'))
    print(a.get_all_name_list())
    print(a.get_the_number_of_name_list())