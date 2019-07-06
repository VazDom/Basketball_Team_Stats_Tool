import constants
import os

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")


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


def main_menu():
	COMMANDS = ["Display Teams", "Help", "Quit"]
	for index, option in enumerate(COMMANDS, start = 1):
		print("{}) {}".format(index, option))
	print()


def team_menu():
	for index, team in enumerate(constants.TEAMS, start = 1):
		print('{}) {}'.format(index, team))


def team_info(team_opton):
	try:
		team = balanced_teams[team_opton -1]
		players_names = [player['name'] for player in team]
		experienced = len([player for player in team if player['experience'] == True])
		inexperienced = len([player for player in team if player['experience'] == True])
		print("\n\n{} Stats:".format(constants.TEAMS[team_opton -1]))
		print()
		print()
		print("{} Players: ".format(constants.TEAMS[team_opton -1]), end = '')
		for player in players_names:
			if player == players_names[-1]:
				print(player)
			else:
				print(player, end = ', ')
		print()
		print()
		print('{} experienced players'.format(experienced))
		print('{} inexperienced players'.format(inexperienced))
		print()
		input('Press enter to continue')
		clear_screen()

		
	except IndexError:
		print("\nThat is not a valid option. Please try again. \n")
		input('Press enter to continue')
		clear_screen()
	except ValueError:
		print("\nThat is not a valid option. Please try again. \n")
		input('Press enter to continue')
		clear_screen()


def main():
	clear_screen()
	while True:
		print("WELLCOME \n\n")
		main_menu()
		try:
			option = int(input('Choose an option >  '))
		except ValueError:
			print('Wrong input')
			input('Press enter to continue')
			clear_screen()
			continue
		print()
		if option == 1:
			team_menu()
			print()
			try:
				team_opton = int(input("Select your team >  "))
			except ValueError:
				print('Wrong input')
				input('Press enter to continue')
				clear_screen()
				continue
			team_info(team_opton)
			#pass
		elif option == 2:
			clear_screen()
			print('Team Stats will display a submenu to choose which team stats to display')
			print('Help will display this message')
			print('Quit will exit the program')
			input('Press enter to continue')
			clear_screen()
			continue
		elif option == 3:
			clear_screen()
			print('Ok good bye')
			break
		else:
			clear_screen()
			print("\nPlease this is not a valid option, try again\n")
			continue


if __name__ == "__main__":
	clear_screen()
	balanced_teams = team_selections(debug_data())
	main()