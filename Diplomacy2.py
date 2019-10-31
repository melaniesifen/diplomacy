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
    def cityTracker(self, city_lst):
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
    def diplomacyZip(self, s):
        s2 = iter(s) # make s into an iterator
        army, city, action = next(s2), next(s2), list(s2)
        return army, city, action
    

        
# read std in
def diplomacy_read(r, w):
    r = r.split("\n") # splits reader by line
    dip = War()
    lst = []
    for s in r: # for string in reader
        army, city, action = dip.diplomacyZip(s)
        #Create Army objects
        army = Army(action, location = city)
        lst.append(army)
    dip.cityTracker(lst)
    return dip 

