"""This lass dictates the program's reaction to user input"""


class Action:
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        raise NotImplementedError

    def mod_db(self, *args, **kwargs):
        """Specify how db is modified when the action is taken"""
        raise NotImplementedError