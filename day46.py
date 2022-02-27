import functools

class CollegeMember:
    """Creates a member of the College of Engineering (COE)"""
    def __init__(self, name: str, birthyear: int, sex: str):
        self.name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}
        
    def whisper(function):
        @functools.wraps(function)
        def wrapper(self, *args):
            ''' Whispering decorator '''
            original_output = function(self, *args)
            first_part, words = original_output.split(' says: ')
            words = words.replace('!', '.')
            new_output = f"{first_part} whispers: {words}.."
            return new_output
        return wrapper
    
    def says(self, words):
        '''Allows a college member to talk'''
        return f"{self.name} says: {words}"
    
if __name__ == "__main__":
    RK = CollegeMember("RK", 1959, 'male')
    
    print(RK.says.__name__)
    print(RK.says.__doc__)
