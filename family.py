class Family():
    def __init__(self,name,age,relation):
        self.name = name
        self.age = age
        self.relation = relation

    def eating(self):
        print("Let's have lunch together")
        

        
son1 = Family("Alp",13,"son")
print(son1.age)
son2 = Family("Eren",13,"son")
print(son2.age)
father = Family("Mehmet", 50, "father")
print(father.age)
mother = Family("Esra", 50, "mother")
print(mother.age)
print(mother.eating())

print(son1.name)
print(son2.name)
print(mother.name)
print(father.name)

