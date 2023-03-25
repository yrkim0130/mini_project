"""
1. 성적 입력
    1. 번호 / 이름 / 국 / 영 / 수 / 과 / 총합 / 평균
2. 전체 보기
    1. 여러 학생
3. 검색
    1. 한 학생 성적 한 줄 조회
4. 삭제
    1. 전체 삭제
    2. 부분 삭제
5. CSV 파일 저장
"""
# import random
# import pandas as pd 


# 성적표 프로그램
class GradeWriterProgram:
    # num = -1
    
    def __init__(self, name: str, kor: int, eng: int, math: int, sci: int) -> None:
        # self.num = random.randint(1, 100)
        # self.num += 1
        self.num = 0
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.sci = sci
        self.student: list= []
        self.student = {self.num: [self.num+1, self.name, self.kor, self.eng, self.math, self.sci, self.total_score(), self.average_score()]}
        print(self.student)
        self.num += 1
    
    
    def total_score(self) -> int:
        total: int = self.kor + self.eng + self.math + self.sci
        return total


    def average_score(self) -> float:
        average: float = self.total_score() / 4
        return average
    
    # def input_data(self) -> list:
    #     student: list= []
    #     student = {self.num : [self.num, self.name, self.kor, self.eng, self.math, self.sci, self.total_score(), self.average_score()]}
    #     return student
    
    def show_data(self) -> None:    
        print("수험번호\t이름\t국어\t영어\t수학\t과학\t총합\t평균")
        print(f"{self.student[0][0]}\t\t{self.student[0][1]}\t{self.student[0][2]}\t{self.student[0][3]}\t{self.student[0][4]}\t{self.student[0][5]}\t{self.student[0][6]}\t{self.student[0][7]}")


    def search_data(self):
        search: int = int(input("수험번호를 입력해주세요! : "))
        # if search 
        pass 


    def delete_data(self):
        pass


youjesuck = GradeWriterProgram("유재석", 70, 80, 90, 80)
youjesuck = GradeWriterProgram("김영록", 50, 60, 100, 20)

# youjesuck.input_data()
youjesuck.show_data()


# class SaveGradeDataInitailization(GradeWriterProgram):
#     pass