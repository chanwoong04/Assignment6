from module_b_new_3 import Graph

if __name__ == "__main__":
    print("------ 그래프 출력 프로그램 ------")
    try:
        graph = Graph()
        subject = graph.input()
        graph.LineGraph(subject)
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
