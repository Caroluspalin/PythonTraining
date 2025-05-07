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


# 3. Ask for a team member name and print their role. Loop until "quit".

def sanakirja_team_3():
    team = {
        "Jukka": "software developer",
        "Anne": "project manager",
        "Susanna": "software developer",
        "Aliisa": "lead developer"
    }

    while True:
        name = input("Anna nimi (quit lopettaa): ")
        if name == "quit":
            break
        if name in team:
            print(f"{name} : titteli on {team[name]}")
        else:
            print(f"{name} : ei kuulu joukkueeseen")

sanakirja_team_3()
