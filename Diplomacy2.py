from collections import Counter as C
    
class Army(object):
    def __init__(self, action = [], supported = False, alive = True, location):
        self.action = action #List containing action and army action taken toward
        self.supported = supported
        self.alive = True 
        self.location = location

class War(Army):
    def __init__(self, cities):
        #Inherit from army and create war attributes
        self.cities = diplomacy_read()

    #Perform action (move, hold, support)
    def actionTaken(self):
        #Move and resolve action
        if self.action[0] == 'move':
            self.location = self.action[1] 
            #Call function to resolve what happens next
        #Support and resolve action
        elif self.action[0] == 'support':
            self.action[1].supported  = True
            #Call function to resolve what happens next
        #Hold
        else:
    
    #Move and track 
    def cityTracker(self):
        #Dictionary to hold cities and armies occupying the cities
        #{city : [List of armies in city],...}
        city_dict = {}
        for i in city_lst:
            if i not in city_dict:
                city_dict[i] = list(city_lst(zip(*lst))[0])
            elif i in city_dict:
                city_dict[i].append(i)
        return city_dict

    # packs the two parts of the action (if there are two parts) into one item
    # returns the army, city, and action      
    def diplomacy(self, s):
        s2 = iter(s) # make s into an iterator
        army, city, action = next(s2), next(s2), list(s2)
        return army, city, action
    

        
# read std in
def diplomacy_start(r, w):
    r = r.split("\n") # splits reader by line
    lst = []
    dip = War()
    for s in r: # for string in reader
        army, city, action = diplomacy(s)
        #Create Army objects
        army = Army(action, location = city)
        lst.append(army)




























# read std in and solve warfare problem
def diplomacy_start(r, w):
    r = r.split("\n") # splits reader by line
    lst = []
    for s in r: # for string in reader
        army, city, action = diplomacy_read(s)
        new_city = diplomacy_action(action, city) # new city is determined by the action
        lst += (army, new_city, action)
    diplomacy_eval(lst)


























def diplomacy_eval(lst):
    # if cities are all different, all armies are alive
    city_lst = list(zip(*lst))[1] # list of all cities
    if len(city_lst) == len(set(city_lst)): # checks for unique cities
        return #army city, army ciy, ... army, city
    # if city is repeated, then multiple armies are in one city (at war)
    armies_at_war = diplomacy_warfare(city_lst, lst)
    # for item in lst: largest count = city, others = [dead]
    

# create new list of cities with duplicates
# return the list of armies at war with support
def diplomacy_warfare(city_lst, lst):
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
        for tup in lst:
            if tup[1] == city:
                armies += tup[0]
        armies_at_war += [armies]
    #Dictionary for 