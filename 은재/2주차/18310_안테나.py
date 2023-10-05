house_num = int(input())
print("집의 수", house_num)
house_loc = input()
print("집의 위치", house_loc)

house_loc = list(map(int, house_loc.split(' '))) #문자열 분리 및 정수 변환 후 리스트 생성
house_loc.sort() #오름차순 정렬
print(house_loc)

#중간값이 최소가 되는 위치
print(house_loc[(house_num-1)//2]) 