INF = int(1e9)
# 압축할 문자열
s1 = input()


def solution(s):

    res = INF

    for i in range(1, len(s)+1):  # i: 1 ~ len(s)
        print("if length", i)
        index = 0
        res_str = ""  # 압축 결과를 여기에 저장하고, 전 압축 결과와 길이를 비교한다.
        while index < len(s):  # 문자열 길이 내에서
            count = 1
            tmp_str = s[index:index+i]  # 문자열을 i개 단위로 자른 요소
            index += i  # 다음 단위와 비교한다. s = "hello", i = 1일 때 'h'와 'e' 비교.
            # print("in while index<len(s), tmp_str = %s, count = %d" % (tmp_str, count))
            while tmp_str == s[index:index+i]:  # 다음 문자단위와 비교
                count += 1
                index += i
                # print("in while tmp_str==s[:], count = %d, index = %d" % (count, index))
            if count == 1:  # 압축결과에서 1은 생략
                res_str += tmp_str
            else:
                res_str += (str(count) + tmp_str)
            print("res_str added:", res_str)

        res = min(res, len(res_str))

    return res


n = solution(s1)
print(n)
