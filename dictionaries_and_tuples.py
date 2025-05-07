# 1. Create and print a team role dictionary.
def sanakirja_team_1():
    team = {
        'Jukka': 'software developer',
        'Anne': 'project manager',
        'Susanna': 'software developer',
        'Aliisa': 'lead developer'
    }
    print(team)

sanakirja_team_1()


# 2. Print team members in original and sorted order.

def sanakirja_team_2():
    team = {
        "Jukka": "software developer",
        "Anne": "project manager",
        "Susanna": "software developer",
        "Aliisa": "lead developer"
    }

    for name in team:
        print(name, end=' ')
    print()

    for name in sorted(team):
        print(name, end=' ')
    print()

sanakirja_team_2()