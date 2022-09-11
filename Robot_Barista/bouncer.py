def age_validation(age: int, name: str):
    if age < 16:
        print('We are sorry, ' + name + ' we do not have anything for you here.')
        exit()

def validate_input_age(name):
    age = input('What is your age, ' + name + '?\n')
    try:
        age = int(age)                                                                
        age_validation(age, name)                                                
        if age <= 0:
            print('The value is not correct, only positive numbers are allowed.')
            return validate_input_age(name)
        return age
    except ValueError:
        print('The value is not correct, only numbers are allowed.')
        return validate_input_age(name)

def evil_status(name):
    if (name == 'ben') or (name == 'pat'):
        evilst = input('Are you evil?\n').lower()
        if evilst == 'no':
            print('Oh, come on in!')
        elif evilst == 'yes' and 4 <= int(input('How many good deeds have you done today?\n')):
            print('All right, you can have a coffee.')
        else: 
            print('No coffee for you!.')
            exit()
