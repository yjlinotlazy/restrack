"""The menu class. It maintains definition of a menu and methods to navigate
through it"""


import pickle
from restrack.action import Action


class Menu:
    def __init__(self, items, conn):
        """
        Parameters
        ----------
        items : list of str
            named items in the menu
        conn
            database connection
        """
        self.items = None
        self.add_items(items)
        self.conn = conn

    def display(self):
        """display items in the right order"""
        raise NotImplementedError

    def parse_option(self, *args, **kwargs):
        """Perform action based on option"""
        raise NotImplementedError

    def add_items(self, items):
        for i in items:
            self.add_item(i)

    def add_item(self, item, action):
        """
        Add an item to the menu
        Parameters
        ----------
        item : str
            name of the item
        action : Action
            action to be taken when this item is selected
        Returns
        -------
            int : the number of the item
        """
        raise NotImplementedError

    def remove_item(self, item):
        """Remove item of the given name"""
        raise NotImplementedError