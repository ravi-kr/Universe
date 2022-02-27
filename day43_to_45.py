import error
import datetime

class CollegeMember:
    """Creates a member of the College of Engineering (COE)"""
    def __init__(self, name: str, birthyear: int, sex: str):
        self.name = name
        self.birthyear = birthyear
        if type(birthyear) is not int:
            raise error.InvalidBirthyearError("The birthyear is not a valid \
                                              integer. Try semething like 1991")
        self.sex = sex
        self._traits = {}
        
    def add_trait(self, trait: str, value=True):
        self._traits[trait] = value
        
    def exhibits_trait(self, trait: str) -> bool:
        try:
            value = self._traits[trait]
            return value
        except KeyError as e:
            print(f"{self.name} does not have a character trait with the name {e}")
            return False
        
if __name__ == "__main__":
    #RK = CollegeMember("RK", '1959', "male")
    #print("RK: ", RK)
    
    RK = CollegeMember("RK", 1959, "male")
    print("RK: ", RK)    
    
    RK.add_trait('tidy-minded')
    RK.add_trait('kind')
    
    RK.exhibits_trait('kind')
    
    RK.exhibits_trait('mean')
        
        
