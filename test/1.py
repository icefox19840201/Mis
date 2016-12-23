#encoding:utf-8
# magicians=["alice","david","carolina"]
# for item in magicians:
#     print(item.title())
# num=(1,2,3,4,5)
# num1=[item**2 for item in num]
# print(num1)
# num2=(1,2,4)
# num3=num2[:]
# print(num3)
class Card:
    def __init__(self,rank,suit):
        self.suit=suit
        self.rank=rank
        self.hard,self.soft=self._points()
class NumberCard(Card):
    def _points(self):
        return  int(self.rank),int(self.rank)
class AceCard(Card):
    def _points(self):
        return 1,11
class FaceCard(Card):
    def _points(self):
        return 10,10
#映射
def card(rank,suit):
    class_={
        1:AceCard,
        11:FaceCard,
        12:FaceCard,
        13:FaceCard
    }.get(rank,suit)
    return  class_(rank,suit)
def card1(rank,suit):
        from functools import partial
        part_class={

            1:partial(AceCard,"A"),
            11:partial(FaceCard,"J"),
            12:partial(FaceCard,"Q"),
            13:partial(FaceCard,"k"),
        }.get(rank,partial(NumberCard,str(rank)))
        return part_class(suit)
if __name__=="__main__":
     a=card1(12,1)
     print(a._points())
