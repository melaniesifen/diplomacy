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
        super().__init__(self, letter = "A", action = [], supported = False, alive = True, location = "Madrid")
        self.cities = {}

    def removeDictValue(self, value):
        city = self.cities[self.value.location]
        if len(city) > 1:
            city.remove(value)               
        else:
            self.cities[self.value.location] = ''

    #Resolve actions (move, hold, support)
    #Call after making dictionary 
    def actionTaken(self):
        armyList = list(self.cities.values())
        for army in armyList:
            #If army action move, update location attribute and dict city value 
            if armyList[army].action[0] == "Move":       
                newLocation = self.cities[armyList[army].action[-1]]
                curLocation = self.cities[armyList[army].location]
                #If city doesnt exist in dict already
                if self.cities[armyList[army].action[-1]] not in self.cities:
                    self.removeDictValue(army)   #Remove army from original location
                    Newlocation = armyList[army]  #Create new city and army in dict
                #City exists
                else: 
                   self.removeDictValue(army) 
                   newLocation = armyList[army]

            elif self.cities[army].action[0] == "Support":
            else: #action == 'hold'
                pass

    #Move armies based on moves
    #Create new dict with processed moves 
    #{city: [[army, move], ...], ...}
    def cityTracker(self, army_lst):
        #Dictionary to hold cities and armies occupying the cities
        #{city : [List of armies in city],...}
        city_dict = {}
        for i in army_lst:
            if i not in city_dict:
                city_dict[i] = list(city_lst(zip(*army_lst))[0])
            elif i in city_dict:
                city_dict[i].append(i)
        #If cities attribute empty update it
        if len(self.cities) == 0:
            self.cities = city_dict
        else:
            return city_dict

    def __str__(self):
        return self.army + " " + self.city + " " + self.action

        
# read std in and create war 
def diplomacy_read(r):
    r = r.split("\n") # splits reader by line
    army_lst = []
    #Create Army object list
    for s in r: # for string in reader
        army_letter, city, action = diplomacy_separate(s)
        army = Army(army_letter, action, location = city)
        army_lst.append(str(army))
    return army_lst

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
    
    


