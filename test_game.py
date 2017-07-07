from eye_game import EyeGamePage
from collections import namedtuple
import pytest


Level = namedtuple("Level", ['name','value'])

ROBOT = Level(name='ROBOT', value = 30)
JASTRZAB = Level(name='JASTRZAB', value = 25)

@pytest.mark.parametrize("level", [JASTRZAB,ROBOT])

def test_kret_level(driver,level):
    eye_game = EyeGamePage(driver)
    eye_game.load()
    #eye_game.click_chosenone()
    eye_game.get_to_robot_level()
    assert eye_game.get_reached_level() == 'ROBOT'


