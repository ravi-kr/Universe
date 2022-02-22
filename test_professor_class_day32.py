import pytest
import datetime
from day20_to_24 import CollegeMember

now = datetime.datetime.now().year

@pytest.fixture
def RS():
    return Professor.RS()

def test_correction_of_attributes_(RS):
    assert RS.name == "RS"
    assert RS.subject == "Structures"
    assert RS.department == "Civil"
    
def test_repr_output(capfd, RS):
    print(RS)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Professor(name='RS', birthyear=1980, sex='female', subject='Structures', department='Civil')"
