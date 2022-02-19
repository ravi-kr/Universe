
from __future__ import annotations
from typing import Tuple
import datetime
from abc import ABC, abstractmethod

class CollegeMember:
    """Creates a member of the College of Engineering (COE)"""
    location: str = "India"
    def __init__(self, name: str, birthyear: int, sex: str):
        self.name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}
        
    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}',"
                f"birthyear={self.birthyear},sex='{self.sex}')")
    
    @property
    def age(self) -> int:
        now = datetime.datetime.now().year
        return now - self.birthyear
    
    @property
    def says(self, words) -> str:
        return f"{self.name} says {words}."
    
    
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
class Pupil(CollegeMember):
    """Creates a College Pupil"""
    def __init__(self, name: str, birthyear: int, sex: str, start_year: int, pet: Tuple[str, str] = None):
        super().__init__(name, birthyear, sex)
        self.start_year = start_year
        
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

class Vocab(ABC):
    def __init__(self, name: str, incantation: str, effect: str):
        self.name = name
        self.incantation = incantation
        self.effect = effect
        
    @abstractmethod
    def cast(self):
        pass
    
    @property
    @abstractmethod
    def defining_feature(self):
        pass
    
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
        
def main():
    SS = CollegeMember(name = "SS", birthyear = 1985, sex = 'female')
    SS.add_trait("kind")
    SS.add_trait("tidy-minded")
    SS.add_trait("impatient", value = False)
    
    SS.print_traits()
    print()
    
    SS.exhibits_trait("kind")
    SS.exhibits_trait("funny")
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
if __name__ == "__main__":
    main()
    
