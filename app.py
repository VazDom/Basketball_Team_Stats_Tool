import constants
import os


def debug_data():
	players = constants.PLAYERS[:]

	for player in players:
		player['height'] = player['height'].split()
		player['height'] = int(player['height'][0])
		player['guardians'] = player['guardians'].split(" and ")
		if player['experience'] == 'YES':
			player['experience'] = True
		else:
			player['experience'] = False
	return players


def team_selections(players):
	Panthers = []
	Bandits = []
	Warriors = []
	exp_player = []
	nonexp_player = []

	for player in players:
		if player['experience']:
			exp_player.append(player)
		else:
			nonexp_player.append(player)
	while exp_player:
		Panthers.append(exp_player.pop())
		Bandits.append(exp_player.pop())
		Warriors.append(exp_player.pop())
	while nonexp_player:
		Panthers.append(nonexp_player.pop())
		Bandits.append(nonexp_player.pop())
		Warriors.append(nonexp_player.pop())
	balanced_teams = [Panthers, Bandits, Warriors]

	return balanced_teams
