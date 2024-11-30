import pandas as pd
import json

class Categorylist:
    def __init__(self):
        self.result = 0

    def Catlist(self):
        return typelist  # 생성된 과목 리스트 반환

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
