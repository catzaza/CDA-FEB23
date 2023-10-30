# sets 1
football_team = {"Alice", "Bob", "Charlie", "David"}
soccer_team = {"Charlie", "Eva", "Frank", "David"}

print("Introducing players of the football team:")
for player in football_team:
    print(player)

print("\nIntroducing players of the soccer team:")
for player in soccer_team:
    print(player)

union_teams = football_team.union(soccer_team)
print("\nDemonstrating a Union of two sets:")
print("Union of both teams:", union_teams)

soccer_not_in_football = soccer_team.difference(football_team)
print("\nDifference between soccer and football teams:")
print("Players in soccer but not in football:", soccer_not_in_football)

football_not_in_soccer = football_team.difference(soccer_team)
print("\nDifference between football and soccer teams:")
print("Players in football but not in soccer:", football_not_in_soccer)

# 2
empty = set()

while True:
    user_input = input("Enter a value to add to the set (or 'exit' to stop): ")
    if user_input.lower() == 'exit':
        break
    else:
        empty.add(user_input)

print("Updated set:", empty)

# 3
soccer_team = {"Charlie", "Eva", "Frank", "David"}

user_input = input("Enter a player's name to delete from the soccer team: ")

if user_input in soccer_team:
    soccer_team.discard(user_input)
    print(f"{user_input} has been removed from the soccer team.")
    print("Updated soccer team:", soccer_team)
else:
    print(f"{user_input} is not in the soccer team.")

# 4 
football_team = {"Alice", "Bob", "Charlie", "David"}
soccer_team = {"Charlie", "Eva", "Frank", "David"}

football_team.clear()
soccer_team.clear()

print("Football Team after clearing:", football_team)
print("Soccer Team after clearing:", soccer_team)

empty = set()

empty.clear()

print("Empty set after clearing:", empty)
