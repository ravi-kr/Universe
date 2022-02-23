import pytest
import datetime
from day37 import Pupil, Charm, Transfiguration, DataEngineer, DataScientist, CoreEngineer, ProductManagement, SoftwareEngineer

now = datetime.datetime.now().year

@pytest.fixture
def DoYourDeeds():
    return Charm.DoYourDeeds()

@pytest.fixture
def MakeUsGreat():
    return Charm.MakeUsGreat()

@pytest.fixture
def alteraror_DE():
    return Transfiguration.alteraror_DE()

@pytest.fixture
def make_a_de():
    return DataEngineer.make_a_de()

@pytest.fixture
def make_a_ds():
    return DataScientist.make_a_ds()

@pytest.fixture
def make_a_ce():
    return CoreEngineer.make_a_ce()

@pytest.fixture
def make_a_pm():
    return ProductManagement.make_a_pm()

@pytest.fixture
def make_a_se():
    return SoftwareEnginer.make_a_se()

@pytest.fixture
def LY():
    return Pupil.LY()

@pytest.fixture
def SJ():
    SJ = Pupil.SJ()
    SJ.add_trait('highly intelligent')
    return SJ

@pytest.fixture
def AB():
    return Pupil.AB()

@pytest.fixture
def LY_with_friends():
    LY = Pupil.LY()
    SJ = Pupil.SJ()
    LY.befriend(SJ)
    return LY

def test_correctness_of_attributes_(LY):
    assert LY.name == "LY"
    assert LY.start_year == 1994
    assert LY.pet_name == 'Marshmallo'
    assert LY.pet_type == 'rabbit'

def test_current_year_property(LY):
    assert LY.current_year == (now - LY.start_year + 1)

def test_elms_property(LY):
    assert LY._skills == {
            'Critical Thinking' : False,
            'Self-Defense' : False,
            'Driving' : False,
            'Physics' : False,
            'Arts' : False,
            'Music' : False,
            'Hard Defense' : False,
            'Strategy' : False,
            'Multi-task' : False}

def test_friends_property(LY_with_friends):
    assert LY_with_friends.friends == "LY's current friends are: ['SJ']"

def test_LY_befriend_SJ(capfd, LY, SJ):
    LY.befriend(SJ)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "SJ is now your friend!"

def test_befriend_house_AB(capfd, LY, AB):
    LY.befriend(AB)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "AB is now your friend!"

def test_delete_skills(capfd, LY):
    del LY.skills
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Caution, you are deleting this students' Skill's!\nYou should only do that if she dropped out of school without passing any exams!"
    with pytest.raises(AttributeError):
        print(LY.skills)

def test_set_skills_raises_ValueError_with_wrong_input_argument(capfd, LY):
    with pytest.raises(ValueError):
        LY.skills = 'Strategy'

def test_set_skills_with_passed_grade(capfd, LY):
    LY.skills = ("Strategy", "G")
    assert LY._skills == {
            'Critical Thinking' : False,
            'Self-Defense' : False,
            'Driving' : False,
            'Physics' : False,
            'Arts' : False,
            'Music' : False,
            'Hard Defense' : False,
            'Strategy' : True,
            'Multi-task' : False}

def test_set_skills_with_not_passed_grade(capfd, LY):
    LY.skills = ("Strategy", "H")
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == 'The exam was not passed so no skill was awarded!'
    assert LY._skills == {
            'Critical Thinking' : False,
            'Self-Defense' : False,
            'Driving' : False,
            'Physics' : False,
            'Arts' : False,
            'Music' : False,
            'Hard Defense' : False,
            'Strategy' : False,
            'Multi-task' : False}

def test_staticmethod_passed_with_passed_grades():
    assert Pupil.passed('E') == True
    assert Pupil.passed('Excellent') == True
    assert Pupil.passed('G') == True
    assert Pupil.passed('Good') == True
    assert Pupil.passed('A') == True
    assert Pupil.passed('Acceptable') == True

def test_staticmethod_passed_with_not_passed_grades():
    assert Pupil.passed('P') == False
    assert Pupil.passed('Poor') == False
    assert Pupil.passed('H') == False
    assert Pupil.passed('Horrible') == False

def test_staticmethod_passed_default_return_value():
    assert Pupil.passed('D') == False

def test_repr_output(capfd, LY):
    print(LY)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Pupil(name='LY', birthyear=1994, sex='male', start_year=2015)"

def test_learn_vocal_charm_if_being_too_young(capfd, LY, MakeUsGreat):
    LY.learn_vocal(MakeUsGreat)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "LY is too young to study this vocal!"

