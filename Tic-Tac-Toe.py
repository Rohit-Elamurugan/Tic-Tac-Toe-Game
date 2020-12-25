def check(array):
    for i in range(3):
        if array[i,0] == array[i,1] == array[i,2]:
            if array[i,0] != '-':
                return array[i,0]
    for i in range(3):
        if array[0,i] == array[1,i] == array[2,i]:
            if array[0,i] != '-':
                return array[0,i]
    if (array[0,0] == array[1,1] == array[2,2]) or (array[0,2] == array[1,1] == array[2,0]):
        if array[1,1] != '-':
            return array[1,1]
    return False

import numpy
import random

winner = ''
marked = ''
human = '-'
arr = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
places = []

while human != 'O' and human != 'X':
    human = input('X or O: ')
    computer = 'O' if human == 'X' else 'X'

print(arr)

while '-' in arr:
    while True:
        try:
            place = int(input('Place: '))
            break
        except:
            continue
    if place not in places:
        
        if place == 1:
            arr[2,0] = human
        if place == 2:
            arr[2,1] = human
        if place == 3:
            arr[2,2] = human
        if place == 4:
            arr[1,0] = human
        if place == 5:
            arr[1,1] = human
        if place == 6:
            arr[1,2] = human
        if place == 7:
            arr[0,0] = human
        if place == 8:
            arr[0,1] = human
        if place == 9:
            arr[0,2] = human

        if len(places) != 0:
            if place == 1:
                if places[-1] == 4 and arr[0,0] == '-':
                    arr[0,0] = computer
                elif places[-1] == 5 and arr[0,2] == '-':
                    arr[0,2] = computer
                elif places[-1] == 2 and arr[2,2] == '-':
                    arr[2,2] = computer
                elif places[-1] == 7 and arr[1,0] == '-':
                    arr[1,0] = computer
                elif places[-1] == 9 and arr[1,1] == '-':
                    arr[1,1] = computer
                elif places[-1] == 3 and arr[2,1] == '-':
                    arr[2,1] = computer
                else:
                    if arr[2,1] == human and arr[0,1] == '-':
                        arr[0,1] = computer
                    elif arr[1,0] == human and arr[1,2] == '-':
                        arr[1,2] = computer
                    
            if place == 2:
                if places[-1] == 1 and arr[2,2] == '-':
                    arr[2,2] = computer
                elif places[-1] == 3 and arr[2,0] == '-':
                    arr[2,0] = computer
                elif places[-1] == 5 and arr[0,1] == '-':
                    arr[0,1] = computer
                elif places[-1] == 8 and arr[1,1] == '-':
                    arr[1,1] = computer
                else:
                    x = random.choice([0,1])
                    y = random.choice([0,2])
                    while arr[x,y] != '-':
                        x = random.choice([0,1])
                        y = random.choice([0,2])
                    arr[x,y] = computer
                    
            if place == 3:
                if places[-1] == 6 and arr[0,2] == '-':
                    arr[0,2] = computer
                elif places[-1] == 5 and arr[0,0] == '-':
                    arr[0,0] = computer
                elif places[-1] == 2 and arr[2,0] == '-':
                    arr[2,0] = computer
                elif places[-1] == 7 and arr[1,1] == '-':
                    arr[1,1] = computer
                elif places[-1] == 9 and arr[1,2] == '-':
                    arr[1,2] = computer
                elif places[-1] == 1 and arr[2,1] == '-':
                    arr[2,1] = computer
                else:
                    if arr[2,1] == human and arr[0,1] == '-':
                        arr[0,1] = computer
                    elif arr[1,2] == human and arr[1,0] == '-':
                        arr[1,0] = computer
                
            if place == 4:
                if places[-1] == 7 and arr[2,0] == '-':
                    arr[2,0] = computer
                elif places[-1] == 1 and arr[0,0] == '-':
                    arr[0,0] = computer
                elif places[-1] == 5 and arr[1,2] == '-':
                    arr[1,2] = computer
                elif places[-1] == 6 and arr[1,1] == '-':
                    arr[1,1] = computer
                else:
                    x = random.choice([0,2])
                    y = random.choice([1,2])
                    while arr[x,y] != '-':
                        x = random.choice([0,2])
                        y = random.choice([1,2])
                    arr[x,y] = computer
                
            if place == 5:
                if places[-1] == 2 and arr[0,1] == '-':
                    arr[0,1] = computer
                elif places[-1] == 4 and arr[1,2] == '-':
                    arr[1,2] = computer
                elif places[-1] == 6 and arr[1,0] == '-':
                    arr[1,0] = computer
                elif places[-1] == 8 and arr[2,1] == '-':
                    arr[2,1] = computer
                elif places[-1] == 1 and arr[0,2] == '-':
                    arr[0,2] = computer
                elif places[-1] == 3 and arr[0,0] == '-':
                    arr[0,0] = computer
                elif places[-1] == 7 and arr[2,2] == '-':
                    arr[2,2] = computer
                elif places[-1] == 9 and arr[2,0] == '-':
                    arr[2,0] = computer
                else:
                    x = random.choice([0,1,2])
                    y = random.choice([0,1,2])
                    while arr[x,y] != '-':
                        x = random.choice([0,1,2])
                        y = random.choice([0,1,2])
                    arr[x,y] = computer
                
            if place == 6:
                if places[-1] == 9 and arr[2,2] == '-':
                    arr[2,2] = computer
                elif places[-1] == 3 and arr[0,2] == '-':
                    arr[0,2] = computer
                elif places[-1] == 5 and arr[1,0] == '-':
                    arr[1,0] = computer
                elif places[-1] == 4 and arr[1,1] == '-':
                    arr[1,1] = computer
                else:
                    x = random.choice([0,2])
                    y = random.choice([0,1])
                    while arr[x,y] != '-':
                        x = random.choice([0,2])
                        y = random.choice([0,1])
                    arr[x,y] = computer

            if place == 7:
                if places[-1] == 8 and arr[0,2] == '-':
                    arr[0,2] = computer
                elif places[-1] == 4 and arr[2,0] == '-':
                    arr[2,0] = computer
                elif places[-1] == 5 and arr[2,2] == '-':
                    arr[2,2] = computer
                elif places[-1] == 3 and arr[1,1] == '-':
                    arr[1,1] = computer
                elif places[-1] == 9 and arr[0,1] == '-':
                    arr[0,1] = computer
                elif places[-1] == 1 and arr[1,0] == '-':
                    arr[1,0] = computer
                else:
                    if arr[0,1] == human and arr[2,1] == '-':
                        arr[2,1] = computer
                    elif arr[1,0] == human and arr[1,2] == '-':
                        arr[1,2] = computer

            if place == 8:
                if places[-1] == 9 and arr[0,0] == '-':
                    arr[0,0] = computer
                elif places[-1] == 7 and arr[0,2] == '-':
                    arr[0,2] = computer
                elif places[-1] == 5 and arr[2,1] == '-':
                    arr[2,1] = computer
                elif places[-1] == 2 and arr[1,1] == '-':
                    arr[1,1] = computer
                else:
                    x = random.choice([1,2])
                    y = random.choice([0,2])
                    while arr[x,y] != '-':
                        x = random.choice([1,2])
                        y = random.choice([0,2])
                    arr[x,y] = computer

            if place == 9:
                if places[-1] == 6 and arr[2,2] == '-':
                    arr[2,2] = computer
                elif places[-1] == 5 and arr[2,0] == '-':
                    arr[2,0] = computer
                elif places[-1] == 8 and arr[0,0] == '-':
                    arr[0,0] = computer
                elif places[-1] == 7 and arr[0,1] == '-':
                    arr[0,1] = computer
                elif places[-1] == 3 and arr[1,2] == '-':
                    arr[1,2] = computer
                elif places[-1] == 1 and arr[1,1] == '-':
                    arr[1,1] = computer
                else:
                    if arr[0,1] == human and arr[2,1] == '-':
                        arr[2,1] = computer
                    elif arr[1,2] == human and arr[1,0] == '-':
                        arr[1,0] = computer
        
        else:
            x = random.randint(0,2)
            y = random.randint(0,2)
            while arr[x,y] != '-':
                x = random.randint(0,2)
                y = random.randint(0,2)
            arr[x,y] = computer
                
        print(arr)
        
        if check(arr) != False:
            winner = check(arr)
            print(check(arr),'won')
            break
        
        places.append(place)
    else:
        print('Try again')
quit()
