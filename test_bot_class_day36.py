import pytest
from day29_to_31 import Bot

@pytest.fixture
def moon_bot():
    return Bot(['engine class land', 'wheels class land', \
                'frame class land', 'power supply class land'\
                    , 'processor class land'])

@pytest.fixture
def air_bot():
    return Bot(['engine class air', 'wheels class air', \
                'frame class air', 'power supply class air'\
                    , 'processor class air'])

def test_iterator_behaviour(air_bot):
    all_components = [component for component in air_bot]
    assert all_components == ['engine class air', 'wheels class air', 'frame class air', 'power supply class air', 'processor class air']
