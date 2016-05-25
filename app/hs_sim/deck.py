import random
from draw_tree import DrawTree


class Deck(object):
    def __init__(self, curve, shuffle=False):
        self.curve = curve

        self.cards = []
        self.drawn = 0

        for i in range(len(curve)):
            self.cards += ([i] * curve[i])

        if shuffle:
            self.shuffle()

        self.tree = DrawTree(self)

    @property
    def cards_remaining(self):
        return len(self.cards) - self.drawn

    def draw_card(self, number=1):
        cards = self.cards[self.drawn:self.drawn + number]

        self.drawn += number

        return cards

    def shuffle(self, iterations=300):
        def swap(a, b):
            temp = self.cards[a]
            self.cards[a] = self.cards[b]
            self.cards[b] = temp

        def random_index():
            return random.randint(self.drawn, 29)

        for _ in range(iterations):
            first = random_index()
            second = random_index()

            swap(first, second)

    def curve_graph(self):
        rows = max(self.curve)
        out_lines = []
        for row in range(rows, 0, -1):
            line = '{}|'.format(row)
            for cost in range(len(self.curve)):
                if self.curve[cost] > row:
                    line += ' # '
                elif self.curve[cost] == row:
                    line += ' {} '.format(self.curve[cost])
                else:
                    line += '   '

            out_lines.append(line)

        out_lines.append('X\--------------------------------')
        out_lines.append('   0  1  2  3  4  5  6  7  8  9 10')

        return '\n'.join(out_lines)

    def curve_summary(self):
        return ' '.join("{}:{}".format(i, self.curve[i]) for i in range(0, 11))

    def __str__(self):
        return "deck of {} cards, {} drawn, with curve: {}".format(
            len(self.cards), self.drawn, self.curve_summary())

    def __repr__(self):
        return repr(self.cards)
