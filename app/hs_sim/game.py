import random


class TurnResult(object):
    def __init__(self, hand=[], mana=0, cards=0, played=[], coin=False,
                 hero_power=True, drawn_card=None):
        missed_drop = False
        if cards == 0 or mana > 0:
            missed_drop = True

        if hero_power and mana < 2:
            hero_power = False
        else:
            mana -= 2

        self.hand = hand
        self.mana = mana
        self.cards = cards
        self.played = played
        self.missed_drop = missed_drop
        self.coin = coin
        self.hero_power = hero_power
        self.drawn_card = drawn_card


def compare_plays(first, second):
    saved_mana = second.mana - second.mana
    extra_cards = second.cards - first.mana

    if saved_mana > extra_cards * 2:
        return second

    if first.missed_drop and not second.missed_drop:
        return second

    return first


def curve_to_cards(curve):
    chunks = []
    for mana, number in zip(range(len(curve) + 1), curve):
        if number:
            cards = [str(mana)] * number
            chunks.append(', '.join(cards))

    return ', '.join(chunks)


class Game(object):
    def __init__(self, deck, coin=False, plays=None):
        self.deck = deck
        self.coin = coin

        self.hand = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.turn = -1

        self.metrics = {
            'cards': 0,
            'mana': 0,
            'hero_power': 0,
            'missed_drops': []
        }

        if plays:
            self.set_up(coin)
            self.plays = plays
            for play in plays:
                self.take_turn(play)

        else:
            self.plays = []

    def draw_cards(self, cards):
        drawn = self.deck.draw_card(cards)

        for card in drawn:
            self.hand[card] += 1

        return self.hand

    def draw_card(self):
        return self.draw_cards(1)

    def set_up(self, coin=False):

        self.draw_cards(3)

        if not coin and random.random() < 0.5:
            coin = True
            self.coin = True
            self.draw_card()

        self.turn = 0

    def find_most_efficient_play(self, hand=None, cards=0, played=[],
                                 coin=False):
        if hand is None:
            hand = self.hand[:]
        mana = self.turn - sum(played)
        if coin:
            mana += 1

        best_play = None
        for i in range(mana, -1, -1):
            if i < len(hand) and hand[i]:  # coordination
                next_hand = hand[:]
                next_hand[i] -= 1
                next_played = played[:]
                next_played.append(i)
                new_play = self.find_most_efficient_play(next_hand,
                                                         cards + 1,
                                                         next_played)

                if best_play is None:
                    best_play = new_play
                    continue

                best_play = compare_plays(best_play, new_play)

        return best_play or TurnResult(hand, mana, cards, played, coin)

    def take_turn(self):
        self.turn += 1
        self.draw_card()

        if self.turn < len(self.plays):
            play = self.plays[self.turn]

        else:
            play = self.find_most_efficient_play()

            if self.coin:
                coin_play = self.find_most_efficient_play(coin=True)
                best = compare_plays(play, coin_play)
                if best == coin_play:
                    self.coin = False
                    play = best

            self.plays.append(play)

        self.hand = play.hand

        self.metrics['cards'] += play.cards
        self.metrics['mana'] += play.mana
        if play.missed_drop:
            self.metrics['missed_drops'].append(self.turn)
        if play.hero_power:
            self.metrics['hero_power'] += 1

        return play, self.metrics

    @property
    def cards_in_hand(self):
        return curve_to_cards(self.hand)
