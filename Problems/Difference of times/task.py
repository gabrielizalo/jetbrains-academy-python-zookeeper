first_hours = int(input())
first_minutes = int(input())
first_seconds = int(input())
second_hours = int(input())
second_minutes = int(input())
second_seconds = int(input())
elapsed_hours = second_hours - first_hours
elapsed_minutes = second_minutes - first_minutes
elapsed_seconds = second_seconds - first_seconds
total_elapsed_seconds = elapsed_seconds + (elapsed_minutes * 60) + (elapsed_hours * 60 * 60)
print(total_elapsed_seconds)
