import pytest
from day20_to_24 import Worker
import datetime

now = datetime.datetime.now().year

@pytest.fixture
def AL():
    return Worker.AL()

def test_correctness_of_attributes_(AL):
    assert AL.name == "AL"
    assert AL.year_of_death == 1295
    
def test_age_property(AL):
    assert AL.age == (now - AL.birthyear)
    
def test_repr_output(capfd, AL):
    print(AL)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Worker(name='AL', birthyear=1201, sex='female', year_of_death=1295)"
