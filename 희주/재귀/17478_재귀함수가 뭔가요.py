import sys

N = int(sys.stdin.readline().rstrip()) # 재귀 횟수 N

start_line = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
question = "\"재귀함수가 뭔가요?\""
story_1 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
story_2 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
story_3 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""

answer = "\"재귀함수는 자기 자신을 호출하는 함수라네\""
last_sentence = "라고 답변하였지."
tap ="____"

def recursive_function(n):
    print(tap*n+question) # 질문
    
    if n == N: # N 번째에
        print(tap*n+answer) # 답변
        print(tap*n+last_sentence) # 마무리 문장 출력 
        return 1
    
    print(tap*n+story_1) # 이야기 출력
    print(tap*n+story_2)
    print(tap*n+story_3)
    
    recursive_function(n+1) # n+1 재귀 호출
    
    print(tap*n+last_sentence) # 마무리 문장 출력 
    
print(start_line) # 첫 문장 
recursive_function(0) # 재귀 함수 호출

## 실행시간: 44ms