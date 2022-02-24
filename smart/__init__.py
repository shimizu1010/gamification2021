#問題文の表示は直すひつようがある。
from otree.api import *
c = cu

doc = ''

class Constants(BaseConstants):
    name_in_url = ''
    players_per_group = 500
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    number = models.IntegerField(initial=0)
    score = models.IntegerField()

    total_universe = models.IntegerField()
    total_universe_0 = models.IntegerField()
    total_meta_universe = models.IntegerField()
    universe_text = models.StringField()
    universe_point = models.IntegerField()


    total_color = models.IntegerField()
    total_color_0 = models.IntegerField()
    total_meta_color = models.IntegerField()
    color_text = models.StringField()
    color_point = models.IntegerField()


    total_conspiracy_theory = models.IntegerField()
    total_conspiracy_theory_0 = models.IntegerField()
    total_meta_conspiracy_theory = models.IntegerField()
    conspiracy_theory_text = models.StringField()
    conspiracy_theory_point = models.IntegerField()


    total_intelligence = models.IntegerField()
    total_intelligence_0 = models.IntegerField()
    total_meta_intelligence = models.IntegerField()
    intelligence_text = models.StringField()
    intelligence_point = models.IntegerField()


    total_dress = models.IntegerField()
    total_dress_0 = models.IntegerField()
    total_meta_dress = models.IntegerField()
    dress_text = models.StringField()
    dress_point = models.IntegerField()


    total_shoes = models.IntegerField()
    total_shoes_0 = models.IntegerField()
    total_meta_shoes = models.IntegerField()
    shoes_text = models.StringField()
    shoes_point = models.IntegerField()


    total_fakenews = models.IntegerField()
    total_fakenews_0 = models.IntegerField()
    total_meta_fakenews = models.IntegerField()
    fakenews_text = models.StringField()
    fakenews_point = models.IntegerField()


    total_tour = models.IntegerField()
    total_tour_0 = models.IntegerField()
    total_meta_tour = models.IntegerField()
    tour_text = models.StringField()
    fakenews_point = models.IntegerField()


    total_vaccine = models.IntegerField()
    total_vaccine_0 = models.IntegerField()
    total_meta_vaccine = models.IntegerField()
    vaccine_text = models.StringField()
    vaccine_point = models.IntegerField()



    #playerオブジェクトから質問の得点を取ってきて、合計を格納
    def compute(self):
        def cal(number, answer, meta_answer, total):
            if meta_answer[number - 1] == 0:
                if answer[number - 1] == 0:
                    if total / number <= 0.5:
                        point = 1, 
                        text = "正解！ 多数派があなたと同じように考えています"
                    else:
                        point = 0
                        text = "不正解！ 多数派はあなたと同じように考えていません"
                elif answer[number - 1] == 1:
                    if total / number >= 0.5:
                        point = 1
                        text = "正解！ 多数派があなたと同じように考えています"
                    else:
                        point = 0
                        text = "不正解！ 多数派はあなたと同じように考えていません"
            elif meta_answer[number - 1] == 1:
                if answer[number - 1] == 0:
                    if total / number >= 0.5:
                        point = 1
                        text = "正解！ 少数派があなたと同じように考えています"
                    else:
                        point = 0
                        text = "不正解！ 少数派はあなたと同じように考えていません"
                elif answer[number - 1] == 1:
                    if total / number <= 0.5:
                        point = 1
                        text = "正解！ 少数派があなたと同じように考えています"
                    else:
                        point = 0
                        text = "不正解！ 少数派はあなたと同じように考えていません"
            return text
        
        universes = [p.universe for p in self.get_players()]
        self.total_universe = sum(universes)
        self.total_universe_0 = self.number - self.total_universe
        meta_universes = [p.meta_universe for p in self.get_players()]
        #self.total_meta_universe = sum(meta_universes)
        self.universe_text = cal(self.number, universes, meta_universes, self.total_universe)


        colors = [p.color for p in self.get_players()]
        self.total_color = sum(colors)
        self.total_color_0 = self.number - self.total_color
        meta_colors = [p.meta_color for p in self.get_players()]
        self.color_text = cal(self.number, colors, meta_colors, self.total_color)



        """if meta_universes[self.number - 1] == 0:
            print("多数派と答えている")
            if universes[self.number - 1] == 0:
                print("はいと答えている")
                if self.total_universe / self.number <= 0.5:
                    self.universe_point = 1
                    self.universe_text = "正解！ 多数派があなたと同じように考えています"
                else:
                    self.universe_point = 0
                    self.universe_text = "不正解！ 多数派はあなたと同じように考えていません"
            elif universes[self.number - 1] == 1:
                print("いいえと答えている")
                if self.total_universe / self.number >= 0.5:
                    self.universe_point = 1
                    self.universe_text = "正解！ 多数派があなたと同じように考えています"
                else:
                    self.universe_point = 0
                    self.universe_text = "不正解！ 多数派はあなたと同じように考えていません"
        elif meta_universes[self.number - 1] == 1:
            print("少数派と答えている")
            if universes[self.number - 1] == 0:
                print("はいと答えている")
                if self.total_universe / self.number >= 0.5:
                    self.universe_point = 1
                    self.universe_text = "正解！ 少数派があなたと同じように考えています"
                else:
                    self.universe_point = 0
                    self.universe_text = "不正解！ 少数派はあなたと同じように考えていません"
            elif universes[self.number - 1] == 1:
                print("いいえと答えている")
                if self.total_universe / self.number <= 0.5:
                    self.universe_point = 1
                    self.universe_text = "正解！ 少数派があなたと同じように考えています"
                else:
                    self.universe_point = 0
                    self.universe_text = "不正解！ 少数派はあなたと同じように考えていません"
        """
                    


        colors = [p.color for p in self.get_players()]
        self.total_color = sum(colors)
        meta_colors = [p.meta_color for p in self.get_players()]
        self.total_meta_color = sum(meta_colors)
        

        conspiracy_theorys = [p.conspiracy_theory for p in self.get_players()]
        self.total_conspiracy_theory = sum(conspiracy_theorys)
        meta_conspiracy_theorys = [p.meta_conspiracy_theory for p in self.get_players()]
        self.total_meta_conspiracy_theory = sum(meta_conspiracy_theorys)


        intelligences = [p.intelligence for p in self.get_players()]
        self.total_intelligence = sum(intelligences)
        meta_intelligences = [p.meta_intelligence for p in self.get_players()]
        self.total_meta_intelligence = sum(meta_intelligences)


        dresss = [p.dress for p in self.get_players()]
        self.total_dress = sum(dresss)
        meta_dresss = [p.meta_dress for p in self.get_players()]
        self.total_meta_dress = sum(meta_dresss)


        shoess = [p.shoes for p in self.get_players()]
        self.total_shoes = sum(shoess)
        meta_shoess = [p.meta_shoes for p in self.get_players()]
        self.total_meta_shoes = sum(meta_shoess)
    

        fakenewss = [p.fakenews for p in self.get_players()]
        self.total_fakenews = sum(fakenewss)
        meta_fakenewss = [p.meta_fakenews for p in self.get_players()]
        self.total_meta_fakenews = sum(meta_fakenewss)


        tours = [p.tour for p in self.get_players()]
        self.total_tour = sum(tours)
        meta_tours = [p.meta_tour for p in self.get_players()]
        self.total_meta_tour = sum(meta_tours)


        vaccines = [p.vaccine for p in self.get_players()]
        self.total_vaccine = sum(vaccines)
        meta_vaccines = [p.meta_vaccine for p in self.get_players()]
        self.total_meta_vaccine = sum(meta_vaccines)


    def result_compute(self):
        if 0.5 <= (self.total_universe / self.number):
            self.universe_text = '平均よりも賢いと考えている人が多数派です'
        else :
            self.universe_text = '平均よりも賢くないと考えている人が多数派です'
        

        if 0.5 <= (self.total_color / self.number):
            self.color_text = '平均よりもフェイクニュースに騙されると考えている人が多数派です'
        else :
            self.color_text = '平均よりもフェイクニュースに騙されないと考えている人が多数派です'


        if 0.5 <= (self.total_conspiracy_theory / self.number):
            self.conspiracy_theory_text = '平均よりもフェイクニュースに騙されると考えている人が多数派です'
        else :
            self.conspiracy_theory_text = '平均よりもフェイクニュースに騙されないと考えている人が多数派です'


        if 0.5 <= (self.total_intelligence / self.number):
            self.intelligence_text = '平均よりもフェイクニュースに騙されると考えている人が多数派です'
        else :
            self.intelligence_text = '平均よりもフェイクニュースに騙されないと考えている人が多数派です'


        if 0.5 <= (self.total_dress / self.number):
            self.dress_text = '平均よりもフェイクニュースに騙されると考えている人が多数派です'
        else :
            self.dress_text = '平均よりもフェイクニュースに騙されないと考えている人が多数派です'


        if 0.5 <= (self.total_shoes / self.number):
            self.shoes_text = '平均よりもフェイクニュースに騙されると考えている人が多数派です'
        else :
            self.shoes_text = '平均よりもフェイクニュースに騙されないと考えている人が多数派です'


        if 0.5 <= (self.total_fakenews / self.number):
            self.fakenews_text = '平均よりもフェイクニュースに騙されると考えている人が多数派です'
        else :
            self.fakenews_text = '平均よりもフェイクニュースに騙されないと考えている人が多数派です'


        if 0.5 <= (self.total_tour / self.number):
            self.tour_text = '平均よりもフェイクニュースに騙されると考えている人が多数派です'
        else :
            self.tour_text = '平均よりもフェイクニュースに騙されないと考えている人が多数派です'


        if 0.5 <= (self.total_vaccine / self.number):
            self.vaccine_text = '平均よりもフェイクニュースに騙されると考えている人が多数派です'
        else :
            self.vaccine_text = '平均よりもフェイクニュースに騙されないと考えている人が多数派です'

#プレイヤーごとの質問と答え
class Player(BasePlayer):
    universe = models.IntegerField(choices=[[0, 'はい'],[1, 'いいえ']], label='この宇宙は究極的には素粒子やその間に働く力など物理的なものに尽きており非物理的なものなど存在しない', widget=widgets.RadioSelect, initial=0)
    meta_universe = models.IntegerField(choices=[[0, '多数派'],[1, '少数派']], label='前の質問で、あなたが答えた回答は多数派だと想いますか、少数派だと思いますか？', widget=widgets.RadioSelect, initial=0)


    color = models.IntegerField(choices=[[0, 'はい'],[1, 'いいえ']], label='色は人間が存在してなくても世界に存在している', widget=widgets.RadioSelect, initial=0)
    meta_color = models.IntegerField(choices=[[0, '多数派'],[1, '少数派']], label='前の質問で、あなたが答えた回答は多数派だと想いますか、少数派だと思いますか？', widget=widgets.RadioSelect, initial=0)


    conspiracy_theory = models.IntegerField(choices=[[0, 'はい'],[1, 'いいえ']], label='自分を含めた一部の人以外の、世の中の大多数の人々は、陰謀論に騙されている', widget=widgets.RadioSelect, initial=0)
    meta_conspiracy_theory = models.IntegerField(choices=[[0, '多数派'],[1, '少数派']], label='前の質問で、あなたが答えた回答は多数派だと想いますか、少数派だと思いますか？', widget=widgets.RadioSelect, initial=0)


    intelligence = models.IntegerField(choices=[[0, 'はい'],[1, 'いいえ']], label='自分は正直、平均的な人よりは知能が高いと思う', widget=widgets.RadioSelect, initial=0)
    meta_intelligence = models.IntegerField(choices=[[0, '多数派'],[1, '少数派']], label='前の質問で、あなたが答えた回答は多数派だと想いますか、少数派だと思いますか？', widget=widgets.RadioSelect, initial=0)


    dress = models.IntegerField(choices=[[0, '白と金'],[1, '青と黒']], label='このドレスの色は？', widget=widgets.RadioSelect, initial=0)
    meta_dress = models.IntegerField(choices=[[0, '多数派'],[1, '少数派']], label='前の質問で、あなたが答えた回答は多数派だと想いますか、少数派だと思いますか？', widget=widgets.RadioSelect, initial=0)


    shoes = models.IntegerField(choices=[[0, 'はい'],[1, 'いいえ']], label='このシューズの色は？', widget=widgets.RadioSelect, initial=0)
    meta_shoes = models.IntegerField(choices=[[0, '多数派'],[1, '少数派']], label='前の質問で、あなたが答えた回答は多数派だと想いますか、少数派だと思いますか？', widget=widgets.RadioSelect, initial=0)


    fakenews = models.IntegerField(choices=[[0, 'はい'],[1, 'いいえ']], label='自分はフェイクニュースに騙されない方である', widget=widgets.RadioSelect, initial=0)
    meta_fakenews = models.IntegerField(choices=[[0, '多数派'],[1, '少数派']], label='前の質問で、あなたが答えた回答は多数派だと想いますか、少数派だと思いますか？', widget=widgets.RadioSelect, initial=0)


    tour = models.IntegerField(choices=[[0, 'はい'],[1, 'いいえ']], label='あなたは友人と、絶景で有名な国立公園のツアーに参加しようとしています。ところが、そのツアーの同意書に、「このツアーにより、0.0001％の確率で死亡することがあります。」と書かれているのを友人が見つけました。あなたはそれでもこのツアーに参加しますか？', widget=widgets.RadioSelect, initial=0)
    meta_tour = models.IntegerField(choices=[[0, '多数派'],[1, '少数派']], label='前の質問で、あなたが答えた回答は多数派だと想いますか、少数派だと思いますか？', widget=widgets.RadioSelect, initial=0)


    vaccine = models.IntegerField(choices=[[0, 'はい'],[1, 'いいえ']], label ='成人になると100人に１人が罹患する病気があり、発見が遅れれば命にかかわることになります。ワクチンを打てばその病気はほぼ確実に発症しなくなることが知られています。しかしながら、ワクチンは0.0001％の確率で重篤な副作用があり、最悪の場合死に至ります。あなたはそれでもワクチンを打ちますか？', widget=widgets.RadioSelect, initial=0)
    meta_vaccine = models.IntegerField(choices=[[0, '多数派'],[1, '少数派']], label='前の質問で、あなたが答えた回答は多数派だと想いますか、少数派だと思いますか？', widget=widgets.RadioSelect, initial=0)

    sex = models.IntegerField(choices=[[0, '男性'],[1, '女性'],[2, 'その他']], label ='', widget=widgets.RadioSelect, initial=0)

    age = models.IntegerField(initial=0)


#ページの定義
class Start_Page(Page):
    @staticmethod
    def before_next_page(self, timeout_happened):
        #参加者の人数をカウント
        self.group.number += 1


class Universe(Page):
    form_model = 'player'
    form_fields = ['universe', 'meta_universe']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
        #参加者の人数をカウント
        #self.group.number += 1
        #print('＋1')
class Universe_result(Page):
    pass
    #@staticmethod
    #def is_displayed(player):
    #    print("idは",player.id_in_group)
    #    return player.id_in_group >= 3


class Color(Page):
    form_model = 'player'
    form_fields = ['color', 'meta_color']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class Color_result(Page):
    @staticmethod
    def is_displayed(player):
        print("idは",player.id_in_group)
        return player.id_in_group >= 3


class Conspiracy_theory(Page):
    form_model = 'player'
    form_fields = ['conspiracy_theory']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class Conspiracy_theory_meta(Page):
    form_model = 'player'
    form_fields = ['meta_conspiracy_theory']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
        self.group.result_compute()
class Conspiracy_theory_result(Page):
    @staticmethod
    def is_displayed(player):
        print("idは",player.id_in_group)
        return player.id_in_group >= 3


class Intelligence(Page):
    form_model = 'player'
    form_fields = ['intelligence']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class Intelligence_meta(Page):
    form_model = 'player'
    form_fields = ['meta_intelligence']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
        self.group.result_compute()
class Intelligence_result(Page):
    @staticmethod
    def is_displayed(player):
        print("idは",player.id_in_group)
        return player.id_in_group >= 3


class Dress(Page):
    form_model = 'player'
    form_fields = ['dress']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class Dress_meta(Page):
    form_model = 'player'
    form_fields = ['meta_dress']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
        self.group.result_compute()
class Dress_result(Page):
    @staticmethod
    def is_displayed(player):
        print("idは",player.id_in_group)
        return player.id_in_group >= 3


class Shoes(Page):
    form_model = 'player'
    form_fields = ['shoes']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class Shoes_meta(Page):
    form_model = 'player'
    form_fields = ['meta_shoes']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
        self.group.result_compute()
class Shoes_result(Page):
    @staticmethod
    def is_displayed(player):
        print("idは",player.id_in_group)
        return player.id_in_group >= 3


class Fakenews(Page):
    form_model = 'player'
    form_fields = ['fakenews']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class Fakenews_meta(Page):
    form_model = 'player'
    form_fields = ['meta_fakenews']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
        self.group.result_compute()
class Fakenews_result(Page):
    @staticmethod
    def is_displayed(player):
        print("idは",player.id_in_group)
        return player.id_in_group >= 3


class Tour(Page):
    form_model = 'player'
    form_fields = ['tour']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class Tour_meta(Page):
    form_model = 'player'
    form_fields = ['meta_tour']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
        self.group.result_compute()
class Tour_result(Page):
    @staticmethod
    def is_displayed(player):
        print("idは",player.id_in_group)
        return player.id_in_group >= 3


class Vaccine(Page):
    form_model = 'player'
    form_fields = ['vaccine']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class Vaccine_meta(Page):
    form_model = 'player'
    form_fields = ['meta_vaccine']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
        self.group.result_compute()
class Vaccine_result(Page):
    @staticmethod
    def is_displayed(player):
        print("idは",player.id_in_group)
        return player.id_in_group >= 3


class Higher_Threshold_Lastpage(Page):
    @staticmethod
    def is_displayed(player):
        print("idは",player.id_in_group)
        return player.id_in_group >= 3


class Lower_Threshold_Lastpage(Page):
    pass

class Demography(Page):
    form_model = 'player'
    form_fields = ['age', 'sex']


#ページ表示の順番
page_sequence = [Start_Page, Universe, Universe_result, Color, Color_result, Conspiracy_theory, Conspiracy_theory_meta, Conspiracy_theory_result, Intelligence, Intelligence_meta, Intelligence_result, Dress, Dress_meta, Dress_result, Shoes, Shoes_meta, Shoes_result, Fakenews, Fakenews_meta, Fakenews_result, Tour, Tour_meta, Tour_result, Vaccine, Vaccine_meta, Vaccine_result, Higher_Threshold_Lastpage, Lower_Threshold_Lastpage]