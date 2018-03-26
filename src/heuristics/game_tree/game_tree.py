class GameTree:
    def __init__(self, obj):
        self.data = obj
        self.parent = None
        self.child = None
        self.children = []
        self.move_sequence = []
        self.move_count = 0
        self.child_move_count = 9999

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
