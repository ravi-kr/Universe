import sys
sys.path.append('../')
print(sys.path.append('../'))

import yaml
from day37 import CollegeMember, Pupil

if __name__=="__main__":
    with open('config.yaml', 'r') as c:
        config = yaml.load(c)
        
        RK = CollegeMember(**config['RK'])
        print('RK: ', RK)
        
        AL = Pupil(**config['AL'])
        print('AL: ', AL)
        
        PS = Pupil(**config['PS'])
        print('PS:', PS)
