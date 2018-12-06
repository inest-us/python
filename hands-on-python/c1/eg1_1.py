def addPick(cue, dict):
    str = 'Enter an example for ' + cue + ': '
    response = input(str)
    dict[cue] = response

def tellStory(): 
    userPicks = dict() 
    addPick('animal', userPicks) 
    addPick('food', userPicks) 
    addPick('city', userPicks) 
    print(userPicks)

tellStory()

