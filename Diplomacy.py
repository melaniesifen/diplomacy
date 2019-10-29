# read std in and solve warfare problem
def diplomacy_solve(r, w):
    r = r.split("\n") # splits reader by line
    lst = []
    for s in r: # for string in reader
        army, city, action = diplomacy_read(s)
        new_city = diplomacy_action(action, city) # new city is determined by the action
        new_army = diplomacy_support(action, army) # if army supports another, change army to supported army
        lst += (new_army, new_city, action)
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
    city_lst = list(zip(*lst))[1] # tuple of all cities
    if len(city_lst) == len(set(city_lst)): # checks for unique cities
        return #Army, city
    # if city is repeated, then multiple armies are in one city (at war)
    armies_at_war = diplomacy_warfare(city_lst, lst) # list of armies at war with each other
    # count number of occurences of each army in lst
    # for item in lst: largest count = city, others = [dead]
    
# create new list of cities with duplicates
# return the list of armies at war
def diplomacy_warfare(city_lst, lst):
    city_lst_duplicates1, city_lst_duplicates2 = set(), set()
    add1, add2 = city_lst_duplicates1.add, city_lst_duplicates2.add
    for city in city_lst:
        if city in city_lst_duplicates1:
            add2(city)
        else:
            add1(city)
    cities_at_war = list(city_lst_duplicates2)
    
    armies_at_war = []
    for city in cities_at_war:
        armies = []
        for tup in lst: # [(army, city, action), (army2, city2, action2),...]
            if tup[1] == city: # if city in tup == city in city_at_war
                armies += [tup[0]] # this army is at war
        armies_at_war += [armies] # separates armies at war by city
                
    return armies_at_war
    
    

    
    
    
    