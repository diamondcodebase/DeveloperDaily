import random
import time
import math

round = 0
concentration = random.randrange(1,3)
knowledgeAndSkills = {1, 10}
skillRequired = random.randrange(1, 20)
concentrationRequired = random.randrange(5, 10)
success = False

# this function helps developer increasing concentration given that concentration smaller than 10
def EnjoyCoffee():
    global concentration
    if concentration < 10:
        concentration += 1
        print(f"Developer takes a sip of nice coffee~, Concentration level: {concentration}")
    else:
        print("Concentration level: 10 (max level)")       

# this function helps developer gaining new skills to the skill set, number of possible new skills depends on learning ability, in turn concentration
def DoResearch():
    global concentration
    learningAbility = math.floor(concentration/2)
    for x in range(1, learningAbility):
       newSkill = random.randint(1, 20)
       knowledgeAndSkills.add(newSkill)       
    print(f"Developer studies case of possible solution/trick through Google/ChatGPT, skill set now is {knowledgeAndSkills}")

# this function determines whether developer has enough concentration and proper skill to complete the task  
def TrialAndError():
    global round
    round += 1
    print(f"Round {round}, fight!")
    time.sleep(3)
    if skillRequired in knowledgeAndSkills and concentrationRequired <= concentration:
        print("Task completed!")
        return True
    else:
        print("Fail... try again~\n")
        return False

# this function just give thanks, called after the task completion
def GiveThanks():
    print("Developer makes it finally~!! Give thanks with grateful heart~!")


# this function prints out the task and developer initial status 
def TaskStart():
    print(f"This task required skill {skillRequired}, concentration {concentrationRequired}. Let do it~")
    print(f"Currently, developer's skill set is {knowledgeAndSkills} and concentration {concentration}")


TaskStart()

while not success:
    EnjoyCoffee()
    DoResearch()
    success = TrialAndError()
GiveThanks()
