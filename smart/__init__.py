from otree.api import *
c = cu


doc = ''

class Constants(BaseConstants):
    name_in_url = 'smart'
    players_per_group = 500
    num_rounds = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_smart = models.IntegerField()
    total_meta_smart = models.IntegerField()
    total_fakenews = models.IntegerField()
    total_meta_fakenews = models.IntegerField()
    number = models.IntegerField(initial=0)
    smart_text = models.StringField()
    fakenews_text = models.StringField()

    def compute(self):
        smarts = [p.smart for p in self.get_players()]
        print('smartsの値は', smarts)

        self.total_smart = sum(smarts)
        print('total_smartの値は', self.total_smart)

        meta_smarts = [p.meta_smart for p in self.get_players()]
        self.total_meta_smart = sum(meta_smarts)
    
        fakenewses = [p.fakenews for p in self.get_players()]
        self.total_fakenews = sum(fakenewses)

        meta_fakenewses = [p.meta_fakenews for p in self.get_players()]
        self.total_meta_fakenews = sum(meta_fakenewses)
    
    def result_compute(self):
        if 0.5 <= (self.total_smart / self.number):
            self.smart_text = '平均よりも賢いと考えている人が多数派です'
        else :
            self.smart_text = '平均よりも賢くないと考えている人が多数派です'
        if 0.5 <= (self.total_fakenews / self.number):
            self.fakenews_text = '平均よりもフェイクニュースに騙されると考えている人が多数派です'
        else :
            self.fakenews_text = '平均よりもフェイクニュースに騙されないと考えている人が多数派です'







class Player(BasePlayer):
    smart = models.IntegerField(choices=[[0, '賢くない'],[1, '賢い']], label='あなたは平均的な人々と比べて賢いですか？', widget=widgets.RadioSelect, initial=0)

    meta_smart = models.IntegerField(choices=[[0, '少数派'],[1, '多数派']], label='前の質問で、あなたが答えた回答は多数派か少数派のどちらだと思いますか？', widget=widgets.RadioSelect, initial=0)

    fakenews = models.IntegerField(choices=[[0, '思う'],[1, '思わない']], label='あなたは平均的な人々と比べてフェイクニュースに騙されるほうだと思いますか？', widget=widgets.RadioSelect, initial=0)

    meta_fakenews = models.IntegerField(choices=[[0, '少数派'],[1, '多数派']], label='前の質問で、あなたが答えた回答は多数派か少数派のどちらだと思いますか？', widget=widgets.RadioSelect, initial=0)


#check

#def check(self, player.smart, b):
  #  c = self.a + self.b
 #   print(c)


#def check():
 #   ratio = self.group.total_smart / self.id_in_group
class Start_Page(Page):
    pass

class Survery1(Page):
    form_model = 'player'
    form_fields = ['smart']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
        self.group.number += 1
        print('＋1')

class Survery2(Page):
    form_model = 'player'
    form_fields = ['meta_smart']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()

class Survery3(Page):
    form_model = 'player'
    form_fields = ['fakenews']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()

class Survery4(Page):
    form_model = 'player'
    form_fields = ['meta_fakenews']
    @staticmethod
    def before_next_page(self, timeout_happened):
        self.group.compute()
        self.group.result_compute()



class Result1(Page):
    @staticmethod
    def is_displayed(player):
        print("idは",player.id_in_group)
        return player.id_in_group >= 3

class Result2(Page):
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



page_sequence = [Start_Page, Survery1, Survery2, Result1, Survery3, Survery4, Result2, Higher_Threshold_Lastpage, Lower_Threshold_Lastpage]