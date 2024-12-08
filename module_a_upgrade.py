import pandas as pd
import json

# 연도별 파일 경로를 딕셔너리로 정의
file_paths = {
    2020: '20201231.csv',
    2021: '20211231.csv',
    2022: '20221231.csv',
    2023: '20231231.csv'
}

# 연도별 데이터 처리
for year, file_path in file_paths.items():
    # CSV 파일 읽기
    try:
        data = pd.read_csv(file_path, encoding="cp949")  # 인코딩: cp949
    except Exception as e:
        print(f"Error reading file for {year}: {e}")
        continue

    result = {}  # JSON 결과 저장용 딕셔너리
    typelist = []  # 과목 리스트
    i = 1  # 과목 번호 카운터

    # '유형' 열 기준으로 그룹화하여 처리
    for category, group in data.groupby("유형"):
        type_data = {"남자": {}, "여자": {}}  # 남자/여자 데이터를 저장할 딕셔너리

        # 각 그룹의 데이터를 순회하며 처리
        for _, row in group.iterrows():
            score = row["표준점수"]
            type_data["남자"][score] = row["남자"]
            type_data["여자"][score] = row["여자"]

        # 그룹 데이터를 결과에 추가
        result[category] = type_data
        typelist.append(f"{i}.{category}")  # 예: "1.과목명"
        i += 1

    # JSON 파일로 저장
    output_json = f"structured_type_data_new_{year}.json"
    try:
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
        print(f"Processed and saved: {output_json}")
    except Exception as e:
        print(f"Error saving JSON file for {year}: {e}")