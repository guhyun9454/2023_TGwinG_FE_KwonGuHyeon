class Subject:
    def __init__(self):
        self.score = None
        self.subject_name = None
        self.max_score = None

    def get_subject_name(self):
        return self.subject_name 

    def set_score(self, score):
        self.score = score

    def get_score(self):
        return self.score

    def get_max_score(self):
        return self.max_score

class Korean(Subject):
    def __init__(self):
        self.subject_name = "국어"
        self.max_score = 100

class Math(Subject):
    def __init__(self):
        self.subject_name = "수학"
        self.max_score = 100

class History(Subject):
    def __init__(self):
        self.subject_name = "역사"
        self.max_score = 50

class Student:
    def __init__(self, name):
        self.name = name
        self.kor = Korean()
        self.math = Math()
        self.his = History()
        self.subjects = [self.kor,self.math,self.his]


    def get_name(self):
        return self.name
    
    def make_sum(self):
        sum = 0
        for i in self.subjects:
            sum +=i.get_score()
        return sum
    
    def print(self):
        print(f"===== Student {self.get_name()} =====")
        for i in self.subjects:
            print(f"Score of {i.get_subject_name()} : {i.get_score()} / {i.get_max_score()}")

def print_rank(students):
    lst = []
    for i in students:
        lst.append([i.make_sum(),i])
    lst.sort(key=lambda x: x[0],reverse=True)
    for idx,j in enumerate(lst):
        print(f"Rank {idx+1} : {j[1].get_name()} ( {j[0]} / 250)")
    highest_score = 0









# 실행 함수 (수정하지 마세요. 코드 테스트용 함수입니다.)
def Test():
    n = int(input("How many students: "))

    students = []

    for i in range(n):
        name = input("Name of Student: ")

        student = Student(name)

        for subject in student.subjects:
            score = int(input("Score of %s : " %subject.get_subject_name()))
            subject.set_score(score)

        print()
        student.print()
        print()
        students.append(student)

    print("===== Rank =====")
    print_rank(students)

Test()