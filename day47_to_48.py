from collections import defaultdict

class CollegeMember:
    """ Creates a member of the College of Engineering (COE)"""
    def __init__(self, name: str, birthyear: int, sex: str):
        
        self.name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = defaultdict(lambda: False)
    
    def add_trait(self, trait, value = True):
        self._traits[trait] = value
        
    def exhibits_trait(self, trait: str) -> bool:
        value = self._traits[trait]
        return value
    
    def print_traits(self):
        true_traits = [trait for trait, value in self._traits.items() if value]
        false_traits = [trait for trait, value in self._traits.items() if not value]
        
        if true_traits:
            print(f"{self.name} is {','.join(true_traits)}")
        
        if false_traits:
            print(f"{self.name} is not {','.join(false_traits)}")
            
        if (not true_traits and not false_traits):
            print(f"{self.name} does not have traits yet")
            
if __name__ == "__main__":
    
    RK = CollegeMember('RK', 1959, 'male')
    
    RK.add_trait('tidy-minded')
    RK.add_trait('kind')
    
    RK.exhibits_trait('kind')
    RK.exhibits_trait('mean')
