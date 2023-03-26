people = [
    {"name": "Harry", "house": "griffindor"},
    {"name": "Dracoy", "house": "sylinderin"}
]


#instead of doing this we can just use the lambda
# def f(person):
#     return person["name"]


people.sort(key=lambda person: person["name"])

print(people)