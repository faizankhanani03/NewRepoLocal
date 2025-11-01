# oop practice

class Student:
    def __init__ (self,name,marks):
        self.name = name
        self.marks = marks 
    def avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("hi" , self.name , "your avg score would be:" , sum/3)
s = Student('tony kakar' , [89,99,87])
s.avg()
