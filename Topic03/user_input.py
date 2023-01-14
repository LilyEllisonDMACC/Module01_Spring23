#Get user age
user_age = input('Please enter your age: ')

#cast age to int and add 25
age_in_25_years = int(user_age) + 25

#cast age in 25 years as str
print('In 25 years you will be age: ' + str(age_in_25_years))

#one_liner
print('In 25 years you will be age: ' + str(int(input('Please enter your age: ')) + 25))