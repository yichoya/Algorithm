# def solution(numbers):
#     answer = []
#     for i in range(0, len(numbers) - 1):
#         tmp = -1
#         for j in range(i + 1, len(numbers)):
#             if numbers[i] < numbers[j]:
#                 tmp = numbers[j]
#                 break
#         answer.append(tmp)
#     answer.append(-1)
#     return answer

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for idx, num in enumerate(numbers):
        # 스택: 자신보다 큰 수를 찾지 못한 인덱스 저장
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(idx)
        
    return answer