from collections import Counter as C
    
class Army(object):
    def __init__(self, letter = "A", action = [], supported = False, alive = True, location = "Madrid"):
        self.letter = letter
        self.action = action #List containing action and army action taken toward
        self.supported = supported
        self.alive = alive 
        self.location = location
        
    def __str__(self):
        action = " ".join(a for a in self.action)
        return  self.letter + " " + self.location + " " + action

class War(Army):
    def __init__(self):
        self.cities = {}

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
        #else:
    
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
    
    def __str__(self):
        return self.army + " " + self.city + " " + self.action

        
# read std in and create war 
def diplomacy_read(r):
    r = r.split("\n") # splits reader by line
    lst = []
    #Create Army objects and dict
    for s in r: # for string in reader
        army_letter, city, action = diplomacy_separate(s)
        army = Army(army_letter, action, location = city)
        lst.append(str(army))
    return lst

def diplomacy_separate(s):
    s = s.split()
    s = iter(s)
    army, city, action = next(s), next(s), list(s)
    return army, city, action

def diplomacy_solve():
    # take army objects and determine new city based on action "move"
    # update army objects based on move (in a class function)
    # check which armies are supporting - what happens to those armies? Change alive bool
    pass
    
    


