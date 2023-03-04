#Hello, Welcome the quiz
#This quiz asks for the capital of various popular countries and vice versa

#IMSTRUCTION
'''Enter the number of questions you want to see/answer'''

#At the bottom of the code there are three main functions:

''' 1. answers_only() - Which prints questions with the answers ticked
    
    2. for_sololearners() - Computer answers the questions randomly (because sololearn IDE cannot take inputs effectively)
    
    3. for_IDEandCodeEditors() - This is the main quiz where you answer the questions and could be run in any IDE or CODE Editors
'''

# ❌ signify the one you (or the computer) picked
# ✅ signify the correct answer
# ✅✅ is shown if you(or the computer) picked the correct answer

#for_sololearners is run by default, uncomment which ever one you want 
#Goodluck and don't forget to hit like and share thanks 🤗

from copy import copy as c
import random
global countries , capital,  capitals, _list, num_of_questions 

capitals = {'Germany': 'Berlin','India': 'New Delhi','Israel':'Jerusalem','Italy':'Rome','Japan':'Tokyo','SouthKorea':'Seoul','Mexico':'MexicoCity','Netherlands':'Amsterdam','Norway':'Oslo','Portugal':'Lisbon','Qatar':'Doha','Romania':'Bucharest','Russia':'Moscow','South Africa': 'Pretoria','Spain':'Madrid','Syria': 'Damascus','Togo':'Lome','Ukraine':'Kiev','United Arab Emirates':'Abu Dhabi','United Kingdom': 'London','Argentina': 'Buenos Aires','Australia':'Canberra','Belgium':'Brussels','Brazil':'Brasilia','China':'Beijing','Colombia':'Bogota','Croatia':'Zagreb','Denmark': 'Copenhagen','Egypt': 'Cairo','Nigeria': 'Abuja','USA': 'Washington DC','Ghana': 'Accra','France': 'Paris'}

option = ['A', 'B', 'C', 'D']

num_of_questions = int(input('how many questions do you want: '))
print(num_of_questions)

def utilities():
    global new, new1, countries, capital, _list
    new = [a for a in range(50)]
    new1 = [b for b in range(50)]
    countries = list(capitals.keys())
    random.shuffle(countries)
    capital = list(capitals.values())
    random.shuffle(capital)
    _list = [find_countries, find_capitals]



def getKey(value):
            for key, values in capitals.items():
                if value == values:
                    return key



def find_capitals():
    global new
    j = new.pop(0)
    solution = countries[j]
    question  = f'What is the capital of {solution}?\n'
    correct = capitals[solution]
    del capital[capital.index(correct)]
    wrong = random.sample(capital, 3)
    wrong.append(correct)
    random.shuffle(wrong)
    return [question, correct, wrong]



def find_countries(): 
    global new1
    k = new1.pop(0)
    solution = capital[k]
    question = f'What Country is {solution} the capital of?\n'
    correct = getKey(capital[k])
    del countries[countries.index(correct)]
    wrong = random.sample(countries, 3)
    options = wrong + [correct]
    random.shuffle(options)
    return [question, correct, options]



def chooser():
    global _list
    func = random.choice(_list)
    try:
        func = func()
    except (IndexError, ValueError):
        _list.remove(func)
        try:
            func = _list[0]
            func = func()
        except:
            utilities()
            func = random.choice(_list)
            func = func()
    return func



def answers_only():
    utilities()
    print('')
    for a in range(num_of_questions):
        func = chooser()
        n = 0
        print(f'{a+1}. {func[0]}')
        answer = func[1]
        for i in option:
            solution = func[2][n]
            value = f'\t{i}. {solution}'
            if solution == answer:
                value += ' ✅'
            print(value, end = '\n\n')
            n += 1   



def for_sololearners():
    your_score = 0
    utilities()
    all_solutions = ''

    print()

    for a in range(num_of_questions):
        func = chooser()
        n = 0
        string = f'{a+1}. {func[0]}\n'
        solutions = c(string)
        answer = func[1]
        values = {}
        values1 = []

        for i in option:
            solution = func[2][n]
            value = f'\t{i}. {solution}'
            values1.append(value)
            string += value + '\n'
            value1 = ''.join(value.strip().split('.')).split()
            values[value1[0]] = value1[1]
            n += 1    
        print(string, '\n')
        user_solution = random.choice(['A', 'B', 'C', 'D'])
        user_answer = values[user_solution]
        values2 = values1.copy()
        for options in values2:
            index = values2.index(options)
            if answer in options:
                options += ' ✅'
                if user_answer == answer:
                    your_score += 1
                    options +=  '✅'
            elif user_answer in options and user_answer: 
                options += ' ❌'
            values1[index] = options



        for named in values1:
            solutions += named + '\n'
        all_solutions += solutions + '\n'


    print(f'Sololearn Engine scored {your_score} out of {num_of_questions}\nSee it\'s picked answers and the correct answers below 👇')
    print('\nSOLUTIONS'.center(45))
    print('-' * 9)
    print(all_solutions)
    


def for_IDEandCodeEditors():
    your_score = 0
    utilities()
    all_solutions = ''
    

    for a in range(num_of_questions):
        func = chooser()
        n = 0
        string = f'{a+1}. {func[0]}\n'
        solutions = c(string)
        answer = func[1]
        values = {}
        values1 = []

        for i in option:
            solution = func[2][n]
            value = f'\t{i}. {solution}'
            values1.append(value)
            string += value + '\n'
            value1 = ''.join(value.strip().split('.')).split()
            values[value1[0]] = value1[1]
            n += 1    
        print(string, '\n')


        while True:
            try:
                user_solution = input('Enter the correct option: ').upper()
                user_answer = values[user_solution]
                break
            except:
                print('Your Put an invalid option!. TRY AGAIN')
                print('Enter options one of A,B,C,D (not case sensitive)')
      
        values2 = values1.copy()
        for options in values2:
            index = values2.index(options)
            if answer in options:
                options += ' ✅'
                if user_answer == answer:
                    your_score += 1
                    options +=  '✅'
            elif user_answer in options and user_answer: 
                options += ' ❌'
            values1[index] = options



        for named in values1:
            solutions += named + '\n'
        all_solutions += solutions + '\n'


    print(f'You scored {your_score} out of {num_of_questions}')
    print('\nSOLUTIONS'.center(45))
    print('-' * 9)
    print(all_solutions)
    



#answers_only()
for_sololearners()
# for_IDEandCodeEditors()
