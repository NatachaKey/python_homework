#task1
def hello():
    return 'Hello!'
print(hello())

#task2
def greet(name):
    return f'Hello, {name}!'
print(greet('Vasya'))

#task3

def calc(valueOne, valueTwo, action='multiply'):
    try:
        if action=='add':
            return valueOne + valueTwo
        elif action=='subtract':
            return valueOne-valueTwo
        elif action== 'multiply':
            return valueOne*valueTwo
        elif action =='divide':
            return valueOne/valueTwo
        elif action =='modulo':
            return valueOne%valueTwo
        elif action == 'int_divide':
            return valueOne//valueTwo
        elif action == 'power':
            return valueOne**valueTwo
        
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

#task4
def data_type_conversion(value, dataType):
    try:
        if dataType == 'float':
            return float(value)
        elif dataType == 'str':
            return str(value)
        elif dataType == 'int':
            return int(value)
    except ValueError:
        return f"You can't convert {value} into a {dataType}."
data_type_conversion('banana', 'int')

#task5
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    except TypeError:
        return 'Invalid data was provided.'
    
#task6
def repeat(string, count):
    output=''
    for i in range(count):
        output+= string
    return output
print(repeat('hello',2))

#task7

def student_scores(position, **kwargs):
    if position == "best":
        best_student = None
        highest_score = 0  
        
        for student, score in kwargs.items():
            if score > highest_score:
                highest_score = score
                best_student = student
        return best_student
    
    elif position == "mean":
        average_score = sum(kwargs.values()) / len(kwargs)
        return average_score
    else:
        return "Invalid score type. Use 'best' or 'mean'."
print(student_scores("best", John=85, Alice=92, Bob=78))    
    
#task8
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    # Split the string into a list of words
    words = string.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        elif word.lower() not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()  
    return " ".join(words)

#task9
def hangman(secret, guess):
    result=''
    for i in secret:
        if i in guess:
            result +=i
        else:
            result+='_'
    return result

print(hangman("alphabet",'ab'))


#task10
def pig_latin(string):
    result = []
    vovel = 'aeuio'
    string=string.split(" ")
    for i in string:
        if i[0] in vovel:
            i = i+ 'ay'
        elif i[0]=="q" and i[1]=="u":
            i= i[2:]+"quay"
        elif i[0] not in vovel and i[1]=="q" and i[2]=="u":
            i=i[3:]+i[0]+i[1]+i[2]+"ay"
        elif i[0] and i[1] not in vovel:
            i=i[2:]+i[0]+i[1]+"ay"     
        else:
            i=i[1:]+i[0]+"ay"
        result.append(i)    
    return " ".join(result)
print(pig_latin("squere"))




