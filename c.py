import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

class Categorylist:
    def __init__(self):
        self.result = 0
    def Catlist(self):
        return typelist
# 클래스로 만들어서 모듈 가져올때 사용할 수 있게 함

# CSV 파일 읽기
file_path = "20231231.csv"
data = pd.read_csv(file_path, encoding="cp949")  # 파일 인코딩 설정

# 유형별 데이터 정리
result = {}  # 통합 결과 저장
i = 1
typelist = []  # 과목 이름이 들어갈 리스트 생성

for category, group in data.groupby("유형"):  # '유형' 열 기준 그룹화
    type_data = {"남자": {}, "여자": {}}  # 남자/여자 인원 저장용
    for _, row in group.iterrows():
        score = row["표준점수"]
        type_data["남자"][score] = row["남자"]
        type_data["여자"][score] = row["여자"]
    result[category] = type_data
    typelist.append(f"{i}.{category}")  # "번호.과목명" 형태로 저장
    i += 1

# 결과 저장 (JSON 파일)
output_json = "structured_type_data_new.json"
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

class Graph:
    def __init__(self):
        pass

    def input(self):
        c = Categorylist()
        sublist = c.Catlist()  # 과목 리스트 가져오기
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
        # JSON 데이터에서 과목별 데이터 추출
        male_score = data[subject]['남자']
        female_score = data[subject]['여자']

        # x축(표준점수)와 y축(남자/여자 인원수) 데이터 생성
        x = sorted(map(int, male_score.keys()))
        y_male = [male_score[str(score)] for score in x]
        y_female = [female_score[str(score)] for score in x]

        # 그래프 설정 (한글 폰트 지원)
        plt.rcParams['font.family'] = 'Malgun Gothic'

        # 그래프 그리기
        plt.plot(x, y_male, label="남자", color='blue', linestyle='-')
        plt.plot(x, y_female, label="여자", color='red', linestyle='--')

        # 그래프 설정 (한글 사용)
        plt.xlabel("표준 점수")
        plt.ylabel("인원수")
        plt.title(f"{subject} 과목의 남녀 표준 점수 인원수")
        plt.legend()
        plt.show()

        return 0


# JSON 파일 읽기
with open("structured_type_data_new.json", "r", encoding="UTF-8") as f:
    data = json.load(f)

# Graph 클래스 실행
if __name__ == "__main__":
    graph = Graph()
    selected_subject = graph.input()
    graph.LineGraph(selected_subject)
