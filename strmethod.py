class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"Person's name={self.name} age= {self.age}"


person1 = person("viraj",20)
print(person1)
