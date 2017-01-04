class Student:
    next_id = 1
    def __init__(self, name):
        self.name = name
        self.student_id = Student.next_id
        Student.next_id += 1

    def __str__(self):
        return "{}, id = {}".format(self.name, self.student_id)
john = Student("John")
print(john)

jane = Student("Jane")
print(jane)

ann = Student("Ann")
print(ann)
