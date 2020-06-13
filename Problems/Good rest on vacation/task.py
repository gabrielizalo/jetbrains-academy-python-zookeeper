duration = int(input())
cost_food = int(input())
flight_cost = int(input())
night_cost = int(input())

total_required = (cost_food * duration) + (flight_cost * 2) + ((duration - 1) * night_cost)
print(total_required)
