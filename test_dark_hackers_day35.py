
import pytest
from day29_to_31 import DarkHackers, Charm 

@pytest.fixture
def task_hacker():
    task_hacker = DarkHackers("task_hacker", 1990)
    return task_hacker

@pytest.fixture
def master_hacker():
    master_hacker = DarkHackers("master_hacker", 1985)
    return master_hacker

@pytest.fixture
def do_your_deeds():
    return Charm.DoYourDeeds()

def test_correctness_of_attributes_(task_hacker):
    assert task_hacker.name == "task_hacker"
    assert AL.birth_year == 1990
    
def test_leader_property(task_hacker, master_hacker):
    assert task_hacker.leader == master_hacker
    
def test_repr_output(capfd, task_hacker):
    print(task_hacker)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "DarkHackers(name='task_hacker', birthyear=1990)"
    
def test_cast_vocab(task_hacker, do_your_deeds):
    assert task_hacker.cast_vocab(do_your_deeds) == "task_hacker: Do your deeds!"
