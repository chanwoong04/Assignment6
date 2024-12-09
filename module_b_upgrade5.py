import json
import matplotlib.pyplot as plt
from module_a_upgrade3 import Categorylist

class Graph:
    def __init__(self):
        self.year = self.select_year()  # 연도 선택
        self.data = self.load_json_data()  # JSON 데이터 로드

    def select_year(self):
        """사용자로부터 연도를 선택받습니다."""
        print("사용 가능한 연도:")
        available_years = ['2020', '2021', '2022', '2023']
        for year in available_years:
            print(year)

        while True:
            year = input("연도를 선택하세요: ").strip()
            if year in available_years:
                return year
            else:
                print("잘못된 연도입니다. 다시 시도하세요.")

    def load_json_data(self):
        """선택된 연도의 JSON 데이터를 로드합니다."""
        json_file = f"structured_type_data_new_{self.year}.json"
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print(f"{self.year}년 데이터를 찾을 수 없습니다. JSON 파일을 생성했는지 확인하세요.")
            exit()

    def input(self):
        """사용자로부터 과목 선택을 받습니다."""
        c = Categorylist()
        sublist = c.Catlist(int(self.year))  # 선택된 연도의 과목 리스트 가져오기
        if not sublist:
            print("과목 리스트를 불러올 수 없습니다. 프로그램을 종료합니다.")
            exit()

        print("\n과목 리스트:")
        for item in sublist:  # 과목 리스트 출력
            print(item)

        while True:
            try:
                i = int(input("원하는 과목 번호를 입력하세요: "))
                if 1 <= i <= len(sublist):  # 입력값 검증
                    subject = sublist[i - 1].split(".", 1)[1]  # "번호.과목명"에서 과목명만 추출
                    return subject
                else:
                    print("잘못된 입력입니다. 번호를 다시 입력하세요.")
            except ValueError:
                print("유효한 번호를 입력하세요.")

    def LineGraph(self, subject):
        """선택한 과목에 대한 그래프를 출력합니다."""
        male_score = self.data[subject]['남자']
        female_score = self.data[subject]['여자']

        x = sorted(map(int, male_score.keys()))
        y_male = [male_score[str(score)] for score in x]
        y_female = [female_score[str(score)] for score in x]

        plt.rcParams['font.family'] = 'Malgun Gothic'
        plt.bar(x, y_male, label="남자", alpha=0.6, width=0.4, align='center')
        plt.bar(x, y_female, label="여자", alpha=0.6, width=0.4, align='center')

        plt.xlabel("표준 점수")
        plt.ylabel("인원수")
        plt.title(f"{self.year}년 {subject} 과목의 남녀 표준 점수 인원수")
        plt.legend()
        plt.show()
