# Eduard Kosenko, 101480050

# 1.b
gym_member = "Alex Alliton"  # str
preferred_weight_kg = 20.5  # float
highest_reps = 25  # int
membership_active = True  # bool

# 1.c
#Dict of key: string, value: Tuple of 3 int values representing yoga, running, and weightlifting
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (10, 20, 30),
    "Taylor": (50, 45, 40)
}

#1.d
for member, stat in workout_stats.copy().items():
    workout_stats[member+"_total"] = sum(stat)

#1.e
#a list, containing lists of int values (3x3 matrix in this case)
workout_list = []
for stat in workout_stats.values():
    if type(stat) is tuple:
        workout_list.append(list(stat))

#1.f
yoga_running = [sum(stats[:2]) for stats in workout_list]
print("Yoga and Running minutes:")
for i in range(0, len(yoga_running)):
    #converting workout_stats keys to list to have an iterable list of names
    print(list(workout_stats.keys())[i], yoga_running[i])

weightlifting_last_two = [stats[2] for stats in workout_list[-2:]]
print("Weightlifting minutes for last two friends:")
for i in range(0, len(weightlifting_last_two)):
    # slicing workout_stats to get last 2 friend names
    print(list(workout_stats.keys())[1:3][i], weightlifting_last_two[i])

for member, total in workout_stats.items():
    if member.endswith("_total"):
        print(f'Total for: {member.removesuffix('_total')}: {total}')
        if total > 120:
            print(f"Great job staying active, {member}!")

#helper array
activities = ('Yoga', 'Running', 'Weightlifting')

friend_name = input("Enter a friends name: ")
if friend_name in workout_stats:
    print(f"Friend {friend_name} did:")
    for i in range(0, len(workout_stats[friend_name])):
        print(activities[i], workout_stats[friend_name][i])
else:
    print(f"Friend {friend_name} not found :(")

total_stats = [(member, total) for member, total in workout_stats.items() if member.endswith("_total")]
max_member = max(total_stats, key=lambda member_stat: member_stat[1])
print(f"Highest total workout: {max_member[0].removesuffix('_total')}, {max_member[1]} minutes")
min_member = min(total_stats, key=lambda member_stat: member_stat[1])
print(f"Lowest total workout: {min_member[0].removesuffix('_total')}, {min_member[1]} minutes")