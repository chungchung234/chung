"""
===============================
문제출처  : chung
문제번호  : note
문제단계  : 연습장
최초생성  : 2022.01.23
생성자    : chung
문제설명  : asdasd
===============================
"""
def solution(answers):
    answer = []
    ans_1=[1, 2, 3, 4, 5]*2001
    ans_2=[2, 1, 2, 3, 2, 4, 2, 5]*126
    ans_3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1001
    cnt=[0,0,0]
    for i, ans in enumerate(answers):
        if ans_1[i]==ans:
            cnt[0]+=1
        if ans_2[i]==ans:
            cnt[1]+=1
        if ans_3[i]==ans:
            cnt[2]+=1
    for i,j in enumerate(cnt):
        if j == max(cnt):
            answer.append(i+1)
    return answer

print(solution([1,2,3,4,5]*2000))