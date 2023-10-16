import sys
iteration = int(sys.stdin.readline())
middle_count = 0

first_sentence = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."

def middle_sentence(n, text =''):

    global middle_count

    if n == 0:
        return text

    text = '____' * middle_count + "\"재귀함수가 뭔가요?\"\n"
    text += '____' * middle_count + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n"
    text += '____' * middle_count + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n"
    text += '____' * middle_count + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n"

    middle_count += 1
    return text + middle_sentence(n-1)



def last_sentence(n,text = ''):

    text += ('____'*(n)+"라고 답변하였지.\n")

    if n == 0:

        return text
    
    n -= 1

    return text+last_sentence(n)

def chatbot(n):
    print(first_sentence)
    print(middle_sentence(n).strip())
    print('____'*n+"\"재귀함수가 뭔가요?\"")
    print('____'*n+"\"재귀함수는 자기 자신을 호출하는 함수라네\"")
    print(last_sentence(n).strip())

chatbot(iteration)
