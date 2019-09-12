import random
class Card():
    def __init__(self,suit,rank_value):
        self._suit = suit
        self._rank_value = rank_value

    def get_suit(self):
        return self._suit
    def get_rank_value(self):
        return self._rank_value
    def get_suit_symbol(self):
        if self._suit == "Club":
            return "\u2663"
        elif self._suit == "Diamond":
            return "\u2662"
        elif self._suit == "Heart":
            return "\u2661"
        elif self._suit == "Spade":
            return "\u2660"
    def get_rank(self):
        if self._rank_value == 1:
            return "A"
        elif self._rank_value == 11:
            return "J"
        elif self._rank_value == 12:
            return "Q"
        elif self._rank_value == 13:
            return "K"
        else:
            return str(self._rank_value)

    def __str__(self):
        s = self.get_rank()
        s += self.get_suit_symbol()
        return s



class CardList():
    def __init__(self):
        self._cards = list()
    def add_card(self,new_card):
        self._cards.append(new_card)
    def get_cards(self):
        return self._cards
    def get_size(self):
        return len(self._cards)
    def shuffle(self):
        random.shuffle(self._card)
    def __str__(self):
        s = ""
        for i in self._cards:
            s += str(i) + ","
        return s[:-1]

    def insertionsort(self,a,n):
        pivot=a[0]
        left = []
        right = []

        for i in range(1,len(a)):
            if a[i].get_rank_value() > pivot[n].get_rank_value():
                right.append(a[i])
            else:
                left.append(a[i])
        return insertionsort(left) + [pivot] + insertionsort(right)

    def bubblesort(a,n):
        for i in range(len(a)-1):
            for j in range(len(a)-1-i):
                if a[j] > a[j+1][n]:
                    a[j],a[j+1] = a[j+1],a[j]
        return a

    def sort_by_suit(self):
        bysuit = [[],[],[],[]]
        for i in self._cards:
            if i.get_suit() = "Spade":
                bysuit[0].append(i)
            if i.get_suit() = "Heart":
                bysuit[1].append(i)
            if i.get_suit() = "Diamond":
                bysuit[2].append(i)
            if i.get_suit() = "Club":
                bysuit[3].append(i)
        for i in range(4):
            bysuit[i] = quicksort(bysuit[i])

        self._cards = []
        for i in range(4):
            for j in i:
                self._cards.add_card(j)

    
                
        



        
