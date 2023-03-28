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

from typing import * 
import pandas as pd
# import random

# 성적표 프로그램
class GradeWriterProgram:
    num: int = 0
    student_numbering: List = [] 
    
    # 0. 생성자
    # def __init__(self) -> None:
    #     self.data: Dict[int, List[int, str, float]] = {self.num : [self.num, self.name, self.kor, self.eng, self.math, 
    #                                                                 self.sci, self.total_score(), self.average_score()]}
    #     self.num += 1
    #     self.student_numbering.append(self.data)

    # 총합
    def total_score(self, kor: int, eng: int, math: int, sci: int) -> int:
        total: int = kor + eng + math + sci
        return total

    # 평균
    def average_score(self, value) -> float:
        average: float =  value / 4
        return average
    
    # 성적 입력 로직
    def __input_logic(self) -> None:
        name: str = input("이름 : ")
        kor: int = int(input("국어 : "))
        eng: int = int(input("영어 : "))
        math: int = int(input("수학 : "))
        sci: int = int(input("과학 : "))

        total: int = self.total_score(kor, eng, math, sci)
        data: Dict[int, List[int, str, float]] = {self.num : [self.num, name, kor, eng, math, 
                                                            sci, total, self.average_score(total)]}
        self.num += 1
        self.student_numbering.append(data)
    
    # 1. 성적 입력
    def input_data(self) -> None:
        while True:
            try:
                search: int = int(input("1번을 눌러 성적을 입력해주세요.\n종료를 원하시면 -2번을 눌러주세요.\n: "))
    
                if search == 1:
                    self.__input_logic()
                    print(self.student_numbering)
                elif search == -2:
                    print("종료합니다. 전 단계로 이동합니다.")
                    break
                else:
                    print("잘못 입력하셨습니다. 다시 입력해주세요.")
                    continue
            except (ValueError, TypeError):
                print("다시 입력해주세요!!")
                continue
        
    # 전체 보기 로직
    def __show_logic(self, order) -> None:
        return f"{self.student_numbering[order][order][0]}\t\t{self.student_numbering[order][order][1]}\t{self.student_numbering[order][order][2]}\t{self.student_numbering[order][order][3]}\t{self.student_numbering[order][order][4]}\t{self.student_numbering[order][order][5]}\t{self.student_numbering[order][order][6]}\t{self.student_numbering[order][order][7]}"
    
    # 2. 전체 보기
    def show_data(self) -> None:    
        print("수험번호\t이름\t국어\t영어\t수학\t과학\t총합\t평균")
        for index, _ in enumerate(self.student_numbering):
            print(self.__show_logic(index))

    # 검색 로직
    def __search_logic(self, search) -> Union[Any, Literal[-1], None]:
        try:
            if self.student_numbering[search][search][0] == search:
                return self.__show_logic(search)
        except IndexError:
            return "없는 데이터 입니다. 다시 확인해주세요."

    # 3. 검색
    def one_search_data(self):
        while True:
            try:
                search: int = int(input("수험번호를 입력해주세요.\n종료를 원하시면 -2번을 눌러주세요.\n: "))
                if search == -2:
                    print("종료합니다. 전 단계로 이동합니다.")
                    # self.option_select()
                    break
                else:
                    injection = self.__search_logic(search=search)
                    print("수험번호\t이름\t국어\t영어\t수학\t과학\t총합\t평균")
                    print(injection)
            except (ValueError, KeyError, TypeError) as error:
                print(f"{error} -> 올바른 입력이 아닙니다 다시 입력해주세요")



    # 부분 삭제 로직
    def __delete_logic(self, order) -> None:
        self.student_numbering[order][order][0] = order
        self.student_numbering[order][order][1] = None
        self.student_numbering[order][order][2] = None
        self.student_numbering[order][order][3] = None
        self.student_numbering[order][order][4] = None
        self.student_numbering[order][order][5] = None
        self.student_numbering[order][order][6] = None
        self.student_numbering[order][order][7] = None
        
    # 4. 삭제
    def delete_data(self) -> None:
        while True:
            try:
                dt: int = int(input("원하시는 메뉴의 번호를 입력해주세요.\n종료를 원하시면 -2번을 눌러주세요.\n1. 전체 삭제\t2. 부분 삭제\n: "))
                if dt == 1:
                    self.student_numbering.clear()
                    print("전체 삭제 했습니다.")
                elif dt == 2:
                    dt_search: int = int(input("삭제를 원하시는 학생의 수험번호를 입력해주세요.\n: "))
                    self.__delete_logic(dt_search)
                    print("해당 성적을 삭제 했습니다.")
                elif dt == -2:
                    print("종료합니다. 전 단계로 이동합니다.")
                    break
            except IndexError:
                print("다시 입력해주세요.")
            
    def save_data(self):
        dd = [pd.DataFrame(data, index=["번호", "이름", "국어", "수학", 
                                        "영어", "과학", "총합", "평균"]).T for _, data in enumerate(self.student_numbering)]
        data = pd.concat(dd)
        print("데이터를 저장합니다..!")
        return data.to_csv("sungjuk.csv", index=False, index_label=False)

    # 옵션 선택
    def option_select(self) -> None:
        while True:
            # 번호 입력 시 해당 메서드 실행
            print("[ 성적표 프로그램 ]")
            print("1. 성적 입력\t2. 전체 보기\t3. 검색\n4. 삭제\t\t5. 파일 저장\t6. 종료하기")
            sel = int(input("원하시는 메뉴의 번호를 입력해주세요.\n: "))
            # 1. 성적 입력
            if sel == 1:
                print("[ 1. 성적 입력 ]")
                self.input_data()
            # 2. 전체 보기
            elif sel== 2:
                print("[ 2. 전체 보기 ]")
                self.show_data()
            # 3. 검색
            elif sel == 3:
                print("[ 3. 검색 ]")
                self.one_search_data()
            # 4. 삭제
            elif sel == 4:
                print("[ 4. 삭제 ]")
                self.delete_data()
            # 5. CSV 파일 저장
            elif sel == 5:
                print("[ 5. 파일 저장 ]")
                self.save_data()
            # 6. 종료하기
            elif sel == 6:
                print("[ 6. 종료하기 ]")
                print("성적표 프로그램을 종료합니다.")
                break
            else:
                print("잘못 입력하셨습니다. 다시 입력해주세요.")
                continue
        
    


first_class = GradeWriterProgram().option_select()


# class SaveGradeDataInitailization(GradeWriterProgram):
#     pass