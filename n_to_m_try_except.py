try:
    startFrom = int(input('Start From (1-10): '))
    endOn = int(input('End On (1-10): '))
except ValueError:
    print('Please input a number.')
    startFrom = int(input('Start From (1-10): '))
    endOn = int(input('End On (1-10): '))

while(startFrom <= endOn):
    print(startFrom)
    startFrom +=1

    