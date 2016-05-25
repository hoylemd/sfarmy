import json


class BaseNode(object):
    def __init__(self, depth=0):
        self.depth = depth
        self.children = {}
        self.parent = None

    def add_child(self, node):
        node.parent = self
        self.children[node.value] = node


class DrawTreeNode(BaseNode):
    def __init__(self, value, count, choices, curve, depth=0):
        super(DrawTreeNode, self).__init__(depth)
        self.value = value
        self.count = count
        self.choices = choices

        self.curve = curve

    @property
    def probability(self):
        return float(self.count) / float(self.choices)

    def create_children(self, depth=0):
        self.children = {}
        choices = sum(self.curve)
        child_depth = self.depth + 1

        print "Adding children to {}:".format(str(self))
        for cost in range(len(self.curve)):
            if self.curve[cost]:
                new_curve = self.curve[:]
                new_curve[cost] -= 1

                node = DrawTreeNode(cost, self.curve[cost], choices, new_curve,
                                    child_depth)

                self.add_child(node)

        print "  {}".format(
            ', '.join(child.short_str for _, child in self.children.items()))

        if depth:
            print "Generating entire next generation ({})".format(child_depth)
            for cost in self.children:
                self.children[cost].create_children(depth - 1)

    def __str__(self):
        return ("Node: {} cost, {} possible draws of {} cards in deck"
                .format(self.value, self.count, self.choices))

    def dict(self, recursive=False):
        struct = {
            'value': self.value,
            'count': self.count,
        }

        if recursive:
            struct['children'] = []
            for _, child in self.children.items():
                struct['children'].append(child.dict(recursive))

        return struct

    @property
    def short_str(self):
        return "{} {}s".format(self.count, self.value)


class DrawTree(DrawTreeNode):
    def __init__(self, deck):
        self.deck = deck
        super(DrawTree, self).__init__(0, 0, 0, deck.curve)

    def build_tree(self, depth=3):
        self.create_children(depth)

    def __str__(self):
        return "Deck tree: {}".format(self.deck.curve)

    def dump(self):
        struct = self.dict(True)
        struct['deck'] = repr(self.deck)

        return json.dumps(struct)
