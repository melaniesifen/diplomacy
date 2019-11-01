from collections import defaultdict as D

# read std in and solve warfare problem
def diplomacy_solve(r, w):
    r = r.split("\n") # splits reader by line
    lst = []
    for s in r: # for string in reader
        army, city, action = diplomacy_read(s)
        new_city = diplomacy_action(action, city) # new city is determined by the action
        lst += (army, new_city, action)
    diplomacy_eval(lst)

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
    
def diplomacy_eval(lst):
    # if cities are all different, all armies are alive
    city_lst = list(zip(*lst))[1] # list of all cities
    army_lst = list(zip(*lst))[0] # list of all armies
    if len(city_lst) == len(set(city_lst)): # checks for unique cities
        return #army city, army ciy, ... army, city
    # if city is repeated, then multiple armies are in one city (at war)
    # create dict = {city : [army in city, armcy in city], city2 : [army in city2, ...]}
