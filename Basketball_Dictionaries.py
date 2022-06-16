# Challenge 1: Update the Constructor
class Player:
    def __init__(self, info):
        self.name = info["name"]
        self.age = info["age"]
        self.position = info["position"]
        self.team = info["team"]
        
# Ninja Bonus: Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects.
@classmethod
def get_team(cls, team_list):
	player_list = []

	for user in team_list:
		player_list.append(cls(user))
	return player_list

# Challenge 2: Create instances using individual player dictionaries.
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)
print(player_kevin)
print(player_jason)
print(player_kyrie)


# Challenge 3: Make a list of Player instances from a list of dictionaries
players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
]

new_team = []

for player in players:
	new_team.append(player)
print(new_team)


