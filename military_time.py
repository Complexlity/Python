#This code converts time for the 12 hour format to the 24hr format

#input the values in this format: hh:mm AM\PM
#for example 1:23 PM, 12:35 AM

#Hit the Like and Upvote if you liked it. 
#Thank you

time = input()
try:
    timed = time.split()
    time = timed[0]
    ampm = timed[1]
    ampm = ampm.upper()
    timed = time.split(':')
    hour = timed[0]
    minute = timed[1]
    checker = minute[1]
    
    if any([not[int(hour) in range(1,13),int(minute) in range(1,61)]]):
        raise ValueError
    if ampm == 'PM' or ampm == 'AM':
        if ampm == 'PM':
            if int(hour) == 12:
                 hour = 12
            else:
                hour = int(hour) + 12
        elif int(hour) == 12:
            hour = '00'
        
    else:
        raise ValueError

    print(f'{hour}:{minute}')
   
   

except (IndexError, ValueError):
    print('You have entered a wrong format')
    print('Your input should be in this format: \nhh:mm AM\PM')
    print('for example:  1:23 PM, 12:35 AM')