import json
import matplotlib.pyplot as plt
import numpy as np
from module_a import Categorylist

class Graph:
    def __init__(self):
        self.result = 0


    def input(self):
        c=Categorylist()
        i=input(f"{c.Catlist()}")
        sublist=c.Callist()
        subject=sublist[int(i)]
        return subject
    

    def LineGraph(self,subject):
        male_score = data[subject]['남자']
        female_score = data[subject]['여자']


        x = sorted(map(int, male_score.keys()))
        y_male = [male_score[str(score)] for score in x]
        y_female = [female_score[str(score)] for score in x]
        # x값(표준점수)에 대하여, 각 성별의 스코어(표점)에 대해 각각 매칭되도록 했습니다.

        plt.plot(x, y_male, label="male", color='blue', linestyle='-')
        plt.plot(x, y_female, label="female", color='red',linestyle='--')

        plt.xlabel("score")
        plt.ylabel("headcount")
        plt.title("headcount per score of male/female")
        # plt가 한글 지원을 안해서, 영어로 작성했습니다.
        plt.legend()
        plt.show()
        return 0


with open("structured_type_data_new.json","r",encoding='UTF-8') as f:
    data= json.load(f)
# 파일 읽어서 data에 저장하기, json 파일은 현재 과목명, 성별, 표준점수가 키값으로 있는 삼중 딕셔너리 형태임.
