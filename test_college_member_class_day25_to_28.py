import pytest
from day20_to_24 import CollegeMember
import datetime

now = datetime.datetime.now().year

@pytest.fixture
def RK():
    RK = CollegeMember('RK', 1995, 'male')
    return RK

@pytest.fixture
def RK_with_traits():
    RK = CollegeMember('RK', 1995, 'male')
    RK.add_trait('kind')
    RK.add_trait('wild')
    RK.add_trait('mean', False)
    return RK

def test_correctness_of_attributes_(RK):
    assert RK.name == 'RK'
    assert RK.birthyear == 1995
    assert RK.sex == 'male'
    
def test_add_positive_traits(RK):
    RK.add_trait('kind')
    RK.add_trait('wild')
    assert RK._traits == {'kind': True, 'wild': True}
    
def test_add_negative_traits(RK):
    RK.add_trait('mean', False)
    
def test_exhibit_traits(RK_with_traits):
    assert RK_with_traits.exhibits_traits('kind') == True
    assert RK_with_traits.exhibits_traits('mean') == False
    assert RK_with_traits.exhibits_traits('smart') == False
    
def test_print_traits(capfd, RK_with_traits):
    RK_with_traits.print_traits()
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'RK is kind, wild. \n RK is not mean.'

def test_init_raises_exception_with_missing_arguments():
    with pytest.raises(TypeError):
        RK = CollegeMember()
        
def test_says(RK):
    assert RK.says('Hi PG!') == 'RK says : Hi PG!'
    
def test_name_property(RK):
    assert RK.name == 'RK'
    
def test_age_property(RK):
    assert RK.age == (now - RK.birthyear)
    
def test_repr_output(capfd, RK):
    print(RK)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "CollegeMember(name='RK', birthyear=1995, sex='male')"
    
