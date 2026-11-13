class Student: 
    def __init__(self, name):
        self.name = name

    def introduce (self):
        return f" I am{self.name}"


student = Student("John")
print(student.introduce())
  