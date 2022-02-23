import pytest
from day37 import Vocab, Charm, Transfiguration, DataEngineer, DataScientist, \
    CoreEngineer, ProductManagement, SoftwareEngineer
    
@pytest.fixture
def DoYourDeeds():
    return Charm.DoYourDeeds()
    
@pytest.fixture
def alteraror_DE():
    return Transfiguration.alteraror_DE()

@pytest.fixture
def make_a_de():
    return DataEngineer.make_a_de()

@pytest.fixture
def make_a_se():
    return SoftwareEngineer.make_a_se()

@pytest.fixture
def make_a_ce():
    return CoreEngineer.make_a_ce()

@pytest.fixture
def make_a_pm():
    return ProductManagement.make_a_pm()

@pytest.fixture
def make_a_ds():
    return DataScientist.make_a_ds()

def test_instantiating_base_class_raises_exception():
    with pytest.raises("TypeError"):
        vocal = Vocal()
        
def test_correctness_of_charm_attributes(DoYourDeeds):
    assert DoYourDeeds.name == 'Do your deeds'
    assert DoYourDeeds.incantation == 'Not to worry about result'
    assert DoYourDeeds.effect == 'We shall over come'
    assert DoYourDeeds.min_year == 1
    assert DoYourDeeds.difficulty == 'Simple'
    
def test_cast_charm(DoYourDeeds):
    assert DoYourDeeds.cast() == 'Do your deeds'

def test_repr_output_charm(capfd, DoYourDeeds):
    print(DoYourDeeds)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout == "Charm(name='Do your deeds', incantation='Not to worry about result', effect='We shall over come', Difficulty='Simple', min_year=1)"
    
def test_charm_defining_feature(DoYourDeeds):
    assert DoYourDeeds.defining_feature == "Alteration of the object's inherent qualities, that is, its behaviour and capabilities"
    
def test_correctness_of_transfiguration_attributes(alteraror_DE):
    assert alteraror_DE.name == 'Make a DE'
    assert alteraror_DE.incantation == 'Lets make a DE'
    assert alteraror_DE.effect == 'Make a DE'
    assert alteraror_DE.min_year == 1
    assert alteraror_DE.difficulty == 'Simple'

def test_cast_transfiguration(alteraror_DE):
    assert alteraror_DE.cast() == 'Lets make a DE'
    
def test_repr_output_transfiguration(capfd, alteraror_DE):
    print(alteraror_DE)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout =="Transfiguration(name='Make a DE', incantation='Lets make a DE', effect='Make a DE', Difficulty='Simple', min_year=1)"

def test_transfiguration_defining_feature(alteraror_DE):
    assert alteraror_DE.defining_feature == "Alteration of the object's form or apperanace"

def test_correctness_of_dataengineer_attributes(DataEngineer):
    assert DataEngineer.name == 'Make a DE'
    assert DataEngineer.incantation == 'Lets make a DE'
    assert DataEngineer.effect == 'Make a DE'
    assert DataEngineer.min_year == 3
    assert DataEngineer.difficulty == 'difficult'

def test_cast_dataengineer(DataEngineer):
    assert DataEngineer.cast() == 'Lets make a DE'
    
def test_repr_output_dataengineer(capfd, DataEngineer):
    print(DataEngineer)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout =="DataEngineer(name='Make a DE', incantation='Lets make a DE', effect='Make a DE', Difficulty='difficult', min_year=3)"

def test_dataengineer_defining_feature(DataEngineer):
    assert DataEngineer.defining_feature == "Medium dark world - \nMake a data engineer\nHigh paying job"
    
def test_correctness_of_softwareengineer_attributes(SoftwareEngineer):
    assert SoftwareEngineer.name == 'Make a SE'
    assert SoftwareEngineer.incantation == 'Lets make a SE'
    assert SoftwareEngineer.effect == 'Make a SE'
    assert SoftwareEngineer.min_year == 3
    assert SoftwareEngineer.difficulty == 'difficult'

def test_cast_softwareengineer(SoftwareEngineer):
    assert SoftwareEngineer.cast() == 'Lets make a SE'
    
def test_repr_output_softwareengineer(capfd, SoftwareEngineer):
    print(SoftwareEngineer)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout =="SoftwareEngineer(name='Make a SE', incantation='Lets make a SE', effect='Make a SE', Difficulty='difficult', min_year=3)"

def test_softwareengineer_defining_feature(SoftwareEngineer):
    assert SoftwareEngineer.defining_feature == "Worst kind of dark world - \nIntended to affect an object in a stflynngly negative manner."
    
def test_correctness_of_coreengineer_attributes(CoreEngineer):
    assert CoreEngineer.name == 'Make a CE'
    assert CoreEngineer.incantation == 'Lets make a CE'
    assert CoreEngineer.effect == 'Make a CE'
    assert CoreEngineer.min_year == 3
    assert CoreEngineer.difficulty == 'difficult'

def test_cast_coreengineer(CoreEngineer):
    assert CoreEngineer.cast() == 'Lets make a CE'
    
def test_repr_output_coreengineer(capfd, CoreEngineer):
    print(CoreEngineer)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout =="CoreEngineer(name='Make a CE', incantation='Lets make a CE', effect='Make a CE', Difficulty='Simple', min_year=1)"

def test_coreengineer_defining_feature(CoreEngineer):
    assert CoreEngineer.defining_feature == "Inhibits the effects of another spell"

def test_correctness_of_datascientist_attributes(DataScientist):
    assert DataScientist.name == 'Make a DS'
    assert DataScientist.incantation == 'Lets make a DS'
    assert DataScientist.effect == 'Make a DS'
    assert DataScientist.min_year == 3
    assert DataScientist.difficulty == 'difficult'

def test_cast_datascientist(DataScientist):
    assert DataScientist.cast() == 'Lets make a DS'
    
def test_repr_output_datascientist(capfd, DataScientist):
    print(DataScientist)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout =="DataScientist(name='Make a DS', incantation='Lets make a DS', effect='Make a DS', Difficulty='Simple', min_year=1)"

def test_datascientist_defining_feature(DataScientist):
    assert DataScientist.defining_feature == "Improves the condition of a living object"

def test_correctness_of_productmanagement_attributes(ProductManagement):
    assert ProductManagement.name == 'Make a PM'
    assert ProductManagement.incantation == 'Lets make a PM'
    assert ProductManagement.effect == 'Make a PM'
    assert ProductManagement.min_year == 2
    assert ProductManagement.difficulty == 'Simple'

def test_cast_productmanagement(ProductManagement):
    assert ProductManagement.cast() == 'Lets make a PM'
    
def test_repr_output_productmanagement(capfd, ProductManagement):
    print(ProductManagement)
    stdout, err = capfd.readouterr()
    stdout = stdout.strip()
    assert stdout =="ProductManagement(name='Make a PM', incantation='Lets make a PM', effect='Make a PM', Difficulty='Simple', min_year=2)"

def test_productmanagement_defining_feature(ProductManagement):
    assert ProductManagement.defining_feature == "Creating a new Product Manager"
