from clothing import ClothingItem

class Closet:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        if not isinstance(item, ClothingItem):
            raise TypeError("Only clothing items can go in the closet")
        self._items.append(item)

    def get_items(self):
        return list(self._items)

    def is_empty(self):
        return len(self._items) == 0