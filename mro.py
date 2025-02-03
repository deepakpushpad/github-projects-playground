class parent1 :
    def hello(self):
        print("Hello from parent1") 

class parent2 :
    def hello(self):
        print("Hello from parent2")

class child(parent2, parent1):
    pass


obj=child()

obj.hello() # It will call the hello() method of the second parent class it encounters in the MRO (Method Resolution Order) which is parent1.



