
from __future__ import annotations
from typing import Tuple
import datetime

class CollegeMember:
    """Creates a member of the College of Engineering (COE)"""
    location: str = "India"
    def __init__(self, name: str, birthyear: int, sex: str):
        self.name = name
        self.birthyear = birthyear
        self.sex = sex
        
    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(name='{self.name}',"
                f"birthyear={self.birthyear},sex='{self.sex}')")
    
    @property
    def age(self) -> int:
        now = datetime.datetime.now().year
        return now - self.birthyear
    
    def says(self, words) -> str:
        return f"{self.name} says {words}."
    
    @classmethod
    def CollegeHOD(cls) -> CollegeMember:
        return cls('KK', 1970, 'female')

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
        
        @property
        def skills(self):
            return self._skills
        
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
        
def main():
    RS = Professor.RS()
    LY = Pupil.LY()         
    print(RS)
    print(RS.age)
if __name__ == "__main__":
    main()
    
