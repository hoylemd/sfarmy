from deck import Deck
from game import Game


def simulate_short_game(turns=10):
    print "initializing deck..."
    curve = [2, 2, 4, 4, 5, 4, 4, 2, 1, 1, 1]
    deck = Deck(curve)
    deck.shuffle()
    print deck

    game = Game(deck)
    game.set_up()

    for i in range(turns):
        turn_number = i + 1
        play, metrics = game.take_turn()
        print "Simulating turn {}...".format(turn_number)

        print "Results:".format(turn_number)
        print "  Hand: {}".format(game.cards_in_hand),
        if play.coin:
            print ", with coin."
        else:
            print '.'
        print "  Played {} cards this turn: {}, for a total of {}.".format(
            play.cards, play.played, metrics['cards'])
        if play.hero_power:
            print "  Hero Power used."
        print "  Mana: {}/{} wasted this turn, for a total of {}.".format(
            play.mana, turn_number, metrics['mana'])
        if play.missed_drop and turn_number < 11:
            print "  Missed the {} drop!".format(turn_number)

    print "Final Summary"
    print "=" * 80
    print "Turns taken: {}".format(turns)
    print "Cards played: {}".format(metrics['cards'])
    total_mana = (turns + 1) * (turns / 2)
    print "Mana wasted: {}/{}".format(metrics['mana'], total_mana)
    print "Times used Hero Power: {}".format(metrics['hero_power'])
    if metrics['missed_drops']:
        missed_string = ', '.join(str(d) for d in metrics['missed_drops'])
    else:
        missed_string = 'None!'
    print "Drops missed: {}".format(missed_string)


if __name__ == '__main__':
    curve = [2, 2, 4, 4, 5, 4, 4, 2, 1, 1, 1]
    deck = Deck(curve)
