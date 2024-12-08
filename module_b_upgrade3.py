import json
import matplotlib.pyplot as plt
from module_a import Categorylist


class Graph:
    def __init__(self):
        self.year = self.select_year()  # 연도 선택
        self.data = self.load_json_data()  # JSON 데이터 로드

    def select_year(self):
        """사용자로부터 연도를 선택받습니다."""
        print("사용 가능한 연도:")
        available_years = ['2020','2021','2022','2023']
        for year in available_years:
            print(year)

        try:
            year = str(input("연도를 선택하세요: "))
            # 반복문으로 year 과 available_years 의 값 비교
            for i in range(0,len(available_years)):
                if available_years[i]==year:
                    return year
                    break
                elif i==(len(available_years)-1):
                    raise ValueError
                    break
        except ValueError:
            print("잘못된 연도입니다. 프로그램을 종료합니다.")
            exit()

    def load_json_data(self):
        json_file = f"structured_type_data_new_{self.year}.json"
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print(f"{self.year}년 데이터를 찾을 수 없습니다.")
            exit()

    def input(self):
        c = Categorylist()
        sublist = c.Catlist(self.year)  # 선택된 연도의 과목 리스트 가져오기
        print("과목 리스트:")
        for item in sublist:  # 과목 리스트 출력
            print(item)

        try:
            i = int(input("원하는 과목 번호를 입력하세요: "))
            if 1 <= i <= len(sublist):  # 입력값 검증
                subject = sublist[i - 1].split(".", 1)[1]  # "번호.과목명"에서 과목명만 추출
                return subject
            else:
                print("잘못된 입력입니다. 프로그램을 종료합니다.")
                exit()
        except ValueError:
            print("유효한 번호를 입력하세요. 프로그램을 종료합니다.")
            exit()

    def LineGraph(self, subject):
        """선택한 과목에 대한 그래프를 출력합니다."""
        # JSON 데이터에서 과목별 데이터 추출
        male_score = self.data[subject]['남자']
        female_score = self.data[subject]['여자']

        # x축(표준점수)와 y축(남자/여자 인원수) 데이터 생성
        x = sorted(map(int, male_score.keys()))
        y_male = [male_score[str(score)] for score in x]
        y_female = [female_score[str(score)] for score in x]

        # 그래프 설정 (한글 폰트 지원)
        plt.rcParams['font.family'] = 'Malgun Gothic'

        # 그래프 그리기
        plt.bar(x, y_male, label="남자", color='blue', alpha=0.6, width=0.4, align='center')
        plt.bar(x, y_female, label="여자", color='red', alpha=0.6, width=0.4, align='center')

        # 그래프 설정 (한글 사용)
        plt.xlabel("표준 점수")
        plt.ylabel("인원수")
        plt.title(f"{subject} 과목의 남녀 표준 점수 인원수")
        plt.legend()
        plt.show()

        return 0
