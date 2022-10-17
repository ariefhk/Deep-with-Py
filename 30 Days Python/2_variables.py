# 1. Print sentences
print('Day 2: 30 days of python programming')

# 2. name
first_name = 'arief rachman'
last_name = 'hakim'
fullname = f'{first_name} {last_name}'
country = 'Indonesia'
city = 'Ciamis'
age = 20
is_married = False
is_male = True
hobby, foodLikes = 'coding', 'fried chicken'
skills = ['Javascript', 'React', 'Python', 'Nodejs']
person_info = {
    'firstname': first_name,
    'lastname': last_name,
    'country': country,
    'city': city
}


# 3. check
print(type(fullname))
print(type(age))
print(type(is_male))
print(type(skills))
print(type(person_info))


angka = [1, 2, 3, 4, 5]

numPlusTwo = list(map(lambda x: x+2, angka))
print(numPlusTwo)
