# put your python code here
cinema_halls = int(input())
capacity = int(input())
planned_viewers = int(input())

can_hold = (cinema_halls * capacity) >= planned_viewers
print(can_hold)
