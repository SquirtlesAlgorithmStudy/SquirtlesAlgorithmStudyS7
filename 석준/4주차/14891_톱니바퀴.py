import copy
import sys

matrix = [list(map(int, sys.stdin.readline().strip())) for _ in range(4)]

rotations = int(sys.stdin.readline())

simuation_info = []

for i in range(rotations):
    simuation_info.append(list(map(int, sys.stdin.readline().split())))


def rotation_sequence(wheel_1_1,wheel_2_1,wheel_2_2,wheel_3_1,wheel_3_2,wheel_4_1,matrix,wheel_number,direction):
    new_matrix = copy.deepcopy(matrix)
    
    if wheel_number == 1:

        if wheel_1_1 != wheel_2_1:
            new_matrix[1] = matrix[1][direction:] + matrix[1][:direction]
        else:
            return new_matrix  
        if wheel_2_2 != wheel_3_1:
            new_matrix[2] = matrix[2][-direction:] + matrix[2][:-direction]
        else:
            return new_matrix 
        if wheel_3_2 != wheel_4_1:
            new_matrix[3] = matrix[3][direction:] + matrix[3][:direction]
            return new_matrix
        else:
            return new_matrix 

        
    elif wheel_number == 2:

        if wheel_1_1 != wheel_2_1:
            new_matrix[0] = matrix[0][direction:] + matrix[0][:direction]
        if wheel_2_2 != wheel_3_1:
            new_matrix[2] = matrix[2][direction:] + matrix[2][:direction]
        else:
            return new_matrix
        if wheel_3_2 != wheel_4_1:
            new_matrix[3] = matrix[3][-direction:] + matrix[3][:-direction]
        else:
            return new_matrix
    elif wheel_number == 3:
        
        if wheel_3_2 != wheel_4_1:
            new_matrix[3] = matrix[3][direction:] + matrix[3][:direction]
        if wheel_3_1 != wheel_2_2:
            new_matrix[1] = matrix[1][direction:] + matrix[1][:direction]
        else:
            return new_matrix
        if wheel_2_1 != wheel_1_1:
            new_matrix[0] = matrix[0][-direction:] + matrix[0][:-direction]
        else:
            return new_matrix       
    else:
        if wheel_3_2 != wheel_4_1:
            new_matrix[2] = matrix[2][direction:] + matrix[2][:direction]
        else:
            return new_matrix
        if wheel_2_2 != wheel_3_1:
            new_matrix[1] = matrix[1][-direction:] + matrix[1][:-direction]
        else:
            return new_matrix
        if wheel_1_1 != wheel_2_1:
            new_matrix[0] = matrix[0][direction:] + matrix[0][:direction]
            return new_matrix
        else:
            return new_matrix
    return new_matrix
        

for i in range(len(simuation_info)):
    
    wheel_number = simuation_info[i][0]
    direction = simuation_info[i][1]
    wheel_1_1 = matrix[0][2]
    wheel_2_1 = matrix[1][6]
    wheel_2_2 = matrix[1][2]
    wheel_3_1 = matrix[2][6]
    wheel_3_2 = matrix[2][2]
    wheel_4_1= matrix[3][6]
    
    matrix[wheel_number-1] = matrix[wheel_number-1][-direction:] + matrix[wheel_number-1][:-direction]
    matrix = rotation_sequence(wheel_1_1,wheel_2_1,wheel_2_2,wheel_3_1,wheel_3_2,wheel_4_1,matrix,wheel_number,direction)
    
result = matrix[0][0]*1+matrix[1][0]*2+matrix[2][0]*4+matrix[3][0]*8

print(result)
