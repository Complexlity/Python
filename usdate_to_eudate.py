#This is one of the code coach puzzles
#It converts the date from us format to eu format
"""
There are two formats:
    1 - MM/DD/YYYY
    2 - MonthInWords DD, YYYY 
example:
    6/22/2021 --> 22/6/2021
    June 22, 2021 --> 22/6/2021
"""


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']
my_dic = {}
for num, month in enumerate(months):
    my_dic[month] = int(num) + 1

date = input()
counter = date.count('/')
date_list = date.split('/')

try:
    if all(i.isnumeric() for i in date_list):
            if all([int(date_list[1]) in range(1,32), int(date_list[0]) in range(1,13) , int(date_list[2]) > 1000]):
                new_date = f'{date_list[1]}/{date_list[0]}/{date_list[2]}'
                print(new_date)
            else:
                print('You put an invalid date ')

    else:
        method = date.split()
        method3 = method[1].rstrip(',')

        if all([method[0] in my_dic.keys(), int(method3) in range(1,32), int(method[2]) > 1000]):
                new_date = f'{method3}/{my_dic[method[0]]}/{method[2]}'
                print(new_date)
        else:
            print('You put an invalid date')

except IndexError:
    print('You didn\'t follow the proper format')
    print('''
There are two formats:
    1 - MM/DD/YYYY
    2 - MonthInWords DD, YYYY 
example:
    6/22/2021 --> 22/6/2021
    June 22, 2021 --> 22/6/2021
    ''')