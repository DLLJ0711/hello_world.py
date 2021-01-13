day = int(input('Day (0-6)? '))

if day in range(1, 5):
    print('Get up lazy!')
elif day == 0 or 6:
    print('Stay in night-night land!')