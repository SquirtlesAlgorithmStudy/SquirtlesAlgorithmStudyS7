import sys
input = sys.stdin.readline
N, h_atk = map(int, input().split())
rooms = [tuple(map(int, input().split())) for _ in range(N)]


def simulation(h_max, h_atk):
    cur_h_atk = h_atk
    cur_hp = h_max
    for room in rooms:
        if room[0] == 1:
            attack_count = (room[2] // cur_h_atk) + min(1, room[2] % cur_h_atk)
            cur_hp -= (room[1] * (attack_count - 1))
            if cur_hp <= 0:
                return False
        elif room[0] == 2:
            cur_h_atk += room[1]
            cur_hp += room[2]
            cur_hp = min(cur_hp, h_max)
    return True


start = 1
end = 1_000_000 * 1_000_000 * 123_456

while (start <= end):
    mid = (start + end) // 2
    if simulation(mid, h_atk):
        end = mid - 1
    else:
        start = mid + 1
print(start)


