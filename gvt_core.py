#this is entirely untested as was written impromptu as a challenge
#the intent was to create a turn-based card battler, deck not included.
import random
class Card:
    __slots__: ["__health","__name","__attack","__cost","__faction","__rarity", "__has_power", "__max_health", "__used_attack", "__power"]
    def __init__(self, name, rarity, has_power = False):
        cost = 0
        health = 0
        attack = 0
        faction = ""
        max_health = 0
        used_attack = False
        #defaults ^: these couldve easily been put in for each value when i used self, but i put them
        #up here seperately for my own readibility and clarification purposes.
        #use self to reference the attributes to the object, and prevent them from being static
        self.__rarity = rarity
        self.__cost = cost
        self.__health = health
        self.__name = name
        self.__attack = attack
        self.__faction = faction
        self.__has_power = has_power
        self.__max_health = max_health
        self.__used_attack = used_attack
        self.__power = power
        #accessors
    def get_health(self):
        return self.__health
    def get_name(self):
        return self.__name
    def get_attack(self):
        return self.__attack
    def get_faction(self):
        return self.__faction
    def get_max_health(self):
        return self.__max_health
    def get_cost(self):
        return self.__cost
    def get_rarity(self):
        return self.__rarity
    def has_used_attack(self):
        return self.__used_attack
    #mutators
    def change_current_health(self, amount):
        self.__health += amount
    def decrease_current_health(self, amount):
        self.__health -= amount
    def change_max_health(self, amount):
        self.__max_health += amount
    def change_atk(self, amount):
        self.__attack += amount
    def set_power(self):
        if self.__has_power == True:
            self.__has_power == False
        elif self.__has_power == False:
            self.__has_power == True
    def get_power_name(self):
        return self.__power
    def set_power_name(self, a_name):
        self.__power = a_name
    tp = 0 #stands for total points
    #this part doesnt need to be implemented as a function, as it is intended to be applied to every single
    #card, for both players.
    self.__as_power = False #does the card have a special power, true if it does, false if not.
    if self.__rarity == "common" or "c":
        self.__has_power = False #commons never have powers.
        tp = 8 #total points, randomly distributed to either hp or atk, commons have 8
        for i in range(tp): #random distribution occurs here
            coin = random.randint(0,1) #simulate a coinflip, ish.
            if coin == 0:
                self.__attack +=1
            else:
                self.__health +=1
                self.__max_health +=1
        self.__cost = random.randint(1, 3)
        self.__has_power == False
    elif self.__rarity == "uncommon" or "u":
        roll == random.randint(0,1) #50/50 chance for a power
        if roll == 0:
            self.__has_power == False
        else:
            self.__has_power == True
        self.__cost = random.randint(2,5) #uncommon cards have a cost between 2 and 5
        
        tp = 12 #uncommon cards have 12 total points, randomly distributed
        for i in range(tp): #random distribution occurs here
            coin = random.randint(0,1) #simulate a coinflip, ish.
            if coin == 0:
                self.__attack +=1
            else:
                self.__health +=1
                self.__max_health +=1
    elif self.__rarity == "rare" or "r":
        roll = random.randint(1,4) #simulating a 75% chance for a power
        if roll <4:
            self.__has_power = True
        else:
            self.__has_power = False
        tp = 16
        for i in range(tp):
            coin = random.randint(0,1)
            if coin == 0:
                self.__attack+=1
            else:
                self.__health +=1
                self.__max_health +=1
        self.__cost = random.randint(4, 7)
    elif self.__rarity == "legendary" or "l":
        self.__has_power == True #legendaries always have a power
        self.__cost = 10 #legendaries always cost 10
        tp = 24
        for i in range(tp):
            coin = random.randint(0,1)
            if coin == 0:
                self.__attack+=1
            else:
                self.__health +=1
                self.__max_health +=1
    def __str__(self):
        RARITY_DICT = {"c":"CN", "u":"CM", "r":"RP", "l":"LS"}
        _string = RAIRTY_DICT[self.__rarity] + \
        " " + self.__power.get_name()[0] + \
        " " + "{:0>2d}".format(self.__cost) + \
        " " + "{:0>2d}".format(self.__attack) + \
        " " + "{:0>2d}".format(self.__health)
        return _string

    def __repr__(self):
        return "rarity: " + self.__rarity \
        + "\nname=" + self.__name \
        + "\ncost=" + self.__cost \
        + "\ncurrentHP=" + str(self.__health) \
        + "\nmaxHP=" + str(self.__max_health) \
        + "\nattack=" + str(self.__attack)
        + "\npower=" + self.__power
    def __eq__(self,other):
        if self.__name == other.__name:
            if self.__rarity == other.__rarity:
                if self.__cost == other.__cost:
                    if self.__max_health == other.__max_health:
                        if self.__attack == other.__attack:
                            if self.__power == other.__power:
                                return True
        
        return False


    def attack_card(card, target_card):
    #used for a card attacking another card
        card.decrease_current_health(target_card.get_attack)
        target_card.decrease_current_health(target_card.get_attack)
    def use_power(self, player):
    #check for special conditions
        return self.__power.activate(self, player)
    def print_card(self):
        rarity_code = "" #setting up to use abbreviations for rarity
        hp_marker = "" #determines color code for hp depending on how much is remaining
        rarity_marker = "" #determines what color to make the rarity code
        if self.__health / self.__max_health == 1: #IF FULL health, print in green
            hp_marker = "\u001b[38;5;28m"
        elif self.__health / self.__max_health >= .5 and self.__health / self.__max_health < 1:
            #if half hp to full, print in yellow
            hp_marker = "\u001b[38;5;11m"
        else:
            #if less than half, print in red
            hp_marker = "\u001b[38;5;9m"
        if self.__rarity == "common" or "c":
            rarity_code = "CN"
            rarity_marker = "\u001b[38;5;7m"
        elif self.__rarity == "uncommon" or "u":
            rarity_code = "CM"
            rarity_marker = "\u001b[38;5;10m"
        elif self.__rarity == "rare" or "r":
            rarity_code = "RP"
            rarity_marker ="\u001b[38;5;7m"
        else:
            rarity_code = "LS"
            rarity_marker = "\u001b[38;5;130m"
        #print the final result of the card, assuring room for more on the same line
        print("["+ rarity_marker + rarity_code, "0"+ str(self.__cost), "0" + str(self.__attack), hp_marker + "0" + str(self.__health) + "]",end="")


    def sort(self): #be able to sort the cards by rarity first, then cost
        RARITY_CODES = { "c":1, "u":2, "r":3, "l":4} #give rarities a key value pair that assigns
        #a rarity to an int, so it can be used for sorting
        def __lt__(self, other):
            if RARITY_CODES[self.__rarity] != RARITY_CODES[other.__rarity]:
                return self.__rarity < other.__rarity
            else:
                return self.__cost < other.__cost

        def __le__(self, other):
            if  RARITY_CODES[self.__rarity] != RARITY_CODES[other.__rarity]:
                return self.__rarity <= other.__rarity
            else:
                return self.__cost <= other.__cost

        def __gt__(self, other):
            if RARITY_CODES[self.__rarity] != RARITY_CODES[other.__rarity]:
                return self.__rarity > other.__rarity
            else:
                return self.__cost > other.__cost

        def __ge__(self, other):
            if RARITY_CODES[self.__rarity] != RARITY_CODES[other.__rarity]:
                return self.__rarity >= other.__rarity
            else:
                return self.__cost >= other.__cost

    def __hash__(self): #hash the card
        hashing = self.__attack + 31**self.__health
        return hashing

class Player:
    __slots__ = ["__score", "__resource_points", "__deck", "__faction", "__hand", "__graveyard",
    "__battalion", "__current_rp",]
    def __init__(self, score, resource_points, faction):
        self.__score = 100
        self.__resource_points = 0
        self.__deck = []
        self.__faction = ""
        self.__hand = []
        self.__graveyard = [] #represents discard pile
        self.__battalion = list()
        self.__current_rp = 0
    #my accessor functions
    def get_score(self): #player's life points
        return self.__score
    def get_resource(self):
        return self.__resource_points
    def get_deck(self):
        return self.__deck
    def get_faction(self): #goats or trolls
        return self.__faction
    def get_hand(self):
        return self.__hand
    def get_graveyard(self): #discard pile
        return self.__graveyard
    def get_battalion(self):
        return self.__battalion
    def get_current(self): #a different approach i used to get the current amount of resource points a player
        #has to spend, rather than only using max resource points
        return self.__current_rp
    #my mutator functions
    def decrease_score(self, factor): #factor is the amount to change the score by
        self.__score -= factor
    def increase_score(self, factor):
        self.__score += factor
    def disc_from_battalion(self, card):
        taret = self.__battalion.discard(card)
        self.__graveyard.append(target)
    def disc_from_hand(self, card_index):
        target = self.__hand.remove(__hand[card_index])
        self.__graveyard.append(target)
    def increment_resource(self): #every round, this will be used to increment both
        #player's max resource points by one.
        self.__resource_points +=1
    def draw(self, hand, deck):
        popped = self.__deck.pop() #could use obj = with random integers to make it randomized
        self.__hand.append(popped)
        return self.__hand
    def play(self, hand, battalion, card_index):
        selected = self.__hand[card_index]
        self.__hand.pop(card_index)
        self.__battalion.append(selected)
    def add_to_graveyard(self,card):
        self.__graveyard.append(card)
    
    #add something here about where defeated cards should go


def refund_resource(player): #a function that will be used to refund resource points every round to both
    #players.
    player.increment_resource()
    max_resource_points = player.get_resource()
    current_resource_points = player.get_current()
    current_resource_points = max_resource_points


#Power class, responsible for managing the special abilities that could possibly be listed on a card
class Power:
    __slots__ = ["__name","__description", "__function","__single_use","__used"]
    def __init__(self, name, description, func, single_use):
        self.__name = name
        self.__description = description
        self.__function = func
        self.__single_use = single_use
        self.__used = False
    def activate(self, card, player):
        #activate power function
        if self.__single_use and not self.__used:
            self.__used = self.__function(card, player)
            return True
        elif not self.__single_use:
            self.__function(card, player)
            return True
        else:
            return False
    def set_description(self, change):
        self.__description = change
    def set_single_use(self, true_or_false):
        self.__single_use = true_or_false
    def __eq__(self, other): #check if two powers are equal to eachother
        if self.__name == other.__name and self.__power == other.__power:
            return True
        return False
power_count = 0
#function for regeneration power
def regen(card, player): #this is an example of a power function
    power_count +=1
    print("Activating regeneration on the side of player", player)
    card.set_single_use(card,False)
    new_desc = "Adds one point to the card's currnet health. The card's health cannot exceed it's max health."
    card.set_description(card, new_desc)
    if card.get_health() < card.get_max_health():
        card.change_current_health(1)
    #return True
    else:
        print("Regeneration has been canceled due to health limit.")
        #return False
#function for the power first aid


def first_aid(card,player):
    print("Activating first aid on the side of player", player)
    card.set_single_use(card, True)
    new_desc = "Adds 5 to the player's score, Player score may exceed max."
    card.set_description(card, new_desc)
    player.increase_score(5)
    power_count +=1
#between the powers avaliable, randomly select one if a card has a power
def assign_power(card, player):
    
    toss_up = random.randint(0, power_count)
    if toss_up == 0:
        card.set_power(regen)
    elif toss_up == 1:
        card.set_power(first_aid)
#class Game:
def main():
    #the main game class
    #set up both players
    p1 = Player(100, 0, "Trolls")
    p2 = Player(100, 0, "Goats")
    #__slots__ = ["__rounds", "__p1", "__p2"]
    #def __init__(self, rounds,p1,p2):
        #self.__rounds = 0
    rounds = 0
    #def main_game(self):
    while p1.get_score() > 0 or p2.get_score() > 0:
        p1_turn = True
        #while both players are still able to play, keep the game running
        rounds +=1
        if rounds == 1:
        #setup phase, happens only at the start of the game
            #both players draw 5 cards
            for _ in range(5):
                p1.draw(p1.get_hand(), p1.get_deck())
                p2.draw(p2.hand, p2.deck)
        if p1_turn == True:
            
            #execute the following series of steps if its player1's turn
            refund_resource(p1)
            if p1.deck > 0: #draw a card
                p1.draw(p1.hand, p1.deck)
            else: #print this if no cards remain in deck
                print("No cards remaining in deck. continuing to play phase.")
            #play phase
            print("Hand of player 1: ")
            print(p1.get_hand())
            play = input("Which indexes of cards would you like to play from your hand, player 1? (seperate by space) ")
            #player 1 goes first and chooses cards they want to play
            if play != "":
                split_play = play.split(" ")
                int_play = int(split_play)
                list_play = list(int_play)
                #eventually you end up with a list of cards they chose to play
                for a in list_play: #takes rp away and plays
                    card_cost = p1.get_hand[a].cost
                    if card_cost > p1.get_current(): #if you cant play the card, inform the user
                        print("Not enough RP to play the card.")
                    else:
                        play(p1.hand,p1.battalion, a)
                #end player 1 turn
                p1_turn = False
            else: #p1 skips their turn, resource for p1 is incremented, go to p2's turn
                p1.increment_resource()
                p1_turn = False

        else:
                            
            #execute the following series of steps if its player2's turn
            refund_resource(p2)
            #same documentation from p1 turn applies here
            if p2.deck > 0: #draw a card
                p2.draw(p2.hand, p2.deck)
            else: #print this if no cards remain in deck
                print("No cards remaining in deck. continuing to play phase.")
            #play phase
            print("Hand of player 2: ")
            print(p2.get_hand())
            play = input("Which indexes of cards would you like to play from your hand, player 2? (seperate by space) ")
            
            if play != "":
                split_play = play.split(" ")
                int_play = int(split_play)
                list_play = list(int_play)
                
                for a in list_play:
                    card_cost = p2.get_hand[a].get_cost()
                    if card_cost > p2.get_current():
                        print("Not enough RP to play the card.")
                    else:
                        play(p2.hand,p2.battalion, a)
                p1_turn = True
            else:
                p2.increment_resource()
                p1_turn = True
        #battle phase, for both sides
        #activate all powers for both sides on the field, after showing both player's battalions
        print("Player 1's battalion:")
        for i in range(p1.battalion):
            if p1.battalion[i].get_health() <= 0: #if a card in the battalion's health
                #is found to be 0, it is removed and sent to the graveyard
                #it also is prevented from being printed
                p1.add_to_graveyard(p1.battalion[i])
                p1.battalion.pop(i)
            card.print_card() #display all the active battalion cards


        print("Player 2's battalion:")
        for i in range(p2.battalion):
            if p2.battalion[i].get_health() <= 0:
                p2.add_to_graveyard(p2.battalion[i])
                p2.battalion.pop(i)
            card.print_card()
        #use battalion 1 and 2's powers for every card that has one
        for card in p1.battalion:
            if card.has_power() == True:
                card.use_power()
            else: #if the card doesnt have a power, keep iterating
                continue
        for card in p2.battalion:
            if card.has_power() == True:
                card.use_power()
            else:
                continue
        #phase where cards attack eachother, cards may only attack once per round.
        if len(p1.battalion) > 0:
            for i in range(p1.battalion):
                attack_target = random.randint(0, len(p2.battalion)-1)
                p1.battalion[i].attack_card(p1.battalion[i],attack_target)
                if p1.battalion[i].get_health() < 0: #remove defeated cards
                    defeated = p1.battalion[i]
                    p1.add_to_graveyard(p1.battalion[i]) #add the defeated cards to the graveyard
                    p1.battalion.pop(i)
                if p2.battalion[attack_target].get_health() < 0:
                    #do the same for the card attacked on p2's side
                    defeated = p2.battalion[attack_target]
                    p2.battalion.pop(attack_target)
                    p2.add_to_graveyard(defeated)


        #if one of the battalions is completely wiped out, attack enemy score directly
        #applies to any card that has not attacked yet
        if len(p1.battalion) == 0:
            for card in p2.battalion:
                if card.has_used_attack() == False:
                    p1.score -= card.get_attack()
                else:
                    continue
        if len(p2.battalion) == 0:
            for card in p1.battalion:
                if card.has_used_attack() == False:
                    p2.score -= card.get_attack()
                else:
                    continue
    if p1.get_score() <= 0:
        print("Player 2 has won the duel.")
    elif p2.get_score() <= 0:
        print("Player 1 has won the duel.")

    
"""       
def main():
    rounds = 0
    the_game = Game(rounds)
    the_game.main_game()
"""
    #print("\u001b[38;5;7mtestmessage")
if __name__ == "__main__":
    main()