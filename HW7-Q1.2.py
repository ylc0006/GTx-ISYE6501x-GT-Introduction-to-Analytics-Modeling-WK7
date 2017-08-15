# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 06:04:28 2017

@author: yan.yl.chen
"""

# Import PuLP modeler functions
from pulp import *

# Creates a list of the Foods
Foods = ['Frozen Broccoli', 'Carrots,Raw', 'Celery, Raw', 'Frozen Corn', 
         'Lettuce,Iceberg,Raw', 'Peppers, Sweet, Raw','Potatoes, Baked',
         'Tofu','Roasted Chicken','Spaghetti W/ Sauce','Tomato,Red,Ripe,Raw',
         'Apple,Raw,W/Skin','Banana','Grapes','Kiwifruit,Raw,Fresh','Oranges',
         'Bagels','Wheat Bread','White Bread','Oatmeal Cookies','Apple Pie',
         'Chocolate Chip Cookies','Butter,Regular','Cheddar Cheese',
         '3.3% Fat,Whole Milk','2% Lowfat Milk','Skim Milk','Poached Eggs',
         'Scrambled Eggs','Bologna,Turkey','Frankfurter, Beef',
         'Ham,Sliced,Extralean','Kielbasa,Prk','CapN Crunch','Cheerios',
         'Corn Flks, KelloggS','Raisin Brn, KellgS','Rice Krispies',
         'Special K','Oatmeal','Malt-O-Meal,Choc','Pizza W/Pepperoni','Taco',
         'Hamburger W/Toppings','Hotdog, Plain','Couscous','White Rice',
         'Macaroni,Ckd','Peanut Butter','Pork','Sardines in Oil',
         'White Tuna in Water','Popcorn,Air-Popped','Potato Chips,Bbqflvr',
         'Pretzels','Tortilla Chip','Chicknoodl Soup','Splt Pea&Hamsoup',
         'Vegetbeef Soup','Neweng Clamchwd','Tomato Soup',
         'New E Clamchwd,W/Mlk','Crm Mshrm Soup,W/Mlk','Beanbacn Soup,W/Watr']

# A dictionary of the costs of each of the Foods is created
costs = {'Frozen Broccoli': 0.16,
         'Carrots,Raw': 0.07,
         'Celery, Raw': 0.04,
         'Frozen Corn': 0.18, 
         'Lettuce,Iceberg,Raw': 0.02,
         'Peppers, Sweet, Raw':0.53,
         'Potatoes, Baked':0.06,
         'Tofu':0.31,
         'Roasted Chicken':0.84,
         'Spaghetti W/ Sauce': 0.78,
         'Tomato,Red,Ripe,Raw':0.27,
         'Apple,Raw,W/Skin':0.24,
         'Banana':0.15,
         'Grapes':0.32,
         'Kiwifruit,Raw,Fresh':0.49,
         'Oranges':0.15,
         'Bagels':0.16,
         'Wheat Bread':0.05,
         'White Bread':0.06,
         'Oatmeal Cookies':0.09,
         'Apple Pie':0.16,
         'Chocolate Chip Cookies':0.03,
         'Butter,Regular':0.05,
         'Cheddar Cheese':0.25,
         '3.3% Fat,Whole Milk':0.16,
         '2% Lowfat Milk':0.23,
         'Skim Milk':0.13,
         'Poached Eggs':0.08,
         'Scrambled Eggs':0.11,
         'Bologna,Turkey':0.15,
         'Frankfurter, Beef':0.27,
         'Ham,Sliced,Extralean':0.33,
         'Kielbasa,Prk':0.15,
         'CapN Crunch':0.31,
         'Cheerios':0.28,
         'Corn Flks, KelloggS':0.28,
         'Raisin Brn, KellgS':0.34,
         'Rice Krispies':0.32,
         'Special K':0.38,
         'Oatmeal':0.82,
         'Malt-O-Meal,Choc':0.52,
         'Pizza W/Pepperoni':0.44,
         'Taco':0.59,
         'Hamburger W/Toppings':0.83,
         'Hotdog, Plain':0.31,
         'Couscous':0.39,
         'White Rice':0.08,
         'Macaroni,Ckd':0.17,
         'Peanut Butter':0.07,
         'Pork':0.81,
         'Sardines in Oil':0.45,
         'White Tuna in Water':0.69,
         'Popcorn,Air-Popped':0.04,
         'Potato Chips,Bbqflvr': 0.22,
         'Pretzels':0.12,
         'Tortilla Chip':0.19,
         'Chicknoodl Soup':0.39,
         'Splt Pea&Hamsoup':0.67,
         'Vegetbeef Soup':0.71,
         'Neweng Clamchwd':0.75,
         'Tomato Soup':0.39,
         'New E Clamchwd,W/Mlk':0.99,
         'Crm Mshrm Soup,W/Mlk':0.65,
         'Beanbacn Soup,W/Watr':0.67}

# A dictionary of the Calories in each of the Foods is created
Calories = {'Frozen Broccoli': 73.8,
            'Carrots,Raw': 23.7,
            'Celery, Raw': 6.4,
            'Frozen Corn': 72.2, 
            'Lettuce,Iceberg,Raw':2.6,
            'Peppers, Sweet, Raw':20,
            'Potatoes, Baked':171.5,
            'Tofu':88.2,
            'Roasted Chicken':277.4,
            'Spaghetti W/ Sauce':358.2,
            'Tomato,Red,Ripe,Raw':25.8,
            'Apple,Raw,W/Skin':81.4,
            'Banana':104.9,
            'Grapes':15.1,
            'Kiwifruit,Raw,Fresh':46.4,
            'Oranges':61.6,
            'Bagels':78,
            'Wheat Bread':65,
            'White Bread':65,
            'Oatmeal Cookies':81,
            'Apple Pie':67.2,
            'Chocolate Chip Cookies':78.1,
            'Butter,Regular':35.8,
            'Cheddar Cheese':112.7,
            '3.3% Fat,Whole Milk':149.9,
            '2% Lowfat Milk':121.2,
            'Skim Milk':85.5,
            'Poached Eggs':74.5,
         'Scrambled Eggs':99.6,
         'Bologna,Turkey':56.4,
         'Frankfurter, Beef':141.8,
         'Ham,Sliced,Extralean':37.1,
         'Kielbasa,Prk':80.6,
         'CapN Crunch':119.6,
         'Cheerios':111,
         'Corn Flks, KelloggS':110.5,
         'Raisin Brn, KellgS':115.1,
         'Rice Krispies':112.2,
         'Special K':110.8,
         'Oatmeal':145.1,
         'Malt-O-Meal,Choc':607.2,
         'Pizza W/Pepperoni':181,
         'Taco':369.4,
         'Hamburger W/Toppings':275,
         'Hotdog, Plain':242.1,
         'Couscous':100.8,
         'White Rice':102.7,
         'Macaroni,Ckd':98.7,
         'Peanut Butter':188.5,
         'Pork':710.8,
         'Sardines in Oil':49.9,
         'White Tuna in Water':115.6,
         'Popcorn,Air-Popped':108.3,
         'Potato Chips,Bbqflvr': 139.2,
         'Pretzels':108,
         'Tortilla Chip':142,
         'Chicknoodl Soup':150.1,
         'Splt Pea&Hamsoup':184.8,
         'Vegetbeef Soup':158.1,
         'Neweng Clamchwd':175.7,
         'Tomato Soup':170.7,
         'New E Clamchwd,W/Mlk':163.7,
         'Crm Mshrm Soup,W/Mlk':203.4,
         'Beanbacn Soup,W/Watr':172}

# A dictionary of the Cholesterol in each of the Foods is created
Cholesterol = {'Frozen Broccoli': 0,
         'Carrots,Raw': 0,
         'Celery, Raw': 0,
         'Frozen Corn': 0, 
         'Lettuce,Iceberg,Raw': 0,
         'Peppers, Sweet, Raw':0,
         'Potatoes, Baked':0,
         'Tofu':0,
         'Roasted Chicken':129.9,
         'Spaghetti W/ Sauce': 0,
         'Tomato,Red,Ripe,Raw':0,
         'Apple,Raw,W/Skin':0,
         'Banana':0,
         'Grapes':0,
         'Kiwifruit,Raw,Fresh':0,
         'Oranges':0,
         'Bagels':0,
         'Wheat Bread':0,
         'White Bread':0,
         'Oatmeal Cookies':0,
         'Apple Pie':0,
         'Chocolate Chip Cookies':5.1,
         'Butter,Regular':10.9,
         'Cheddar Cheese':29.4,
         '3.3% Fat,Whole Milk':33.2,
         '2% Lowfat Milk':18.3,
         'Skim Milk':4.4,
         'Poached Eggs':211.5,
         'Scrambled Eggs':211.2,
         'Bologna,Turkey':28.1,
         'Frankfurter, Beef':27.4,
         'Ham,Sliced,Extralean':13.3,
         'Kielbasa,Prk':17.4,
         'CapN Crunch':0,
         'Cheerios':0,
         'Corn Flks, KelloggS':0,
         'Raisin Brn, KellgS':0,
         'Rice Krispies':0,
         'Special K':0,
         'Oatmeal':0,
         'Malt-O-Meal,Choc':0,
         'Pizza W/Pepperoni':14.2,
         'Taco':56.4,
         'Hamburger W/Toppings':42.8,
         'Hotdog, Plain':44.1,
         'Couscous':0,
         'White Rice':0,
         'Macaroni,Ckd':0,
         'Peanut Butter':0,
         'Pork':105.1,
         'Sardines in Oil':34.1,
         'White Tuna in Water':35.7,
         'Popcorn,Air-Popped':0,
         'Potato Chips,Bbqflvr': 0,
         'Pretzels':0,
         'Tortilla Chip':0,
         'Chicknoodl Soup':12.3,
         'Splt Pea&Hamsoup':7.2,
         'Vegetbeef Soup':10,
         'Neweng Clamchwd':10,
         'Tomato Soup':0,
         'New E Clamchwd,W/Mlk':22.3,
         'Crm Mshrm Soup,W/Mlk':19.8,
         'Beanbacn Soup,W/Watr':2.5}

# A dictionary of the Total_Fat in each of the Foods is created
Total_Fat = {'Frozen Broccoli': 0.8,
         'Carrots,Raw': 0.1,
         'Celery, Raw': 0.1,
         'Frozen Corn': 0.6, 
         'Lettuce,Iceberg,Raw': 0,
         'Peppers, Sweet, Raw':0.1,
         'Potatoes, Baked':0.2,
         'Tofu':5.5,
         'Roasted Chicken':10.8,
         'Spaghetti W/ Sauce': 12.3,
         'Tomato,Red,Ripe,Raw':0.4,
         'Apple,Raw,W/Skin':0.5,
         'Banana':0.5,
         'Grapes':0.1,
         'Kiwifruit,Raw,Fresh':0.3,
         'Oranges':0.2,
         'Bagels':0.5,
         'Wheat Bread':1,
         'White Bread':1,
         'Oatmeal Cookies':3.3,
         'Apple Pie':3.1,
         'Chocolate Chip Cookies':4.5,
         'Butter,Regular':4.1,
         'Cheddar Cheese':9.3,
         '3.3% Fat,Whole Milk':8.1,
         '2% Lowfat Milk':4.7,
         'Skim Milk':0.4,
         'Poached Eggs':5,
         'Scrambled Eggs':7.3,
         'Bologna,Turkey':4.3,
         'Frankfurter, Beef':12.8,
         'Ham,Sliced,Extralean':1.4,
         'Kielbasa,Prk':7.1,
         'CapN Crunch':2.6,
         'Cheerios':1.8,
         'Corn Flks, KelloggS':0.1,
         'Raisin Brn, KellgS':0.7,
         'Rice Krispies':0.2,
         'Special K':0.1,
         'Oatmeal':2.3,
         'Malt-O-Meal,Choc':1.5,
         'Pizza W/Pepperoni':7,
         'Taco':20.6,
         'Hamburger W/Toppings':10.2,
         'Hotdog, Plain':14.5,
         'Couscous':0.1,
         'White Rice':0.2,
         'Macaroni,Ckd':0.5,
         'Peanut Butter':16,
         'Pork':72.2,
         'Sardines in Oil':2.7,
         'White Tuna in Water':2.1,
         'Popcorn,Air-Popped':1.2,
         'Potato Chips,Bbqflvr': 9.2,
         'Pretzels':1,
         'Tortilla Chip':7.4,
         'Chicknoodl Soup':4.6,
         'Splt Pea&Hamsoup':4,
         'Vegetbeef Soup':3.8,
         'Neweng Clamchwd':5,
         'Tomato Soup':3.8,
         'New E Clamchwd,W/Mlk':6.6,
         'Crm Mshrm Soup,W/Mlk':13.6,
         'Beanbacn Soup,W/Watr':5.9}

# A dictionary of the Sodium in each of the Foods is created
Sodium = {'Frozen Broccoli': 68.2,
         'Carrots,Raw': 19.2,
         'Celery, Raw': 34.8,
         'Frozen Corn': 2.5, 
         'Lettuce,Iceberg,Raw': 1.8,
         'Peppers, Sweet, Raw':1.5,
         'Potatoes, Baked':15.2,
         'Tofu':8.1,
         'Roasted Chicken':125.6,
         'Spaghetti W/ Sauce': 1237.1,
         'Tomato,Red,Ripe,Raw':11.1,
         'Apple,Raw,W/Skin':0,
         'Banana':1.1,
         'Grapes':0.5,
         'Kiwifruit,Raw,Fresh':3.8,
         'Oranges':0,
         'Bagels':151.4,
         'Wheat Bread':134.5,
         'White Bread':132.5,
         'Oatmeal Cookies':68.9,
         'Apple Pie':75.4,
         'Chocolate Chip Cookies':57.8,
         'Butter,Regular':41.3,
         'Cheddar Cheese':173.7,
         '3.3% Fat,Whole Milk':119.6,
         '2% Lowfat Milk':121.8,
         'Skim Milk':126.2,
         'Poached Eggs':140,
         'Scrambled Eggs':168,
         'Bologna,Turkey':248.9,
         'Frankfurter, Beef':461.7,
         'Ham,Sliced,Extralean':405.1,
         'Kielbasa,Prk':279.8,
         'CapN Crunch':213.3,
         'Cheerios':307.6,
         'Corn Flks, KelloggS':290.5,
         'Raisin Brn, KellgS':204.4,
         'Rice Krispies':340.8,
         'Special K':265.5,
         'Oatmeal':2.3,
         'Malt-O-Meal,Choc':16.5,
         'Pizza W/Pepperoni':267,
         'Taco':802,
         'Hamburger W/Toppings':563.9,
         'Hotdog, Plain':670.3,
         'Couscous':4.5,
         'White Rice':0.8,
         'Macaroni,Ckd':0.7,
         'Peanut Butter':155.5,
         'Pork':38.4,
         'Sardines in Oil':121.2,
         'White Tuna in Water':333.2,
         'Popcorn,Air-Popped':1.1,
         'Potato Chips,Bbqflvr': 212.6,
         'Pretzels':486.2,
         'Tortilla Chip':149.7,
         'Chicknoodl Soup':1862.2,
         'Splt Pea&Hamsoup':964.8,
         'Vegetbeef Soup':1915.1,
         'Neweng Clamchwd':1864.9,
         'Tomato Soup':1744.4,
         'New E Clamchwd,W/Mlk':992,
         'Crm Mshrm Soup,W/Mlk':1076.3,
         'Beanbacn Soup,W/Watr':951.3}

# A dictionary of the Carbohydrates in each of the Foods is created
Carbohydrates= {'Frozen Broccoli': 13.6,
         'Carrots,Raw': 5.6,
         'Celery, Raw': 1.5,
         'Frozen Corn': 17.1, 
         'Lettuce,Iceberg,Raw': 0.4,
         'Peppers, Sweet, Raw':4.8,
         'Potatoes, Baked':39.9,
         'Tofu':2.2,
         'Roasted Chicken':0,
         'Spaghetti W/ Sauce': 58.3,
         'Tomato,Red,Ripe,Raw':5.7,
         'Apple,Raw,W/Skin':21,
         'Banana':26.7,
         'Grapes':4.1,
         'Kiwifruit,Raw,Fresh':11.3,
         'Oranges':15.4,
         'Bagels':15.1,
         'Wheat Bread':12.4,
         'White Bread':11.8,
         'Oatmeal Cookies':12.4,
         'Apple Pie':9.6,
         'Chocolate Chip Cookies':9.3,
         'Butter,Regular':0,
         'Cheddar Cheese':0.4,
         '3.3% Fat,Whole Milk':11.4,
         '2% Lowfat Milk':11.7,
         'Skim Milk':11.9,
         'Poached Eggs':0.6,
         'Scrambled Eggs':1.3,
         'Bologna,Turkey':0.3,
         'Frankfurter, Beef':0.8,
         'Ham,Sliced,Extralean':0.3,
         'Kielbasa,Prk':0.6,
         'CapN Crunch':23,
         'Cheerios':19.6,
         'Corn Flks, KelloggS':24.5,
         'Raisin Brn, KellgS':27.9,
         'Rice Krispies':24.8,
         'Special K':21.3,
         'Oatmeal':25.3,
         'Malt-O-Meal,Choc':128.2,
         'Pizza W/Pepperoni':19.9,
         'Taco':26.7,
         'Hamburger W/Toppings':32.7,
         'Hotdog, Plain':18,
         'Couscous':20.9,
         'White Rice':22.3,
         'Macaroni,Ckd':19.8,
         'Peanut Butter':6.9,
         'Pork':0,
         'Sardines in Oil':0,
         'White Tuna in Water':0,
         'Popcorn,Air-Popped':22.1,
         'Potato Chips,Bbqflvr': 15,
         'Pretzels':22.5,
         'Tortilla Chip':17.8,
         'Chicknoodl Soup':18.7,
         'Splt Pea&Hamsoup':26.8,
         'Vegetbeef Soup':20.4,
         'Neweng Clamchwd':21.8,
         'Tomato Soup':33.2,
         'New E Clamchwd,W/Mlk':16.6,
         'Crm Mshrm Soup,W/Mlk':15,
         'Beanbacn Soup,W/Watr':22.8}

# A dictionary of the Dietary_Fiber in each of the Foods is created
Dietary_Fiber ={ 'Frozen Broccoli': 8.5,
         'Carrots,Raw': 1.6,
         'Celery, Raw': 0.7,
         'Frozen Corn': 2, 
         'Lettuce,Iceberg,Raw': 0.3,
         'Peppers, Sweet, Raw':1.3,
         'Potatoes, Baked':3.2,
         'Tofu':1.4,
         'Roasted Chicken':0,
         'Spaghetti W/ Sauce': 11.6,
         'Tomato,Red,Ripe,Raw':1.4,
         'Apple,Raw,W/Skin':3.7,
         'Banana':2.7,
         'Grapes':0.2,
         'Kiwifruit,Raw,Fresh':2.6,
         'Oranges':3.1,
         'Bagels':0.6,
         'Wheat Bread':1.3,
         'White Bread':1.1,
         'Oatmeal Cookies':0.6,
         'Apple Pie':0.5,
         'Chocolate Chip Cookies':0,
         'Butter,Regular':0,
         'Cheddar Cheese':0,
         '3.3% Fat,Whole Milk':0,
         '2% Lowfat Milk':0,
         'Skim Milk':0,
         'Poached Eggs':0,
         'Scrambled Eggs':0,
         'Bologna,Turkey':0,
         'Frankfurter, Beef':0,
         'Ham,Sliced,Extralean':0,
         'Kielbasa,Prk':0,
         'CapN Crunch':0.5,
         'Cheerios':2,
         'Corn Flks, KelloggS':0.7,
         'Raisin Brn, KellgS':4,
         'Rice Krispies':0.4,
         'Special K':0.7,
         'Oatmeal':4,
         'Malt-O-Meal,Choc':0,
         'Pizza W/Pepperoni':0,
         'Taco':0,
         'Hamburger W/Toppings':0,
         'Hotdog, Plain':0,
         'Couscous':1.3,
         'White Rice':0.3,
         'Macaroni,Ckd':0.9,
         'Peanut Butter':2.1,
         'Pork':0,
         'Sardines in Oil':0,
         'White Tuna in Water':0,
         'Popcorn,Air-Popped':4.3,
         'Potato Chips,Bbqflvr': 1.2,
         'Pretzels':0.9,
         'Tortilla Chip':1.8,
         'Chicknoodl Soup':1.5,
         'Splt Pea&Hamsoup':4.1,
         'Vegetbeef Soup':4,
         'Neweng Clamchwd':1.5,
         'Tomato Soup':1,
         'New E Clamchwd,W/Mlk':1.5,
         'Crm Mshrm Soup,W/Mlk':0.5,
         'Beanbacn Soup,W/Watr':8.6}

# A dictionary of the Protein in each of the Foods is created
Protein ={ 'Frozen Broccoli': 8,
         'Carrots,Raw': 0.6,
         'Celery, Raw': 0.3,
         'Frozen Corn': 2.5, 
         'Lettuce,Iceberg,Raw': 0.2,
         'Peppers, Sweet, Raw':0.7,
         'Potatoes, Baked':3.7,
         'Tofu':9.4,
         'Roasted Chicken':42.2,
         'Spaghetti W/ Sauce': 8.2,
         'Tomato,Red,Ripe,Raw':1,
         'Apple,Raw,W/Skin':0.3,
         'Banana':1.2,
         'Grapes':0.2,
         'Kiwifruit,Raw,Fresh':0.8,
         'Oranges':1.2,
         'Bagels':3,
         'Wheat Bread':2.2,
         'White Bread':2.3,
         'Oatmeal Cookies':1.1,
         'Apple Pie':0.5,
         'Chocolate Chip Cookies':0.9,
         'Butter,Regular':0,
         'Cheddar Cheese':7,
         '3.3% Fat,Whole Milk':8,
         '2% Lowfat Milk':8.1,
         'Skim Milk':8.4,
         'Poached Eggs':6.2,
         'Scrambled Eggs':6.7,
         'Bologna,Turkey':3.9,
         'Frankfurter, Beef':5.4,
         'Ham,Sliced,Extralean':5.5,
         'Kielbasa,Prk':3.4,
         'CapN Crunch':1.4,
         'Cheerios':4.3,
         'Corn Flks, KelloggS':2.3,
         'Raisin Brn, KellgS':4,
         'Rice Krispies':1.9,
         'Special K':5.6,
         'Oatmeal':6.1,
         'Malt-O-Meal,Choc':17.3,
         'Pizza W/Pepperoni':10.1,
         'Taco':20.7,
         'Hamburger W/Toppings':13.6,
         'Hotdog, Plain':10.4,
         'Couscous':3.4,
         'White Rice':2.1,
         'Macaroni,Ckd':3.3,
         'Peanut Butter':7.7,
         'Pork':13.8,
         'Sardines in Oil':5.9,
         'White Tuna in Water':22.7,
         'Popcorn,Air-Popped':3.4,
         'Potato Chips,Bbqflvr': 2.2,
         'Pretzels':2.6,
         'Tortilla Chip':2,
         'Chicknoodl Soup':7.9,
         'Splt Pea&Hamsoup':11.1,
         'Vegetbeef Soup':11.2,
         'Neweng Clamchwd':10.9,
         'Tomato Soup':4.1,
         'New E Clamchwd,W/Mlk':9.5,
         'Crm Mshrm Soup,W/Mlk':6.1,
         'Beanbacn Soup,W/Watr':7.9}

# A dictionary of the Vit_A in each of the Foods is created
Vit_A  ={'Frozen Broccoli': 5867.4,
         'Carrots,Raw': 15471,
         'Celery, Raw': 53.6,
         'Frozen Corn': 106.6, 
         'Lettuce,Iceberg,Raw': 66,
         'Peppers, Sweet, Raw':467.7,
         'Potatoes, Baked':0,
         'Tofu':98.6,
         'Roasted Chicken':77.4,
         'Spaghetti W/ Sauce': 3055.2,
         'Tomato,Red,Ripe,Raw':766.3,
         'Apple,Raw,W/Skin':73.1,
         'Banana':92.3,
         'Grapes':24,
         'Kiwifruit,Raw,Fresh':133,
         'Oranges':268.6,
         'Bagels':0,
         'Wheat Bread':0,
         'White Bread':0,
         'Oatmeal Cookies':2.9,
         'Apple Pie':35.2,
         'Chocolate Chip Cookies':101.8,
         'Butter,Regular':152.9,
         'Cheddar Cheese':296.5,
         '3.3% Fat,Whole Milk':307.4,
         '2% Lowfat Milk':500.2,
         'Skim Milk':499.8,
         'Poached Eggs':316,
         'Scrambled Eggs':409.2,
         'Bologna,Turkey':0,
         'Frankfurter, Beef':0,
         'Ham,Sliced,Extralean':0,
         'Kielbasa,Prk':0,
         'CapN Crunch':40.6,
         'Cheerios':1252.2,
         'Corn Flks, KelloggS':1252.2,
         'Raisin Brn, KellgS':1250.2,
         'Rice Krispies':1252.2,
         'Special K':1252.2,
         'Oatmeal':37.4,
         'Malt-O-Meal,Choc':0,
         'Pizza W/Pepperoni':281.9,
         'Taco':855,
         'Hamburger W/Toppings':126.3,
         'Hotdog, Plain':0,
         'Couscous':0,
         'White Rice':0,
         'Macaroni,Ckd':0,
         'Peanut Butter':0,
         'Pork':14.7,
         'Sardines in Oil':53.8,
         'White Tuna in Water':68,
         'Popcorn,Air-Popped':55.6,
         'Potato Chips,Bbqflvr':61.5,
         'Pretzels':0,
         'Tortilla Chip':55.6,
         'Chicknoodl Soup':1308.7,
         'Splt Pea&Hamsoup':4872,
         'Vegetbeef Soup':3785.1,
         'Neweng Clamchwd':20.1,
         'Tomato Soup':1393,
         'New E Clamchwd,W/Mlk':163.7,
         'Crm Mshrm Soup,W/Mlk':153.8,
         'Beanbacn Soup,W/Watr':888}

# A dictionary of the Vit_C in each of the Foods is created
Vit_C  ={'Frozen Broccoli': 160.2,
         'Carrots,Raw': 5.1,
         'Celery, Raw': 2.8,
         'Frozen Corn': 5.2, 
         'Lettuce,Iceberg,Raw': 0.8,
         'Peppers, Sweet, Raw':66.1,
         'Potatoes, Baked':15.6,
         'Tofu':0.1,
         'Roasted Chicken':0,
         'Spaghetti W/ Sauce': 27.9,
         'Tomato,Red,Ripe,Raw':23.5,
         'Apple,Raw,W/Skin':7.9,
         'Banana':10.4,
         'Grapes':1,
         'Kiwifruit,Raw,Fresh':74.5,
         'Oranges':69.7,
         'Bagels':0,
         'Wheat Bread':0,
         'White Bread':0,
         'Oatmeal Cookies':0.1,
         'Apple Pie':0.9,
         'Chocolate Chip Cookies':0,
         'Butter,Regular':0,
         'Cheddar Cheese':0,
         '3.3% Fat,Whole Milk':2.3,
         '2% Lowfat Milk':2.3,
         'Skim Milk':2.4,
         'Poached Eggs':0,
         'Scrambled Eggs':0.1,
         'Bologna,Turkey':0,
         'Frankfurter, Beef':10.8,
         'Ham,Sliced,Extralean':7.4,
         'Kielbasa,Prk':5.5,
         'CapN Crunch':0,
         'Cheerios':15.1,
         'Corn Flks, KelloggS':15.1,
         'Raisin Brn, KellgS':0,
         'Rice Krispies':15.1,
         'Special K':15.1,
         'Oatmeal':0,
         'Malt-O-Meal,Choc':0,
         'Pizza W/Pepperoni':1.6,
         'Taco':2.2,
         'Hamburger W/Toppings':2.6,
         'Hotdog, Plain':0.1,
         'Couscous':0,
         'White Rice':0,
         'Macaroni,Ckd':0,
         'Peanut Butter':0,
         'Pork':0,
         'Sardines in Oil':0,
         'White Tuna in Water':0,
         'Popcorn,Air-Popped':0,
         'Potato Chips,Bbqflvr': 9.6,
         'Pretzels':0,
         'Tortilla Chip':0,
         'Chicknoodl Soup':0,
         'Splt Pea&Hamsoup':7,
         'Vegetbeef Soup':4.8,
         'Neweng Clamchwd':4.8,
         'Tomato Soup':133,
         'New E Clamchwd,W/Mlk':3.5,
         'Crm Mshrm Soup,W/Mlk':2.2,
         'Beanbacn Soup,W/Watr':1.5}

# A dictionary of the Calcium in each of the Foods is created
Calcium={'Frozen Broccoli': 159,
         'Carrots,Raw': 14.9,
         'Celery, Raw': 16,
         'Frozen Corn': 3.3, 
         'Lettuce,Iceberg,Raw': 3.8,
         'Peppers, Sweet, Raw':6.7,
         'Potatoes, Baked':22.7,
         'Tofu':121.8,
         'Roasted Chicken': 21.9,
         'Spaghetti W/ Sauce': 80.2,
         'Tomato,Red,Ripe,Raw':6.2,
         'Apple,Raw,W/Skin':9.7,
         'Banana':6.8,
         'Grapes':3.4,
         'Kiwifruit,Raw,Fresh':19.8,
         'Oranges':52.4,
         'Bagels':21,
         'Wheat Bread':10.8,
         'White Bread':26.2,
         'Oatmeal Cookies':6.7,
         'Apple Pie':3.1,
         'Chocolate Chip Cookies':6.2,
         'Butter,Regular':1.2,
         'Cheddar Cheese':202,
         '3.3% Fat,Whole Milk':291.3,
         '2% Lowfat Milk':296.7,
         'Skim Milk':302.3,
         'Poached Eggs':24.5,
         'Scrambled Eggs':42.6,
         'Bologna,Turkey':23.8,
         'Frankfurter, Beef':9,
         'Ham,Sliced,Extralean':2,
         'Kielbasa,Prk':11.4,
         'CapN Crunch':4.8,
         'Cheerios':48.6,
         'Corn Flks, KelloggS':0.9,
         'Raisin Brn, KellgS':12.9,
         'Rice Krispies':4,
         'Special K':8.2,
         'Oatmeal':18.7,
         'Malt-O-Meal,Choc':23.1,
         'Pizza W/Pepperoni':64.6,
         'Taco':220.6,
         'Hamburger W/Toppings':51.4,
         'Hotdog, Plain':23.5,
         'Couscous':7.2,
         'White Rice':7.9,
         'Macaroni,Ckd':4.9,
         'Peanut Butter':13.1,
         'Pork':59.9,
         'Sardines in Oil':91.7,
         'White Tuna in Water':3.4,
         'Popcorn,Air-Popped':2.8,
         'Potato Chips,Bbqflvr': 14.2,
         'Pretzels':10.2,
         'Tortilla Chip':43.7,
         'Chicknoodl Soup':27.1,
         'Splt Pea&Hamsoup':33.6,
         'Vegetbeef Soup':32.6,
         'Neweng Clamchwd':82.8,
         'Tomato Soup':27.6,
         'New E Clamchwd,W/Mlk':186,
         'Crm Mshrm Soup,W/Mlk':178.6,
         'Beanbacn Soup,W/Watr':81}


# A dictionary of the Iron in each of the Foods is created
Iron ={  'Frozen Broccoli': 2.3,
         'Carrots,Raw': 0.3,
         'Celery, Raw': 0.2,
         'Frozen Corn': 0.3, 
         'Lettuce,Iceberg,Raw': 0.1,
         'Peppers, Sweet, Raw': 0.3,
         'Potatoes, Baked':4.3,
         'Tofu':6.2,
         'Roasted Chicken':1.8 ,
         'Spaghetti W/ Sauce': 2.3,
         'Tomato,Red,Ripe,Raw':0.6,
         'Apple,Raw,W/Skin':0.2,
         'Banana':0.4,
         'Grapes':0.1,
         'Kiwifruit,Raw,Fresh':0.3,
         'Oranges':0.1,
         'Bagels':1 ,
         'Wheat Bread':0.7,
         'White Bread':0.8,
         'Oatmeal Cookies':0.5,
         'Apple Pie':0.1,
         'Chocolate Chip Cookies':0.4,
         'Butter,Regular':0,
         'Cheddar Cheese':0.2,
         '3.3% Fat,Whole Milk':0.1,
         '2% Lowfat Milk':0.1,
         'Skim Milk':0.1,
         'Poached Eggs':0.7,
         'Scrambled Eggs':0.7,
         'Bologna,Turkey':0.4,
         'Frankfurter, Beef':0.6,
         'Ham,Sliced,Extralean':0.2,
         'Kielbasa,Prk':0.4,
         'CapN Crunch':7.5,
         'Cheerios':4.5,
         'Corn Flks, KelloggS':1.8,
         'Raisin Brn, KellgS':16.8,
         'Rice Krispies':1.8,
         'Special K':4.5,
         'Oatmeal':1.6,
         'Malt-O-Meal,Choc':4.7,
         'Pizza W/Pepperoni':0.9,
         'Taco':2.4,
         'Hamburger W/Toppings':2.5,
         'Hotdog, Plain':2.3,
         'Couscous':0.3,
         'White Rice':0.9,
         'Macaroni,Ckd':1,
         'Peanut Butter':0.6,
         'Pork':0.4,
         'Sardines in Oil':0.7,
         'White Tuna in Water':0.5,
         'Popcorn,Air-Popped':0.8,
         'Potato Chips,Bbqflvr': 0.5,
         'Pretzels':1.2,
         'Tortilla Chip':0.4,
         'Chicknoodl Soup':1.5,
         'Splt Pea&Hamsoup':2.1,
         'Vegetbeef Soup':2.2,
         'Neweng Clamchwd':2.8,
         'Tomato Soup':3.5,
         'New E Clamchwd,W/Mlk':1.5,
         'Crm Mshrm Soup,W/Mlk':0.6,
         'Beanbacn Soup,W/Watr':2}

# Create the 'prob' variable to contain the problem data
prob = LpProblem("The Diet Problem", LpMinimize)

# A dictionary called 'food_vars' is created to contain the referenced Variables
food_vars = LpVariable.dicts("Food",Foods,0)

#create a binary variable to state that a Food is in diet
select_vars = pulp.LpVariable.dicts('Select', Foods, 
                            cat = pulp.LpBinary)

# The objective function is added to 'prob' first
prob += lpSum([costs[i]*food_vars[i] for i in Foods]), "Total Cost of Foods per person"

# The 22 constraints are added to 'prob' for min and Max nutrition requirement

prob += lpSum([Calories[i] * food_vars[i] for i in Foods]) >= 1500, "CaloriesminRequirement"
prob += lpSum([Calories[i] * food_vars[i] for i in Foods]) <= 2500, "CaloriesMaxRequirement"

prob += lpSum([Cholesterol[i] * food_vars[i] for i in Foods]) >= 30, "CholesterolminRequirement"
prob += lpSum([Cholesterol[i] * food_vars[i] for i in Foods]) <= 240, "CholesterolMaxRequirement"

prob += lpSum([Total_Fat[i] * food_vars[i] for i in Foods]) >= 20, "Total_FatminRequirement"
prob += lpSum([Total_Fat[i] * food_vars[i] for i in Foods]) <= 70, "Total_FatMaxRequirement"

prob += lpSum([Sodium[i] * food_vars[i] for i in Foods]) >= 800, "SodiumminRequirement"
prob += lpSum([Sodium[i] * food_vars[i] for i in Foods]) <= 2000, "SodiumMaxRequirement"

prob += lpSum([Carbohydrates[i] * food_vars[i] for i in Foods]) >= 130, "CarbohydratesminRequirement"
prob += lpSum([Carbohydrates[i] * food_vars[i] for i in Foods]) <= 450, "CarbohydratesMaxRequirement"

prob += lpSum([Dietary_Fiber[i] * food_vars[i] for i in Foods]) >= 125, "Dietary_FibersminRequirement"
prob += lpSum([Dietary_Fiber[i] * food_vars[i] for i in Foods]) <= 250, "Dietary_FiberMaxRequirement"

prob += lpSum([Protein[i] * food_vars[i] for i in Foods]) >= 60, "ProteinminRequirement"
prob += lpSum([Protein[i] * food_vars[i] for i in Foods]) <= 100, "ProteinMaxRequirement"

prob += lpSum([Vit_A[i] * food_vars[i] for i in Foods]) >= 1000, "Vit_AminRequirement"
prob += lpSum([Vit_A[i] * food_vars[i] for i in Foods]) <= 10000, "Vit_AMaxRequirement"

prob += lpSum([Vit_C[i] * food_vars[i] for i in Foods]) >= 400, "Vit_CminRequirement"
prob += lpSum([Vit_C[i] * food_vars[i] for i in Foods]) <= 5000, "Vit_CMaxRequirement"

prob += lpSum([Calcium[i] * food_vars[i] for i in Foods]) >= 700, "CalciumminRequirement"
prob += lpSum([Calcium[i] * food_vars[i] for i in Foods]) <= 1500, "CalciumMaxRequirement"

prob += lpSum([Iron[i] * food_vars[i] for i in Foods]) >= 10, "IronminRequirement"
prob += lpSum([Iron[i] * food_vars[i] for i in Foods]) <= 40, "IronMaxRequirement"

# Add constraints for 1.2 a
for i in Foods:
  prob += food_vars[i] <= 1000* select_vars[i], ""

for i in Foods:
  prob += food_vars[i] >= 0.1 * select_vars[i], ""

# Add constraints for 1.2 b
prob += select_vars['Frozen Broccoli'] + select_vars['Celery, Raw'] <=1, ""

# Add constraints for 1.2 c

prob += (select_vars['Roasted Chicken'] + select_vars['Poached Eggs']  
+ select_vars['Scrambled Eggs'] + select_vars['Bologna,Turkey'] 
+ select_vars['Frankfurter, Beef'] + select_vars['Ham,Sliced,Extralean']
+ select_vars['Kielbasa,Prk'] + select_vars['Pizza W/Pepperoni']
+ select_vars['Hamburger W/Toppings'] + select_vars['Hotdog, Plain']
+ select_vars['Pork'] + select_vars['Sardines in Oil']
+ select_vars['White Tuna in Water'] )>=3, ""
        

# The problem data is written to an .lp file
prob.writeLP("DietModel1.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print ("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print (v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen    
print ("Total Cost of Foods per person = ", value(prob.objective))

