from otree.api import *
c = cu

doc = ''

#ゲームの定義
class Constants(BaseConstants):
    name_in_url = ''
    players_per_group = 500
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


#プレイヤー共通データを格納
class Group(BaseGroup):
    #プレイヤー番号
    number = models.IntegerField(initial=0)

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
                    if total / number <= 0.45:
                        text = "正解！ 多数派があなたと同じように考えています"
                    elif total / number >= 0.55:
                        text = "不正解！ 多数派はあなたと同じように考えていません"
                    else:
                        text = "およそ半々でした"
                elif answer[number - 1] == 1:
                    if total / number >= 0.55:
                        text = "正解！ 多数派があなたと同じように考えています"
                    elif total / number <= 0.45:
                        text = "不正解！ 多数派はあなたと同じように考えていません"
                    else:
                        text = "およそ半々でした"
            elif meta_answer[number - 1] == 1:
                if answer[number - 1] == 0:
                    if total / number >= 0.55:
                        text = "正解！ 少数派があなたと同じように考えています"
                    elif total / number <= 0.45:
                        text = "不正解！ 少数派はあなたと同じように考えていません"
                    else:
                        text = "およそ半々でした"
                elif answer[number - 1] == 1:
                    if total / number <= 0.45:
                        text = "正解！ 少数派があなたと同じように考えています"
                    elif total / number >= 0.55:
                        text = "不正解！ 少数派はあなたと同じように考えていません"
                    else:
                        text = "およそ半々でした"
            return text

        universes = [p.universe for p in self.get_players()]
        self.total_universe = sum(universes)
        self.total_universe_0 = self.number - self.total_universe
        meta_universes = [p.meta_universe for p in self.get_players()]
        self.universe_text = cal(self.number, universes, meta_universes, self.total_universe)

        colors = [p.color for p in self.get_players()]
        self.total_color = sum(colors)
        self.total_color_0 = self.number - self.total_color
        meta_colors = [p.meta_color for p in self.get_players()]
        self.color_text = cal(self.number, colors, meta_colors, self.total_color)

        conspiracy_theorys = [p.conspiracy_theory for p in self.get_players()]
        self.total_conspiracy_theory = sum(conspiracy_theorys)
        self.total_conspiracy_theory_0 = self.number - self.total_conspiracy_theory
        meta_conspiracy_theorys = [p.meta_conspiracy_theory for p in self.get_players()]
        self.conspiracy_theory_text = cal(self.number, conspiracy_theorys, meta_conspiracy_theorys, self.total_conspiracy_theory)

        intelligences = [p.intelligence for p in self.get_players()]
        self.total_intelligence = sum(intelligences)
        self.total_intelligence_0 = self.number - self.total_intelligence
        meta_intelligences = [p.meta_intelligence for p in self.get_players()]
        self.intelligence_text = cal(self.number, intelligences, meta_intelligences, self.total_intelligence)

        dresss = [p.dress for p in self.get_players()]
        self.total_dress = sum(dresss)
        self.total_dress_0 = self.number - self.total_dress
        meta_dresss = [p.meta_dress for p in self.get_players()]
        self.dress_text = cal(self.number, dresss, meta_dresss, self.total_dress)

        shoess = [p.shoes for p in self.get_players()]
        self.total_shoes = sum(shoess)
        self.total_shoes_0 = self.number - self.total_shoes
        meta_shoess = [p.meta_shoes for p in self.get_players()]
        self.shoes_text = cal(self.number, shoess, meta_shoess, self.total_shoes)

        fakenewss = [p.fakenews for p in self.get_players()]
        self.total_fakenews = sum(fakenewss)
        self.total_fakenews_0 = self.number - self.total_fakenews
        meta_fakenewss = [p.meta_fakenews for p in self.get_players()]
        self.fakenews_text = cal(self.number, fakenewss, meta_fakenewss, self.total_fakenews)

        tours = [p.tour for p in self.get_players()]
        self.total_tour = sum(tours)
        self.total_tour_0 = self.number - self.total_tour
        meta_tours = [p.meta_tour for p in self.get_players()]
        self.tour_text = cal(self.number, tours, meta_tours, self.total_tour)

        vaccines = [p.vaccine for p in self.get_players()]
        self.total_vaccine = sum(vaccines)
        self.total_vaccine_0 = self.number - self.total_vaccine
        meta_vaccines = [p.meta_vaccine for p in self.get_players()]
        self.vaccine_text = cal(self.number, vaccines, meta_vaccines, self.total_vaccine)


    majority_score = models.IntegerField()

    def majoirty_score_compute(self):
        total_score = 0
        def cal(answer, total_answer, number):
            score = 0
            if answer[number - 1] == 0:
                if total_answer / number <= 0.5:
                    score += 1
            elif answer[number - 1] == 0:
                if total_answer / number <= 0.5:
                    score += 1
            return score
        
        universes = [p.universe for p in self.get_players()]
        self.total_universe = sum(universes)
        total_score += cal(universes, self.total_universe, self.number)
        
        colors = [p.color for p in self.get_players()]
        self.total_color = sum(colors)
        total_score += cal(colors, self.total_color, self.number)

        conspiracy_theorys = [p.conspiracy_theory for p in self.get_players()]
        self.total_conspiracy_theory = sum(conspiracy_theorys)
        total_score += cal(conspiracy_theorys, self.total_conspiracy_theory, self.number)

        intelligences = [p.intelligence for p in self.get_players()]
        self.total_intelligence = sum(intelligences)
        total_score += cal(intelligences, self.total_intelligence, self.number)

        dresss = [p.dress for p in self.get_players()]
        self.total_dress = sum(dresss)
        total_score += cal(dresss, self.total_dress, self.number)

        shoess = [p.shoes for p in self.get_players()]
        self.total_shoes = sum(shoess)  
        total_score += cal(shoess, self.total_shoes, self.number)

        fakenewss = [p.fakenews for p in self.get_players()]
        self.total_fakenews = sum(fakenewss)
        total_score += cal(fakenewss, self.total_fakenews, self.number)

        tours = [p.tour for p in self.get_players()]
        self.total_tour = sum(tours)
        total_score += cal(tours, self.total_tour, self.number)

        vaccines = [p.vaccine for p in self.get_players()]
        self.total_vaccine = sum(vaccines)
        total_score += cal(vaccines, self.total_vaccine, self.number)

        self.majority_score = int(total_score / 9 * 100)


    meta_score = models.IntegerField()

    def meta_score_compute(self):
        total_score = 0
        def cal(number, answer, meta_answer, total):
            score = 0
            if meta_answer[number - 1] == 0:
                if answer[number - 1] == 0:
                    if total / number <= 0.5:
                        score += 1
                elif answer[number - 1] == 1:
                    if total / number >= 0.50:
                        score += 1
            elif meta_answer[number - 1] == 1:
                if answer[number - 1] == 0:
                    if total / number >= 0.50:
                        score += 1
                elif answer[number - 1] == 1:
                    if total / number <= 0.45:
                        score += 1
            return score

        universes = [p.universe for p in self.get_players()]
        self.total_universe = sum(universes)
        meta_universes = [p.meta_universe for p in self.get_players()]
        total_score += cal(self.number, universes, meta_universes, self.total_universe)

        colors = [p.color for p in self.get_players()]
        self.total_color = sum(colors)
        meta_colors = [p.meta_color for p in self.get_players()]
        total_score += cal(self.number, colors, meta_colors, self.total_color)

        conspiracy_theorys = [p.conspiracy_theory for p in self.get_players()]
        self.total_conspiracy_theory = sum(conspiracy_theorys)
        meta_conspiracy_theorys = [p.meta_conspiracy_theory for p in self.get_players()]
        total_score += cal(self.number, conspiracy_theorys, meta_conspiracy_theorys, self.total_conspiracy_theory)

        intelligences = [p.intelligence for p in self.get_players()]
        self.total_intelligence = sum(intelligences)
        meta_intelligences = [p.meta_intelligence for p in self.get_players()]
        total_score += cal(self.number, intelligences, meta_intelligences, self.total_intelligence)

        dresss = [p.dress for p in self.get_players()]
        self.total_dress = sum(dresss)
        meta_dresss = [p.meta_dress for p in self.get_players()]
        total_score += cal(self.number, dresss, meta_dresss, self.total_dress)

        shoess = [p.shoes for p in self.get_players()]
        self.total_shoes = sum(shoess)
        meta_shoess = [p.meta_shoes for p in self.get_players()]
        total_score += cal(self.number, shoess, meta_shoess, self.total_shoes)

        fakenewss = [p.fakenews for p in self.get_players()]
        self.total_fakenews = sum(fakenewss)
        meta_fakenewss = [p.meta_fakenews for p in self.get_players()]
        total_score += cal(self.number, fakenewss, meta_fakenewss, self.total_fakenews)

        tours = [p.tour for p in self.get_players()]
        self.total_tour = sum(tours)
        meta_tours = [p.meta_tour for p in self.get_players()]
        total_score += cal(self.number, tours, meta_tours, self.total_tour)

        vaccines = [p.vaccine for p in self.get_players()]
        self.total_vaccine = sum(vaccines)
        meta_vaccines = [p.meta_vaccine for p in self.get_players()]
        total_score += cal(self.number, vaccines, meta_vaccines, self.total_vaccine)

        self.meta_score = int(total_score / 9 * 100)

    result_text = models.StringField()

    def result_compute(self):
        text = ''
        if self.majority_score >= 80:
            if self.meta_score >= 80:
                text = 'あなたはごく普通の人で、自分のことをよく知っています。他の人がどう思うかを知っているのは、あなたの強みです。そして、人とは違う考え方をしてみようというきっかけになるかもしれません 同時に、ゲームを続けてみると、ここにも意外な自分の一面があるかもしれません。'
            elif self.meta_score >= 65:
                text = 'あなたはごく普通の人で、自分のことを十分に知っています。そして、人とは違う考え方をしてみようというきっかけになるかもしれません同時に、ゲームを続けることで、自分自身をより深く理解することができます。自分の意外な一面が見えてくるかもしれません。'
            elif self.meta_score >= 50:
                text = 'あなたが思っているほど、あなたはユニークでもなければ、珍しい存在でもありません。自分のセルフイメージを見直したほうがいいですよ。このゲームで自分を鍛え、他の人がどう思うかを知ることで、自分をよりよく知ることができます。'
            else:
                text = '自分のことをもっと知りたいあなたは、あなたが思っているようなユニークさや珍しさは全くありません。間違ったセルフイメージを持っていると、とても危険です。このゲームで自分を鍛え、他の人がどう思うかを知ることで、自分をよりよく知ることができます。'
        elif self.majority_score >= 65:
            if self.meta_score >= 80:
                text = 'あなたは一般的に平凡で、自分のことをよく知っています。他の人がどう思うかを知っているのは、あなたの強みです。そして、人とは違う考え方をしてみようというきっかけになるかもしれません同時に、ゲームを続けてみると、ここにも意外な自分の一面があるかもしれません。'
            elif self.meta_score >= 65:
                text = 'あなたは一般的には普通で、自分のことを十分に知っています。そして、人とは違う考え方をしてみようというきっかけになるかもしれません同時に、ゲームを続けることで、自分自身をより深く理解することができます。自分の意外な一面が見えてくるかもしれません。'
            elif self.meta_score >= 50:
                text = 'あなたが思っているほど、あなたはユニークでもなければ、珍しい存在でもありません。自分のセルフイメージを見直したほうがいいですよ。このゲームで自分を鍛え、他の人がどう思うかを知ることで、自分をよりよく知ることができます。'
            else:
                text = '自分のことをもっと知りたいあなたは、あなたが思っているようなユニークさや珍しさは全くありません。間違ったセルフイメージを持っていると、とても危険です。このゲームで自分を鍛え、他の人がどう思うかを知ることで、自分をよりよく知ることができます。'
        elif self.majority_score >= 50:
            if self.meta_score >= 80:
                text = 'あなたは他の人とは少し違っていて、自分のことをよく知っています。これがあなたの美点であり強みです。おめでとうございます。ゲームを続けていくと、意外な自分の一面がここにあるかもしれません。'
            elif self.meta_score >= 65:
                text = 'あなたは他の人とは少し違っていて、自分のことを十分に知っています。これがあなたの美点であり強みです。おめでとうございます。しかし、このゲームを通して自分に対する理解を深めることはできます。ゲームを続けることで、自分をより深く理解することができます。自分の意外な一面を発見できるかもしれません。'
            elif self.meta_score >= 50:
                text = 'あなたは他の人とは少し違っていますが、他の人との関係で自分を意識していないようです。あなたが思っているほど、あなたは普通ではありません。このゲームで自分を鍛え、他の人がどう思うかを知ることで、自分をよりよく知ることができます。'
            else:
                text = 'あなたは他の人とは少し違いますが、自分のユニークさを知らないままでいるのは非常に危険なことです。あなたは自分が思っているような普通の人ではありません。このゲームで自分を鍛え、他の人がどう思うかを知ることで、自分をよりよく知ることができます。'
        else:
            if self.meta_score >= 80:
                text = '他の人とは全く違うことがあなたの美点であり、自分のユニークさをよく理解していることがあなたの強みです。おめでとうございます。ゲームを続けていくと、意外な自分の一面がここにあるかもしれません。'
            elif self.meta_score >= 65:
                text = '自分は他の人とは全く違うというのがあなたの美徳であり、自分のユニークさを一般的に認識しています。ゲームを続けることで、自分をより深く理解することができます。自分の意外な一面を発見できるかもしれません。'
            elif self.meta_score >= 50:
                text = '自分は他の人とは全く違うというのが、あなたの美徳です。しかし、あなたは自分のユニークさに気づいていないようです。あなたが思っているほど、あなたは普通ではありません。このゲームで自分を鍛え、他の人がどう思うかを知ることで、自分をよりよく知ることができます。'
            else:
                text = '自分をもっと知ろう。あなたは自分が思っているような普通の人ではありません。人とは全く違うというのは、あなたの美徳です。しかし、自分のユニークさを知らないままでいるのは、とても危険です。このゲームで自分を鍛え、他の人がどう思うかを知ることで、自分をよりよく知ることができます。'
        self.result_text = text


#プレイヤーごとの質問と答えの格納
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

    shoes = models.IntegerField(choices=[[0, 'グレーと緑'],[1, 'ピンクと白']], label='このシューズの色は？', widget=widgets.RadioSelect, initial=0)
    meta_shoes = models.IntegerField(choices=[[0, '多数派'],[1, '少数派']], label='前の質問で、あなたが答えた回答は多数派だと想いますか、少数派だと思いますか？', widget=widgets.RadioSelect, initial=0)

    fakenews = models.IntegerField(choices=[[0, 'はい'],[1, 'いいえ']], label='自分はフェイクニュースに騙されない方である', widget=widgets.RadioSelect, initial=0)
    meta_fakenews = models.IntegerField(choices=[[0, '多数派'],[1, '少数派']], label='前の質問で、あなたが答えた回答は多数派だと想いますか、少数派だと思いますか？', widget=widgets.RadioSelect, initial=0)

    tour = models.IntegerField(choices=[[0, 'はい'],[1, 'いいえ']], label='あなたは友人と、絶景で有名な国立公園のツアーに参加しようとしています。ところが、そのツアーの同意書に、「このツアーにより、0.0001％の確率で死亡することがあります。」と書かれているのを友人が見つけました。あなたはそれでもこのツアーに参加しますか？', widget=widgets.RadioSelect, initial=0)
    meta_tour = models.IntegerField(choices=[[0, '多数派'],[1, '少数派']], label='前の質問で、あなたが答えた回答は多数派だと想いますか、少数派だと思いますか？', widget=widgets.RadioSelect, initial=0)

    vaccine = models.IntegerField(choices=[[0, 'はい'],[1, 'いいえ']], label ='成人になると100人に１人が罹患する病気があり、発見が遅れれば命にかかわることになります。ワクチンを打てばその病気はほぼ確実に発症しなくなることが知られています。しかしながら、ワクチンは0.0001％の確率で重篤な副作用があり、最悪の場合死に至ります。あなたはそれでもワクチンを打ちますか？', widget=widgets.RadioSelect, initial=0)
    meta_vaccine = models.IntegerField(choices=[[0, '多数派'],[1, '少数派']], label='前の質問で、あなたが答えた回答は多数派だと想いますか、少数派だと思いますか？', widget=widgets.RadioSelect, initial=0)

    sex = models.IntegerField(choices=[[0, '男性'],[1, '女性'],[2, 'その他']], label ='あなたの性別は？', widget=widgets.RadioSelect, initial=0)
    age = models.IntegerField(label ='あなたの年齢は？')


#ページの定義
class StartPage(Page):
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
class UniverseResult(Page):
    pass
    #@staticmethod
    #def is_displayed(player):
    #    return player.id_in_group >= 3

class Color(Page):
    form_model = 'player'
    form_fields = ['color', 'meta_color']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class ColorResult(Page):
    pass
    #@staticmethod
    #def is_displayed(player):
    #    return player.id_in_group >= 3

class ConspiracyTheory(Page):
    form_model = 'player'
    form_fields = ['conspiracy_theory', 'meta_conspiracy_theory']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class ConspiracyTheoryResult(Page):
    pass
    #@staticmethod
    #def is_displayed(player):
    #    return player.id_in_group >= 3

class Intelligence(Page):
    form_model = 'player'
    form_fields = ['intelligence','meta_intelligence']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class IntelligenceResult(Page):
    pass
    #@staticmethod
    #def is_displayed(player):
    #    return player.id_in_group >= 3

class Dress(Page):
    form_model = 'player'
    form_fields = ['dress','meta_dress']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class DressResult(Page):
    pass
    #@staticmethod
    #def is_displayed(player):
    #    return player.id_in_group >= 3

class Shoes(Page):
    form_model = 'player'
    form_fields = ['shoes','meta_shoes']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class ShoesResult(Page):
    pass
    #@staticmethod
    #def is_displayed(player):
    #    return player.id_in_group >= 3

class Fakenews(Page):
    form_model = 'player'
    form_fields = ['fakenews','meta_fakenews']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class FakenewsResult(Page):
    pass
    #@staticmethod
    #def is_displayed(player):
    #    return player.id_in_group >= 3

class Tour(Page):
    form_model = 'player'
    form_fields = ['tour','meta_tour']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class TourResult(Page):
    pass
    #@staticmethod
    #def is_displayed(player):
    #    return player.id_in_group >= 3

class Vaccine(Page):
    form_model = 'player'
    form_fields = ['vaccine','meta_vaccine']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
class VaccineResult(Page):
    pass
    #@staticmethod
    #def is_displayed(player):
    #    return player.id_in_group >= 3

class Demography(Page):
    form_model = 'player'
    form_fields = ['age', 'sex']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.majoirty_score_compute()
        self.group.meta_score_compute()
        self.group.result_compute()

class HigherThresholdLastpage(Page):
    pass
    #@staticmethod
    #def is_displayed(player):
    #    return player.id_in_group >= 3

class LowerThresholdLastpage(Page):
    pass


#ページ表示の順番
page_sequence = [StartPage, Universe, UniverseResult, Color, ColorResult, ConspiracyTheory, ConspiracyTheoryResult, Intelligence, IntelligenceResult, Dress, DressResult, Shoes, ShoesResult, Fakenews, FakenewsResult, Tour, TourResult, Vaccine, VaccineResult, Demography, HigherThresholdLastpage, LowerThresholdLastpage]