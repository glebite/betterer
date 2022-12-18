"""
carouselle.py

So there will be potentially from 0 to 1000 images 
in a folder - each chronologically ordered.
"""
import logging
from collections import deque


SIDE_BUFFER = 5


class Carouselle:
    """
    """
    def __init__(self):
        """
        """
        logging.info('Creating Skeleton')
        self.carouselle = deque()

    def add_to_left(self, item):
        """add
        """
        logging.info(f'Adding {item=}')
        self.carouselle.appendleft(item)

    def add_to_right(self, item):
        """add
        """
        logging.info(f'Adding {item=}')
        self.carouselle.appendleft(item)

    def get(self):
        """get - get the middle item - this is to be displayed
        """
        middle_pos = len(self.carouselle) / 2
        return self.carouselle[middle_pos]

    def removeleft(self):
        """
        """
        logging.info('Removing left')
        return self.carouselle.popleft()

    def removeright(self):
        """
        """
        logging.info('Removing right')
        return self.carouselle.pop()

    def __len__(self):
        return len(self.carouselle)


if __name__ == "__main__":
    x = Carouselle()
