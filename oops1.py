class student:
    def __init__(self,name,rno):
        self.sname=name
        self.roll_num=rno
    def display(self):
        print(f"name is {self.sname} and roll number is {self.roll_num}")

s1=student("Prasanth",3)
s2=student("Neha",17)
print("student 1 details are:")
s1.display()
print("student 2 details are:")
s2.display()
