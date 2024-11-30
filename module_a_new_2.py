import pandas as pd
import json

class Categorylist:
    def __init__(self):
        self.result = 0
    def Catlist(self):
        return typelist
# 클래스로 만들어서 모듈 가져올때 사용할 수 있게 함

# CSV 파일 읽기
file_path = "20231231.csv"
data = pd.read_csv(file_path, encoding="cp949")  # 파일 인코딩에 맞게 설정

# 유형별 데이터 정리
result = {}  # 통합 결과 저장
i=1
typelist=[0]
# 과목 이름이 들어갈 리스트 미리 생성
for category, group in data.groupby("유형"):  # '유형' 열을 기준으로 그룹화
    # 특정 유형별로 표준점수를 키로, 남자/여자인원을 값으로 저장
    type_data = {"남자": {}, "여자": {}}
    for _, row in group.iterrows():
        score = row["표준점수"]
        type_data["남자"][score] = row["남자"]
        type_data["여자"][score] = row["여자"]
    result[category] = type_data
    typelist.append(f"{i}.{category}")
    i=i+1
    # 리스트에 과목명 차례대로 저장
    # f string 이용하여 1.과목명 형태로 저장


# 결과 저장 (JSON 파일)
output_json = "structured_type_data_new.json"
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
