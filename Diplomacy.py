#Army Object
class Army(object):
    def __init__(self, letter = "A", action = [], city = "Madrid", support = 0, alive = True):
        self.letter = letter
        self.action = action
        self.support = support
        self.alive = alive
        self.city = city

    #Sets location attribute for the new city  
    def set_location(self, new_city):
        self.city = new_city
        return self.city

    #String Representation of army, location, and action
    def __str__(self):
        action = " ".join(a for a in self.action)
        return self.letter + " " + self.city + " " + action

#War object
class War(object):
    #Army_list contains army objects
    #City list constains city names
    def __init__(self, army_lst = [], city_lst = []):
        self.army_lst = army_lst
        self.city_lst = [army.city for army in army_lst]

    #Performs move action for army that has it   
    def move(self):
        for army in self.army_lst:
            if army.action[0] == "Move":
                army.set_location(army.action[1])
        self.city_lst = list(set(army.city for army in self.army_lst))
    
    #Creates original city dictionary with armies as values for the city
    #{city: [armies occupying city], ...}
    def set_city_dict(self):
        city_dict = {city : [] for city in self.city_lst}
        for key in city_dict:
            for army in self.army_lst:
                if army.city == key:
                    city_dict[key].append(army)
        return city_dict
    
    #Evaluates the outcome of the war
    def eval_war(self, city_dict):
        #If supporting from a singlely occupied city
        for key, value in city_dict.items():
            if len(value) == 1:
                army = value[0]
                if army.action[0] == "Support":
                    self.add_support(army.action[1])
        #Checks supported armies and determins which live
        for key, value in city_dict.items():
            if len(value) != 1:
                for army in value:
                    if army.action[0] == "Support":
                        self.support(value)
                        if army.alive:
                            self.add_support(army.action[1])
        #Checks for values that are not support in the dictionary
        for key, value in city_dict.items():
            if len(value) != 1:
                if any(army.action[0] == "Support" for army in value):
                    continue
                else:
                    self.support(value)
    
    #Updates support attribte for army 
    def add_support(self, letter):
        for army in self.army_lst:
            if army.letter == letter:
                army.support += 1

    #Update support attribute 
    #Determine dead armies 
    def support(self, value):
        support_values = [army.support for army in value]
        armies = [army for army in value]
        support_tuples = list(zip(armies, support_values))
        max_value = max(tup[1] for tup in support_tuples)
        max_armies = []
        dead_armies = []
        for tup in support_tuples:
            if tup[1] == max_value:
                max_armies.append(tup[0])
            else:
                dead_armies.append(tup[0])
        if len(max_armies) > 1:
            dead_armies += max_armies
        for army in dead_armies:
            army.alive = False
    
    #Helper function to solve
    #Returns war results        
    def war_result(self):
        lst = []
        for army in self.army_lst:
            if army.alive == False:
                army.city = "[dead]"
            lst.append(army.letter + " " + army.city)
        w = "\n".join(item for item in lst)
        return w + "\n"
    
    #Solve the war and return the result
    def solve(self):
        self.move()
        d = self.set_city_dict()
        self.eval_war(d)
        result = self.war_result()
        return result

#Read in file 
#Split items for each line
#Create army object and return list of army objects
def diplomacy_read(r):
    r = r.split("\n")
    army_lst = []
    for s in r:
        if not s:
            continue
        army_letter, city, action = diplomacy_separate(s)
        army = Army(letter = army_letter, action = action, city = city)
        army_lst.append(army)
    return army_lst

#Seperate items for diplomacy_read
def diplomacy_separate(s):
    s = s.split()
    s = iter(s)
    army_letter, city, action = next(s), next(s), list(s)
    return army_letter, city, action

#Perform diplomacy and return result
def diplomacy_solve(r):
    army_lst = diplomacy_read(r)
    war = War(army_lst)
    result = war.solve()
    return result

        
                    
                        