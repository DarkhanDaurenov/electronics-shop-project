from src.item import Item

class Mixinboard:
    _language = "EN"

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value.upper()

    def change_lang(self):
        if self._language == 'RU':
            self._language = 'EN'
        else:
            self._language = 'RU'
        return self._language

class Keyboard(Item, Mixinboard):
    """Дочерний класс для добавления товара"""

    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self._language = language






