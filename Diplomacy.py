from collections import Counter as C

# read std in and solve warfare problem
def diplomacy_solve(r, w):
    r = r.split("\n") # splits reader by line
    lst1, lst2 = [], []
    for s in r: # for string in reader
        army, city, action = diplomacy_read(s)
        new_city = diplomacy_action(action, city) # new city is determined by the action
        new_army = diplomacy_support(action, army) # if army supports another, change army to supported army
        lst1 += (army, city, action)
        lst2 += (new_army, new_city, action)
    diplomacy_eval(lst1, lst2)

 # packs the two parts of the action (if there are two parts) into one item
 # returns the army, city, and action      
def diplomacy_read(s):
    s2 = iter(s) # make s into an iterator
    army, city, action = next(s2), next(s2), list(s2)
    return army, city, action
        
# determines the new location of the army     
def diplomacy_action(action, city):
    if action[0] == "Hold" or "Support": # if action is to hold or support, city does not change
        return city
    # if action is to move, the city changes to the new location
    return action[1]
       
def diplomacy_support(action, army):
    if action[0] == "Support":
        return action[1] # change army to supported army
    # if action is not support, the army stays the same
    return army
    
def diplomacy_eval(lst1, lst2):
    # if cities are all different, all armies are alive
    city_lst = list(zip(*lst2))[1] # list of all cities
    army_lst1 = list(zip(*lst1))[0] # list of all armies
    army_lst2 = list(zip(*lst2))[0] # list of armies without supporting armies
    if len(city_lst) == len(set(city_lst)): # checks for unique cities
        return #army city, army ciy, ... army, city
    # if city is repeated, then multiple armies are in one city (at war)
    armies_at_war = diplomacy_warfare(city_lst, army_lst1, army_lst2)
    # for item in lst: largest count = city, others = [dead]
    
# create new list of cities with duplicates
# return the list of armies at war with support
def diplomacy_warfare(city_lst, lst1, army_lst2):
    city_lst_duplicates1, city_lst_duplicates2 = set(), set()
    add1, add2 = city_lst_duplicates1.add, city_lst_duplicates2.add
    for city in city_lst:
        if city in city_lst_duplicates1:
            add2(city)
        else:
            add1(city)
    cities_at_war = list(city_lst_duplicates2) # list of all duplicate cities (cities at war)
    
    armies_at_war = []
    for city in cities_at_war:
        armies = []
        for tup in lst1:
            if tup[1] == city:
                armies += tup[0]
        armies_at_war += [armies]
        
    for war in armies_at_war:
        for army in war:
            pass
            
        
    army_support = []
        
