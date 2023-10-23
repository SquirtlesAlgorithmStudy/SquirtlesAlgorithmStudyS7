import sys
sys.setrecursionlimit(10**6)

number_of_problem = int(input())
problem_matrix = []
for i in range(number_of_problem):
    row,col,cabbage = map(int,input().split())
    farm_area = [[0 for _ in range(row)] for _ in range(col)]
    for j in range(cabbage):
        x,y = map(int,input().split())
        farm_area[y][x] = 1
    problem_matrix.append(farm_area)
    
def dfs(x,y,problem):
    
    if x<= -1 or x>= len(problem_matrix[problem]) or y<= -1 or y >=len(problem_matrix[problem][0]):
        return False
    if problem_matrix[problem][x][y] == 1:

        problem_matrix[problem][x][y] = 0

        dfs(x-1,y,problem)
        dfs(x,y-1,problem)
        dfs(x+1,y,problem)
        dfs(x,y+1,problem)

        return True
    
    return False

for problem in range(number_of_problem):
    result = 0
    n,m = len(problem_matrix[problem]),len(problem_matrix[problem][0])
    for i in range(n):
        for j in range(m):

            if dfs(i,j,problem) == True:
                result += 1

    print(result)
