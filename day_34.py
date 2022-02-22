from collections import Counter
from day29_to_31 import Bot

moon_bot = Bot(['engine class land', 'wheels class land', \
                'frame class land', 'power supply class land'\
                    , 'processor class land'])
    
rough_bot = Bot(['engine class jungle', 'wheels class jungle', \
                'frame class jungle', 'power supply class jungle'\
                    , 'processor class jungle'])
    
water_bot = Bot(['engine class liquid', 'wheels class liquid', \
                'frame class liquid', 'power supply class liquid'\
                    , 'processor class liquid'])
    
air_bot = Bot(['engine class air', 'wheels class air', \
                'frame class air', 'power supply class air'\
                    , 'processor class air'])
    
all_components = [moon_bot, rough_bot, water_bot, air_bot]

shopping_list = Counter()

for components in all_components:
    for component in components:
        shopping_list[component]+=1
        
print(f"Final Shopping list: {shopping_list}")
