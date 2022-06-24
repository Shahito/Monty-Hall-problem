# imports
from random import choice

class Door:
    """Door class, describe door attributes
    """
    def __init__(self) -> None:
        """init all door object attr
        """
        self.hide_price=False
        self.is_open=False
        self.is_chosen=False

class Game:
    """Define game object
    """
    def __init__(self) -> None:
        """Only attr is three door object
        """
        self.doors=[Door(),Door(),Door()]
    
    def set_random_price(self):
        """Randomly choose one door to hide the price
        """
        choice(self.doors).hide_price=True
    
    def choose_door(self):
        """Randomly choose one door (simulate user choice)
        """
        choice(self.doors).is_chosen=True

    def change_chosen_door(self):
        """Change chosen door (avoid choosing an open door)
        """
        for dr in [d for d in self.doors if d.is_open!=True]:
            if dr.is_chosen: dr.is_chosen=False
            else: dr.is_chosen=True
    
    def open_empty_door(self):
        """Look for and open a empty door (neither the chosen door nor the open door)
        """
        choice([d for d in self.doors if d.hide_price!=True and d.is_chosen!=True]).is_open=True
    
    def get_result(self):
        """Return if the user win the game

        Returns:
            bool: True if win, False if defeat
        """
        for d in self.doors:
            if d.is_chosen and d.hide_price: return True
        return False
