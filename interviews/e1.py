# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")

# def solution(A):
#     # write your code in Python 3.6

#     # collecting all positive, then find min
#     # minim = min([A[i] for i in range(len(A)) if A[i] > 0])

#     minim = 1
#     for i in range(len(A)):
#         if A[i] > 0 and A[i] < minim:
#             minim = A[i]

#     print(">> minim", minim)

#     for j in range(len(A)):
#         if A[j] > 0 and A[j] >= minim: 
#             print("herere A[i]", A[j])

#             if A[j] + 1 in A:
#                 continue
#             else:
#                 return A[j] + 1
#         else:
#             return minim

# A = [1, 2, 3]
# # A = [-1, -3]

# print(solution(A))



# """   
# m = max(A)
# if m < 1:
#     return 1

# A = set(A)
# B = set(range(1, m + 1))
# D = B - A
# if len(D) == 0:
#     return m + 1
# else:
#     return min(D)
# """


def solution(S, A):
    # write your code in Python 3.6
    print(S, A)

    sender = 0
    message = S[0]
    receiver = A[0]

    for _ in range(len(A)):
        print(sender, message, receiver)
        if receiver == 0:
            return message
        else:
            # sender = receiver
            message = message + S[receiver]
            receiver = A[receiver]


# S = "bytdag"
# A = [4, 3, 0, 1, 2, 5]

S = "cdeo"
A = [3, 2, 0, 1]
print(solution(S, A))
