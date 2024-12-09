import pandas as pd
import json

class Categorylist:
    def __init__(self):
        # 연도별 파일 경로를 정의
        self.file_paths = {
            2020: '20201231.csv',
            2021: '20211231.csv',
            2022: '20221231.csv',
            2023: '20231231.csv'
        }

    def create_json_files(self):
        # 모든 연도의 데이터 처리 및 JSON 저장
        for year, file_path in self.file_paths.items():
            try:
                data = pd.read_csv(file_path, encoding="cp949")  # cp949 인코딩 사용
            except Exception as e:
                print(f"Error reading file for {year}: {e}")
                continue

            result = {}
            typelist = []
            i = 1

            for category, group in data.groupby("유형"):
                type_data = {"남자": {}, "여자": {}}

                for _, row in group.iterrows():
                    score = row["표준점수"]
                    type_data["남자"][score] = row["남자"]
                    type_data["여자"][score] = row["여자"]

                result[category] = type_data
                typelist.append(f"{i}.{category}")
                i += 1

            output_json = f"structured_type_data_new_{year}.json"
            try:
                with open(output_json, "w", encoding="utf-8") as f:
                    json.dump(result, f, ensure_ascii=False, indent=4)
                print(f"Processed and saved: {output_json}")
            except Exception as e:
                print(f"Error saving JSON file for {year}: {e}")

    def Catlist(self, year):
        # 선택된 연도의 JSON 파일 읽기
        json_file = f"structured_type_data_new_{year}.json"
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            typelist = [f"{i + 1}.{key}" for i, key in enumerate(data.keys())]
            return typelist
        except FileNotFoundError:
            print(f"{year}년 데이터를 찾을 수 없습니다. JSON 파일을 생성했는지 확인하세요.")
            return []
