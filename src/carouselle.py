"""
carouselle.py

So there will be potentially from 0 to 1000 images 
in a folder - each chronologically ordered.

Given:
1000 images, find the middle 11 (MAX_SIZE)

"""
import logging
from collections import deque


SIDE_BUFFER = 5
MAX_SIZE = 11          # assumes root and 5 on either side


class Carouselle:
    """Carouselle
    """
    def __init__(self):
        """
        """
        logging.info('Creating Carouselle')
        self.carouselle = deque()

    def add_to_left(self, item):
        """add to a left, remove from the right to keep the size

        Parameters:
        item - (?): the item to add

        Returns:
        n/a
        """
        if len(self.carouselle) == MAX_SIZE:
            logging.info('Removing from the right')
            self.removeright()
        self.carouselle.appendleft(item)

    def add_to_right(self, item):
        """add to a left, remove from the right to keep the size
        """
        if len(self.carouselle) == MAX_SIZE:
            logging.info('Removing from the left')
            self.removeleft()
        self.carouselle.append(item)

    def get(self):
        """get - get the middle item - this is to be displayed
        """
        logging.info('Picking the middle value.')
        if len(self.carouselle) >= 1:
            middle_pos = len(self.carouselle) // 2
        else:
            raise ValueError
        return self.carouselle[middle_pos]

    def removeleft(self):
        """Just as the function says - remove from the left.
        """
        logging.info('Removing left')
        return self.carouselle.popleft()

    def removeright(self):
        """Just as the function sys - remove from the right
        """
        logging.info('Removing right')
        return self.carouselle.pop()

    def __len__(self):
        return len(self.carouselle)

    def __str__(self):
        return str(self.carouselle)

    def __rep__(self):
        return str(self)


if __name__ == "__main__":
    x = Carouselle()
