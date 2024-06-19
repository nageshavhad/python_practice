# class student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(" adding new student in database")


# s1 = student("Nagesh", 29)
# print(s1.name, s1.age)

# s2 = student("Ganesh", 31)
# print(s2.name, s2.age)


class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            print(self.marks,"your avg score is:", sum/3)

s1 = student("nagesh", [32, 43, 65])
s1.get_avg()