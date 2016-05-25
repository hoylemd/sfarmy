from card import Card, save_abilities
from utils import write_to_json_file, read_from_json_file


if __name__ == '__main__':
    spec_list = None

    spec_list = read_from_json_file('cards.json')

    cards = [Card(**card_spec) for card_spec in spec_list]

    for card in cards:
        print str(card)

    save_abilities()

    card_list = [card.serialize() for card in cards]

    write_to_json_file(card_list, 'cards.json')
