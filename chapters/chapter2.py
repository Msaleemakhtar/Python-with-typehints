name:str = "Saleem"
fname:str = "Ghulam Muhammad"
age:int = 41
education:str = "Masters in Computer science"


card:str = '''
PIAIC Students Card
Student Name:{b}
fname: {c}
Age : {d}
Education : {a}
'''.format( a= education, b= name, c = fname, d =age)


print(card)