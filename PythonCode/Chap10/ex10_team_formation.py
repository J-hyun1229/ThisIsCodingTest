def find_team(team, s):
    if team[s] != s:
        team[s] = find_team(team, team[s])
    return team[s]


def union_team(team, s1, s2):
    s1 = find_team(team, s1)
    s2 = find_team(team, s2)
    if s1 < s2:
        team[s2] = s1
    else:
        team[s1] = s2


# 학생 수, 연산 개수
n, m = map(int, input().split())
team = [0] * (n+1)

for i in range(1, n+1):
    team[i] = i

for _ in range(m):
    kind, a, b = map(int, input().split())
    if kind == 0:  # 팁 합치기 연산
        union_team(team, a, b)
    elif kind == 1: # 같은 팀 여부 확인 연산
        if team[a] == team[b]:
            print("YES")
        else:
            print("NO")
