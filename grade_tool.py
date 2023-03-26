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
# import pandas as pd 
from typing import * 


# 성적표 프로그램
class GradeWriterProgram:
    num: int = 0
    student_numbering: List = [] 
    
    def __init__(self) -> None:
        self.data: Dict[int, List[int, str, float]] = {self.num : [self.num, self.name, self.kor, self.eng, self.math, 
                                                                    self.sci, self.total_score(), self.average_score()]}
        self.num += 1
        self.student_numbering.append(self.data)

    def input_data(self):
        pass

    def total_score(self) -> int:
        total: int = self.kor + self.eng + self.math + self.sci
        return total

    def average_score(self) -> float:
        average: float = self.total_score() / 4
        return average
    
    def __show_logic(self, order) -> None:
        print("수험번호\t이름\t국어\t영어\t수학\t과학\t총합\t평균")
        print(f"{self.student_numbering[order][0][0]}\t\t{self.student_numbering[order][0][1]}\t{self.student_numbering[order][0][2]}\t{self.student_numbering[order][0][3]}\t{self.student_numbering[order][0][4]}\t{self.student_numbering[order][0][5]}\t{self.student_numbering[order][0][6]}\t{self.student_numbering[order][0][7]}")
    
    # [{0: [0, '유재석', 70, 80, 90, 80, 320, 80.0]}]
    def show_data(self) -> None:    
        # enumerate : 
        for index, _ in enumerate(self.student_numbering):
            self.__show_logic(index)

    def __search_logic(self, search) -> Union[Any, Literal[-1], None]:
        pr: int = len(self.student_numbering) - 1 
        pl: int = 0
        while True:
            pc: int = (pr - pl) // 2 
            
            if self.student_numbering[pc][search][0] == search:
                return self.student_numbering[search]
            elif self.student_numbering[pc][search][0] > search:
                pr = pc + 1 
            elif self.student_numbering[pc][search][0] < search:
                pl = pc - 1

            if pl > pr:
                break
            return -1
    
    def one_search_data(self):
        while True:
            search: int = int(input("수험번호를 입력해주세요! 종료를 원하시면 -2번을 눌러주세요: "))
            injection = self.__search_logic(search=search)

            if search == -2:
                print("종료합니다. 전 단계로 이동합니다")
                self.option_select()

            if injection == -1:
                print("없는 데이터 입니다 다시 확인해주세요")
                continue
            else:
                # 배열 위치에 따른 프린트? ex) list = 1 1번의 데이터를 
                self.__show_logic(search)
        
    def delete_data(self) -> None:
        dt: int = int(input("원하시는 번호를 입력해주세요!\n1. 전체 삭제\t2. 부분 삭제\n: "))
        if dt == 1:
            self.student_numbering.clear()
        elif dt == 2:
            dt_search: int = int(input("수험번호를 입력해주세요!"))
            self.student_numbering.pop(dt_search)
    
    def option_select(self) -> None:
        while True:
            # 번호를 입력하면 해당 메서드가 실행되도록 
            sel = int(input("원하시는 메뉴의 번호를 입력해주세요 : "))
            # 1. 성적 입력
            if sel == 1:
                self.input_data()
            # 2. 전체 보기
            elif sel== 2:
                self.show_data()
            # 3. 검색
            elif sel == 3:
                self.one_search_data()
            # 4. 삭제
            elif sel == 4:
                self.delete_data()
            # 5. CSV 파일 저장
            elif sel == 5:
                pass
            # 6. 종료하기
            elif sel == 6:
                break
            else:
                print("잘못 입력하셨습니다. 다시 입력해주세요.")
                continue
        
    


youjesuck = GradeWriterProgram().option_select()

# youjesuck.input_data()


# class SaveGradeDataInitailization(GradeWriterProgram):
#     pass