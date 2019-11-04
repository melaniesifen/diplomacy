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

class War(object):
    def __init__(self, armyList = []):
        self.armyList = armyList
        self.cityList = [army.location for army in armyList]
        

    #Resolve actions (move, hold, support)
    #Call after making dictionary 
    def actionTaken(self, city_dict):
        armyList = self.armyList
        for army in self.armyList:
            #If army action move, update location attribute and dict city value 
            if armyList[army].action[0] == "Move":              
                #If city doesnt exist in dict already
                if city_dict[armyList[army].action[-1]] not in city_dict:
                    city_dict[armyList[army].action[-1]] = armyList[army]  #Create new city in dict
                    city_dict[armyList[army].location] = armyList[army].action[-1]   #New army location
        for army in armyList:
            if city_dict[army].action[0] == "Support":
                supported_army = army.action[-1]
                new_location = supported_army.location
                city_dict[armyList[army].location] = new_location
                city_dict[armyList[army].letter] = supported_army
        return city_dict
    
                
    #Move armies based on moves
    #Create new dict with processed moves 
    #{city: [[army, move], ...], ...}
    def get_city_dict(self):
        pass
    
    # count len of value in dict 
    def count_len(self, city_dict):
        pass

    def __str__(self):
        return self.army + " " + self.city + " " + self.action
    
    def solve(self):
        # city_dict = get_city_dict(self, city_lst)
        # new_dict = actionTaken(self, armylist, city_dictt)
        # 

        
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

def diplomacy_solve(r):
    army_lst = diplomacy_read(r) # create list of army objects from reader
    war = War(army_lst) # create war object from army list
    war.solve() # solve war
    
    
    


