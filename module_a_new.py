import pandas as pd
import json
# CSV 파일 읽기
file_path = "20231231.csv"
data = pd.read_csv(file_path, encoding="cp949")  # 파일 인코딩에 맞게 설정
# 유형별 데이터 정리
result = {}
for category, group in data.groupby("유형"):  # '유형' 열을 기준으로 그룹화
    # 특정 유형별로 표준점수를 키로, 남자/여자인원을 값으로 저장
    type_data_male = {}
    type_data_female={}
    for _, row in group.iterrows():
        score = row["표준점수"]
        male = row["남자"]
        female = row["여자"]
        type_data_male[score] = [male]
        type_data_female[score] = [female]
    result[category] = type_data_male, type_data_female 
    # 기존 코드에서 남자와 여자의 인원수를 분리해서 나타나게 설정했습니다.

# 결과 저장 (JSON 파일)
output_json = "structured_type_data_new.json"
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=4)


# 그래프 그릴 때 남자 여자 인원이 같이 있어서, 그래프가 이상하게 그려지더라고요. 그래서 이중 디렉토리 형태에서 한번 더 분리하였습니다.
