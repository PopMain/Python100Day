class Student(object):
    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.__passsword = password

    def study(self, course_name):
        print("%s正在学习%s。" % (self.name, course_name))

    def __printPassword(self):
        print(self._Student__passsword)

    def test(self): 
        self._Student__printPassword()

if __name__ == '__main__':
    stu1 = Student('Jensen', 38, 1234)
    stu1.study('Python')
#    print(stu1.__passsword)
#    stu1.__printPassword()
    stu1.test()
