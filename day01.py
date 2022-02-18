class CollegeMember:
    """Creates a member of the College of Engineering (COE)"""
    location = "India"
    def __init__(self, name, birthyear, sex):
        self.name = name
        self.birthyear = birthyear
        self.sex = sex
        
    def says(self, words):
        return f"{self.name} says {words}."

class Pupil(CollegeMember):
    """Creates a College Pupil"""
    def __init__(self, name, birthyear, sex, start_year, pet = None):
        super().__init__(name, birthyear, sex)
        self.start_year = start_year
        
        if pet is not None:
            self.pet_name, self.pet_type = pet
            
        self._eles = {
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
        
class Professor(CollegeMember):
    """Creates a College Professor"""
    def __init__(self, name, birthyear, sex, subject):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        
class Worker(CollegeMember):
    """Creates a College Worker"""
    def __init__(self, name, birthyear, sex, year_of_death):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death
        
def main():
    RK = CollegeMember("RK", 1995, "male")
    print(RK.says("Hello!"))
    PS = Pupil(name = "PS",
               birthyear=1996,
               sex = "female",
               start_year=2014,
               pet = ("Candy", "Dog"))
if __name__ == "__main__":
    main()
    
