import random
import secrets

from collections import defaultdict

#World Cup mini project -- helps randomly assign people teams not friendly yet; in terms of asking the user for amount of people and teams for each person

#global player_count
#global teams_per

def team_assign(x):
    the_names = {'Alex': 0, 'Angel': 1, 'Will': 2, 'Mark': 3, 'Chris': 4, 'Ian': 5, 'Tio Chuy': 6, 'Jon': 7, 'Dany': 8}
    pairs = ([x[i:i+2] for i in range(0, len(x), 2)]) #Takes the 18 teams and groups them in two's.
    a = [x for x in pairs] # Iterates through pairs.
    
    
    x = 0 # Used a stepper to help pair the keys of the dictionary with the indices of pairs.
    for i in the_names:
        the_names[i] = a[x]
        x+=1
    return the_names
        

def team_gen(): 
    #Generates 18 teams using a while loop, which can be adjusted depending on people involved.
    teams = ['Qatar', 'Ecuador', 'Senegal' ,'Netherlands', 'England' ,'Iran', 'USA', 'Wales' ,'Argentina', 'Saudi Arabia', 'Mexico', 'Poland' , 'France' ,'Australia' ,'Denmark','Tunisia', 'Spain', 'Costa Rica' ,'Germany', 'Japan', 'Belgium', 'Canada', 'Morocco' ,'Croatia' ,'Brazil', 'Serbia','Switzerland' ,'Cameroon' ,'Portugal' ,'Ghana', 'Uruguay','South Korea']
    
    two_teams = []
    #list where the 18 teams are stored and what is returned.
    
    i = 0
    while i < 18: # Adjustable depending of how many teams you want.
        x = secrets.choice(teams) # Could of used random but wanted an excuse to explore the secrets module.
        two_teams.append(x)
        
        for j in two_teams:
            if j in teams:
                teams.remove(j)
        
        i+=1
    return two_teams
        
    
    

def main():
    x = team_gen()# team generator is called and stored in variable x. x is a list of 18 teams.
    
    b = team_assign(x)  # The 18 team list is passed to the team assign function and returned as a dictionary containing the 18 teams divided into x players.
    
    for i in b.items(): #Used to present the final results vertically rather than horizontally.
        print(i)
        
          
main()





    
    