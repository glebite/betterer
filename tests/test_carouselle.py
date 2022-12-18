"""test_carouselle.py

Write tests first, make the code work later.
"""
import pytest
import logging
import carouselle


LONG_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,  15, 16]
SHORT_LIST = [1, 2, 3]
EMPTY_LIST = []


@pytest.fixture()
def create_carouselle():
    logging.info("SETUP and TEARDOWN")
    deck = carouselle.Carouselle()
    yield deck
    del deck


def test_create_carouselle(create_carouselle):
    obj = create_carouselle
    assert obj is not None, 'Could not instantiate Carouselle object'


def test_add_carouselle(create_carouselle):
    obj = create_carouselle
    obj.add_to_right('hi')
    length = len(obj)
    assert length == 1, f'expecting 1, got {length=}'


def test_add_more():
    pytest.skip()


def test_add_one_more():
    pytest.skip()    


def test_cycle_one_hundred():
    pytest.skip()


def test_remove_one():
    pytest.skip()    
