from __future__ import annotations
from typing import Tuple, NamedTuple
import datetime
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass

class CollegeMember:
    """Creates a member of the College of Engineering (COE)"""
    location: str = "India"
    def __init__(self, name: str, birthyear: int, sex: str):
        self.name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}
    
    def whisper(function):
        def wrapper(self, *args):
            original_output = function(self, *args)
            first_part, words = original_output.split(' says: ')
            words = words.replace('!', '.')
            new_output = f'{first_part} whispers: {words}..'
            return new_output
        return wrapper
    
    def write_letter(self, recipient, content):
        letter_name = f"dear_{recipient}.txt"
        with Letter(letter_name) as l:
            l.write(content)
    
    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}',"
                f"birthyear={self.birthyear},sex='{self.sex}')")
    
    @property
    def age(self) -> int:
        now = datetime.datetime.now().year
        return now - self.birthyear
    
    @whisper
    def says(self, words) -> str:
        return f"{self.name} says: {words}."
    
    
    @classmethod
    def CollegeHOD(cls) -> CollegeMember:
        return cls('KK', 1970, 'female')
    

    def add_trait(self, trait: str, value = True):
        self._traits[trait] = value
        

    def print_traits(self):
        true_traits = [trait for trait, value in self._traits.items() if value]
        false_traits = [trait for trait, value in self._traits.items() if not value]
        
        if true_traits:
            print(f"{self.name} is {', '.join(true_traits)}")
        if false_traits:
            print(f"{self.name} is not {', '.join(false_traits)}")
        
        if (not true_traits and not false_traits):
            print(f"{self.name} does not have traits yet")


    def exhibits_trait(self, trait: str) -> bool:
        try:
            value = self._traits[trait]
            return value
        except KeyError as e:
            print(f"{self.name} does not have a character trait with the name {e}")
            return False

@dataclass(frozen = True)
class DarkHackers():
    """"Creates a member of Dark Hackers"""
    name: str
    birthyear: str
    
    @property
    def leader(self):
        master_hacker = DarkHackers('master_hacker', 1970)
        return master_hacker
    
    def cast(self, vocab):
        print(f"{self.name}: {spell.incantation}!")


class Letter:
    total_number_of_letters = 0
    def __init__(self, letter_name):
        self.letter_name = letter_name
    
    def __enter__(self):
        self.letter = open(self.letter_name, 'w')
        self.__class__.total_number_of_letters += 1
        return self.letter
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.letter:
            self.letter.close()
        
        
class Pupil(CollegeMember):
    """Creates a College Pupil"""
    def __init__(self, name: str, birthyear: int, sex: str, start_year: int, pet: Tuple[str, str] = None):
        super().__init__(name, birthyear, sex)
        self.start_year = start_year
        self.known_vocabs = set()
        
        if pet is not None:
            self.pet_name, self.pet_type = pet
            
        self._skills = {
            'Critical Thinking' : False,
            'Self-Defense' : False,
            'Driving' : False,
            'Physics' : False,
            'Arts' : False,
            'Music' : False,
            'Hard Defense' : False,
            'Strategy' : False,
            'Multi-task' : False
            }
        
        self._friends = []
 
    def learn_vocab(self, vocab):
        """Allows a pupil to learn a vocab, given that he/she is old enough"""
        if vocab.min_year is not None:
            if self.current_year >= vocab.min_year:
                print(f"{self.name} now knows vocab {vocab.name}")
                self.known_vocabs.add(vocab)
            elif self.exhibits_traits('highly intelligent'):
                print(f"{self.name} now knows vocab {vocab.name}")
                self.known_vocabs.add(vocab)
            elif self.current_year < vocab.min_year:
                print(f"{self.name} is too young to study this vocab!")
        elif vocab.__class__.__name__ in ['Java', 'Python', 'C++']:
            if self.exhibits_trait('Hacker'):
                print(f"{self.name} now knows vocab {vocab.name}")
                self.known_vocabs.add(vocab)
            else:
                print(f"Are you really interested in Open information?!")
        else:
            print(f"{self.name} now knows vocab {vocab.name}")
            self.known_vocabs.add(vocab)
            
    def cast_vocab(self, vocab):
        if vocab.__class__.__name__ == 'Java':
            print(f"This is a dark world - stay away from performing dark actions.")
            
        elif vocab.__class__.__name__ == 'C++':
            if not self.exhibits_trait('Hacker'):
                print(f"You shouldn't perform hacking, that's mean!")
                
        elif vocab in self.known_vocabs:
            print(f"{self.name} : {vocab.incantation}!")
            
        elif vocab.name not in self.known_vocabs:
            print(f"You can't cast the {vocab.name} vocab correctly ",
                  f"You have to study it first")
    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name ='{self.name}',"
                f"{self.birthyear}, sex = '{self.sex}',"
                f"start_year={self.start_year})")
    
    @property
    def skills(self):
        return self._skills
        
    @staticmethod
    def passed(grade):
        """
        Given a grade, determine if an exam was passed.
        """
        grades = {
                'E': True,
                'Excellent': True,
                'G': True,
                'Good': True,
                'A': True,
                'Acceptable': True,
                'P': False,
                'Poor': False,
                'H': False,
                'Horrible': False
                }
            
        return grades.get(grade, False)

    def befriend(self, person):
        """
        Adds another person to your list of friends
        """
        self._friends.append(person)
        print(f"{person.name} is now your friend!")
            
            
    @property
    def current_year(self) -> int:
        now = datetime.datetime.now().year
        return now - self.start_year
        
    @property
    def friends(self):
        return f"{self.name}'s current Friends are: {[person.name for person in self._friends]}"
        
    @skills.setter
    def skills(self, subject_and_grade):
        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError("Pass an iterable with two items: subject and grade")
            
        passed = self.passed(grade)
        
        if passed:
            self._skills[subject] = True
                
        else:
           print("The exam was not passed so no skills were awarded!")
                
    @skills.deleter
    def skills(self):
        print("Caution, you are deleting this students' Skill's!"
              "You should only do that if she dropped out of school without passing any exams!")
        
        del self._skills
        
        
        
    @classmethod
    def LY(cls):
        return cls('LY', 1994, 'male', 2015, ('Marshmallo', 'rabbit'))
    
        
    @classmethod
    def SJ(cls):
        return cls('SJ', 2000, 'female', 2019, ('Tea', 'deer'))
        
    @classmethod
    def AB(cls):
        return cls('AB', 1997, 'female', 2016, ('KitKat', 'cat'))
        
    @classmethod
    def PG(cls):
        return cls('PG', 1996, 'female', 2015, ('Cookie', 'dog'))
        
    @classmethod
    def MP(cls):
        return cls('MP', 1993, 'male', 2014, ('Cocoa', 'dog'))
    
    @staticmethod
    def passed(grade):
        """
        Given a grade, determine if an exam was passed.
        """
        grades = {
                'E': True,
                'Excellent': True,
                'G': True,
                'Good': True,
                'A': True,
                'Acceptable': True,
                'P': False,
                'Poor': False,
                'H': False,
                'Horrible': False
                }
            
        return grades.get(grade, False)
 
     
class Professor(CollegeMember):
    """Creates a College Professor"""
    def __init__(self, name: str, birthyear: int, sex: str, subject: str, department: str):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        self.department = department

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}',"
                f"birthyear={self.birthyear}, sex='{self.sex}',"
                f"subject='{self.subject}')")
        
    @classmethod
    def RS(cls):
        return cls('RS', 1980, 'female', 'Structures', 'Civil')
    
    @classmethod
    def SS(cls):
        return cls('SS', 1970, 'female', 'Data', 'Mathematics')
    
    @classmethod
    def JB(cls):
        return cls('JB', 1965, 'male', 'Weapons', 'Defense')
    
    @classmethod
    def HS(cls):
        return cls('HS', 1995, 'male', 'Corporate Law', 'Law')
        
class Worker(CollegeMember):
    """Creates a College Worker"""
    def __init__(self, name: str, birthyear: int, sex: str, year_of_death: int):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death
        
    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear
    
    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}',"
                f"birthyear = {self.birthyear}, sex = '{self.sex}',"
                f"year_of_death={self.year_of_death})")
    
    @classmethod
    def AL(cls):
        return cls('AL', 1201, 'female', 1295)
    
    @classmethod
    def PZ(cls):
        return cls('PZ', 1970, 'female', 1989)
    
    @classmethod
    def FL(cls):
        return cls('FL', 1998, 'male', 2018)
    
    @classmethod
    def CC(cls):
        return cls('CC', 2001, 'female', 2022)

@dataclass
class Department:
    """Creates a college Department"""
    name: str
    head: Professor
    worker: Worker
    founded_in: int = 1900
    
    def current_age(self):
        now = datetime.datetime.now().year
        return (now - self.founded_in) + 1

class Vocab(ABC):
    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = "Simple", min_year: int = 1):
        self.name = name
        self.incantation = incantation
        self.effect = effect
        self.difficluty = difficulty
        self.min_year = min_year
        
    @abstractmethod
    def cast(self):
        pass
    
    @property
    @abstractmethod
    def defining_feature(self):
        pass
    
    def __repr__(self):
        return(f"{self.__class__.__name__}(name='{self.name}', incantation = '{self.incantation}', effect = '{self.effect}', difficulty = '{self.difficulty}',min_year = '{self.min_year}')")
    

    
class Charm(Vocab):
    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = "Simple", min_year: int = 1):
        super().__init__(name, incantation, effect)
        self.difficulty = difficulty
        self.min_year = min_year
        
    @property
    def defining_feature(self) -> str:
        return ("Alteration of the object's inherent qualities, that is, its behaviour and capabilities")
        
    def cast(self):
        print(f"{self.incantation}")
            
    @classmethod
    def DoYourDeeds(cls):
        return cls('Do your deeds', 'Not to worry about result', 'We shall over come')
        
    def __repr__(self):
        return f"{self.__class__.__name__}({self.incantation}, {self.difficulty}, {self.effect})"

class Transfiguration(Vocab):
    """ Creates a transfiguration - vocab that alters the form or appearance of an object"""
    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)
        
    @property
    def defining_feature(self):
        return("Alteration of the object's form or apperanace")
    
    def cast(self):
        pass
    
class ProductManagement(Vocab):
    """Creates a Product Manager -  a vocab whose effects are irritating but amusing"""
    def __init__(self, name: str, incantation: str, effect: str, min_year: int = 2):
        super().__init__(name, incantation, effect)
        self.min_year = min_year
        
    @property
    def defining_feature(self):
        return("Creating a new Product Manager")
    
    def cast(self):
        pass
    
class DataEngineer(Vocab):
    """Creates a Data Engineer - a vocab that affects an object in negative manner"""
    def __init__(self, name: str, incantation: str, effect: str, min_year: int = 3):
        super().__init__(name, incantation, effect)
        self.min_year = min_year
        
    @property
    def defining_feature(self):
        return("Medium dark world - "
               "Make a data engineer"
               "High paying job")
    
    def cast(self):
        pass
    
class SoftwareEngineer(Vocab):
    """Creates a Software Engineer - a vocab that affects an object in a stflynngly negative manner"""
    def __init__(self, name: str, incantation: str, effect: str, difficulty):
        super().__init__(name, incantation, effect)
    
    @property
    def defining_feature(self):
        return("Worst kind of dark world - "
               "Intended to affect an object in a stflynngly negative manner.")

    def cast(self):
        pass

class CoreEngineer(Vocab):
    """Creates a Core Engineer - a vocab that effects of another vocab"""
    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)
         
    @property
    def defining_feature(self):
        return("Inhibits the effects of another spell")
    
    def cast(self):
        pass
    
class Bot:
    """Creates a bot"""
    def __init__(self, components):
        self.components = components
        self.counter = -1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.counter += 1
        
        if self.counter == len(self.components):
            raise StopIteration
            
        return self.components[self.counter]
            

class DataScientist(Vocab):
    """Creates a data scientist - a vocab that improves the condition of a living object"""
    
    def __init__(self, name: str, incantation: str, effect: str):
        super().__init__(name, incantation, effect)
        
    @property
    def defining_feature(self):
        return("Improves the condition of a living object")
    
    def cast(self):
        pass

def main():
    # SS = CollegeMember(name = "SS", birthyear = 1985, sex = 'female')
    # SS.add_trait("kind")
    # SS.add_trait("tidy-minded")
    # SS.add_trait("impatient", value = False)
    
    # SS.print_traits()
    # print()
    
    # SS.exhibits_trait("kind")
    # SS.exhibits_trait("funny")
    #DC = Pupil(name = "DC", birthyear = 1998, sex = 'female', start_year = 2017)
    #AB = Pupil.AB()
    #RS = Professor.RS()
    #LY = Pupil.LY()      
    #AB.befriend(RK)
    #AB.befriend(LY)
    #AB.befriend(DC)
    #print(RS)
    #print(RS.age)
    #print(AB.friends)
    #print()
    #DYD = Charm.DoYourDeeds()
    #DYD.cast()
    
    # task_hacker = DarkHackers('task_hacker', 1980)
    # print("Task Hacker: ", task_hacker)
    # print("Leader: ", task_hacker.leader)
    
    # worker = Worker.AL()
    # print("Worker: ", worker)
    # print()
    
    # dyd = Charm.DoYourDeeds()
    # TechLead = Charm('The Tech Leader', 'I will make your startup a tech giant', 'Series A funding', 'difficult', min_year = 5)
    # PM = ProductManagement('The PM Role', 'I will make you the biggest PM', '10X New consumers')
    # DE = DataEngineer('The Big Data Role', 'I will make you Big Data Engineer', 'Power and Strength')
    
    # PG = Pupil.PG()
    # AB = Pupil.AB()
    
    # PG.print_traits()
    # PG.add_trait('highly intelligent')
    # PG.print_traits()
    
    # SJ = Pupil.SJ()
    # SJ.print_traits()
    # SJ.add_trait('evil')
    # SJ.print_traits()
    
    # print("PG knows the following Vocabs: ", PG.known_vocabs)
    # print("PG is currently in year: ", PG.current_year)
    # PG.learn_vocab(dyd)
    # print('===============================================')
    # AB.learn_vocab(TechLead)
    # PG.learn_vocab(TechLead)
    # print('===============================================')
    # PG.learn_vocab(PM)
    # print('===============================================')
    # SJ.learn_vocab(PM)
    # print('===============================================')
    
    # PG.learn_vocab(DE)
    # print('===============================================')
    # SJ.learn_vocab(PM)
    # print('===============================================')
    # PG.cast_vocab(TechLead)
    # print('===============================================')
    # PG.cast_vocab(DE)
    # print('===============================================')
    # SJ.cast_vocab(DE)
    # print('===============================================')    
    
    # AL = Worker.AL()
    # PZ = Worker.PZ()
    # FL = Worker.FL()
    # CC = Worker.CC()
    
    # RS = Professor.RS()
    # SS = Professor.SS()
    # JB = Professor.JB()
    
    # print('Age of Prfessor JB:', JB.age)
    
    # law_department = Department('Law', RS, AL)
    # print('law_department: ', law_department)
    
    # science_department = Department('Science', SS, FL)
    # print('science department: ', science_department)
    
    # arts_department = Department('Creativity and Arts', JB, CC)
    # print('arts department: ', arts_department)
    # now = 2022
    # SB = DarkHackers('SB', 1990)
    # print('SB: ', SB)
    # PG = Pupil.PG()
    # letter_content = "Hi RK! \nCan SK and I stop by for a tea this afternoon? \nPG"
    # PG.write_letter('RK', letter_content)
    # print(f"Total number of letter creates so far: {Letter.total_number_of_letters}")
    
    moon_bot = Bot(['wheels class land', 'frame class land', 'engine class land', 'power supply class land', 'processor class land', 'sensor class land'])
    air_bot = Bot(['wheels class air', 'frame class air', 'engine class air', 'power supply class air', 'processor class air', 'sensor class air'])
    
    for components in moon_bot:
        print(components)

if __name__ == "__main__":
    main()
    
