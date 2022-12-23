"""test_carouselle.py

Write tests first, make the code work later.
"""
import pytest
import logging
import carouselle


LONG_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,  15, 16]
SHORT_LIST = [1, 2, 3]
EMPTY_LIST = []
ONE = 1
TWO = 2


@pytest.fixture()
def create_carouselle():
    logging.info("SETUP")
    deck = carouselle.Carouselle()
    yield deck
    logging.info("TEARDOWN")
    del deck


def test_create_carouselle(create_carouselle):
    obj = create_carouselle
    assert obj is not None, 'Could not instantiate Carouselle object'


def test_add_carouselle(create_carouselle):
    obj = create_carouselle
    obj.add_to_right('hi')
    length = len(obj)
    assert length == ONE, f'expecting {ONE}, got {length=}'


def test_add_more(create_carouselle):
    obj = create_carouselle
    obj.add_to_right('hi')
    obj.add_to_right('hi')    
    length = len(obj)
    assert length == TWO, f'expecting {TWO}, got {length=}'


def test_add_one_more():
    pytest.skip()    


def test_cycle_one_hundred(create_carouselle):
    obj = create_carouselle
    for count in range(1, 100):
        obj.add_to_left(count)        
        if count <= 10:
            assert len(obj) == count
        else:
            assert len(obj) == 11


def test_remove_one():
    pytest.skip()


def test_len_zero(create_carouselle):
    obj = create_carouselle
    assert len(obj) == 0, f'Len of object {len(obj)} not equal 0'


def test_get_success(create_carouselle):
    obj = create_carouselle
    obj.add_to_left(1)
    obj.add_to_left(2)
    obj.add_to_left(3)
    assert obj.get() == 2, f'got unexpected value: {obj.get}'
