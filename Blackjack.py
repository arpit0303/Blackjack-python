# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
hitt=False
standd=False
h=False
g=0
a=0
val=0
h_val=0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.suit = ""
        self.rank = ""
        self.hand_value = 0
        self.hand = False

    def __str__(self):
        # return a string representation of a hand
        return self.suit

    def add_card(self, card):
        # add a card object to a hand
        self.suit = card.get_suit()
        self.rank = card.get_rank()
        self.hand=True
        

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        global outcome,outcome2,h,standd,outcome3
        if h:
            self.hand_value = VALUES[self.rank]+VALUES[outcome[1]]+VALUES[outcome2[1]]
            
            if self.rank != 'A' and outcome[1] != 'A' and outcome2[1] != 'A':
                return self.hand_value
            elif (self.hand_value + 10) <= 21:
                self.hand_value += 10
                return self.hand_value
            else:
                return self.hand_value
            
        if standd:
            self.hand_value = VALUES[self.rank]+VALUES[outcome3[1]]
            return self.hand_value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        card=Card(self.suit,self.rank)
        card.draw(canvas,pos)
       
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.outcome=[]
        for i in SUITS:
            for j in RANKS:
                self.outcome.append(i+j)

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.outcome)

    def deal_card(self):
        # deal a card object from the deck
        random.choice(self.outcome)
    
    def __str__(self):
        # return a string representing the deck
        for out in self.outcome:
            return out
  
#define event handlers for buttons
def deal():
    global outcome, in_play,outcome2,outcome3,hitt,h,score,standd,player,g,t,a,b,c,val,h_val,in_play
    b=0
    val=0
    a=0
    c=0
    t=0
    g=0
    h_val=0
    # your code goes here
    if h and not standd:
        score -=1
    
    h=False
    hitt=False
    standd=False
    in_play=True
    d=Deck()
    d.shuffle()
    d.deal_card()
    outcome=str(d)
    
    d.shuffle()
    d.deal_card()
    outcome2=str(d)
    
    d.shuffle()
    d.deal_card()
    outcome3=str(d)
    in_play = True
    player=VALUES[outcome[1]]+VALUES[outcome2[1]]

def hit():
    # replace with your code below
    global r3,s3,in_play,h_val,score,hitt,h,player,g,s6,r6,s7,r7,t
    # if the hand is in play, hit the player
    if t==1:
        g=0
        t=0
    hitt=True
    h=True
    if in_play:
        if g==2:
            h = Hand()
            s7 = random.choice(SUITS)
            r7 = random.choice(RANKS)
            card = Card(s7,r7)
            h.add_card(card)
            h_val += h.get_value()-VALUES[outcome[1]]-VALUES[outcome2[1]]
            player=h_val
            t=1
        if g==1:
            h = Hand()
            s6 = random.choice(SUITS)
            r6 = random.choice(RANKS)
            card = Card(s6,r6)
            h.add_card(card)
            h_val += h.get_value()-VALUES[outcome[1]]-VALUES[outcome2[1]]
            player=h_val
            g +=1
        if g == 0:
            h = Hand()
            s3 = random.choice(SUITS)
            r3 = random.choice(RANKS)
            card = Card(s3,r3)
            h.add_card(card)
            h_val += h.get_value()
            player=h_val
            g += 1
    
    # if busted, assign a message to outcome, update in_play and score
    if h_val > 21 and in_play:
        player=100
        in_play=False
        h=False
        score -=1
    
def stand():
    # replace with your code below
    global in_play,h,s4,r4,standd,s5,r5,outcome3,player,score,a,s8,r8,s9,r9,b,c,val
    if b==1:
        a=0
        b=0
        
    h=False
    standd=True
    s = Hand()
    s4 = random.choice(SUITS)
    r4 = random.choice(RANKS)
    card1 = Card(s4,r4)
    s.add_card(card1)
    val = s.get_value()
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        if val < 17 and a==0:
            s5 = random.choice(SUITS)
            r5 = random.choice(RANKS)
            card2 = Card(s5,r5)
            s.add_card(card2)
            val += s.get_value()-VALUES[outcome3[1]]
            a +=1
        if val < 17 and a==1:
            s8 = random.choice(SUITS)
            r8 = random.choice(RANKS)
            card2 = Card(s8,r8)
            s.add_card(card2)
            val += s.get_value()-VALUES[outcome3[1]]
            b = 1
        if val < 17 and b==1:
            s9 = random.choice(SUITS)
            r9 = random.choice(RANKS)
            card2 = Card(s9,r9)
            s.add_card(card2)
            val += s.get_value()-VALUES[outcome3[1]]
            c = 1

    # assign a message to outcome, update in_play and score
    if player >= val and player <= 21 and val <= 21:
        score += 1
    elif player <= 21 and val <= 21:
        score -= 1
    elif val > 21: 
        score += 1
    elif player > 21:
        score -= 1

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome,outcome2,outcome3,score,hitt,s3,r3,h_val,in_play,h,s4,r4,standd,s5,r5,g,s6,r6,s7,r7,t,a,s8,r8,s9,r9,val,b
    card = Card(outcome[0], outcome[1])
    card.draw(canvas, [180, 400])
    
    card = Card(outcome2[0], outcome2[1])
    card.draw(canvas, [80, 400])
    
    card = Card(outcome3[0], outcome3[1])
    card.draw(canvas, [180, 200])
    
    canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [80 + CARD_BACK_CENTER[0], 202 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    canvas.draw_text("Blackjack",[80,80],50,"Blue")
    canvas.draw_text("Dealer",[80,170],30,"Black")
    canvas.draw_text("Player",[80,370],30,"Black")
    if not hitt and not standd:
        canvas.draw_text("Hit OR Stand?",[250,370],30,"Black")
    canvas.draw_text("Score: "+str(score),[400,120],40,"Black")
    if hitt:
        h=Hand()
        card = Card(s3,r3)
        h.add_card(card)
        h_val = h.get_value()
        h.draw(canvas, [280,400])
        if g == 2:
            h=Hand()
            card = Card(s6,r6)
            h.add_card(card)
            h_val += h.get_value()-VALUES[outcome[1]]-VALUES[outcome2[1]]
            h.draw(canvas, [380,400])
        if t == 1:
            h=Hand()
            card = Card(s7,r7)
            h.add_card(card)
            h_val += h.get_value()-VALUES[outcome[1]]-VALUES[outcome2[1]]
            h.draw(canvas, [480,400])
        if h_val > 21:
            canvas.draw_text("You are Busted.",[250,370],30,"White")
            h=False
        elif h_val >= 18 and not standd:
            canvas.draw_text("Hit or Stand?",[250,370],30,"Black")
        elif not standd:
            canvas.draw_text("Hit or Stand?",[250,370],30,"Black")
        
  
    if standd:
        s=Hand()
        card1 = Card(s4,r4)
        s.add_card(card1)
        s.draw(canvas, [80,202])
        if a==1:
            card2 = Card(s5,r5)
            s.add_card(card2)
            s.draw(canvas, [280,202])
        if b==1:
            card2 = Card(s8,r8)
            s.add_card(card2)
            s.draw(canvas, [380,202])
        if c==1:
            card2 = Card(s9,r9)
            s.add_card(card2)
            s.draw(canvas, [480,202])
        if val > 21:
            canvas.draw_text("Dealer are Busted.",[250,180],30,"White")
        canvas.draw_text("New Deal?",[250,370],30,"Black")
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()

# remember to review the gradic rubric