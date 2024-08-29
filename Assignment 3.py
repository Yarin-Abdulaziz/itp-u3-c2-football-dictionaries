Assignment 3
def group_players_by_country_and_position(squads_list):
    # Convert the list of player data to dictionaries
    players_dict_list = players_as_dictionaries(squads_list)
    
    # Create a dictionary to group players by country and then by position
    country_position_dict = {}
    
    for player in players_dict_list:
        country = player['country']
        position = player['position']
        
        if country not in country_position_dict:
            country_position_dict[country] = {}
        
        if position not in country_position_dict[country]:
            country_position_dict[country][position] = []
        
        country_position_dict[country][position].append(player)
    
    return country_position_dict
