def solution(N): #예를 들어 1041

    N = bin(N) #bin은 이진수로 변환해주는 내장함수 #0b10000010001
    N = N[2:] # 앞의 0x 제거 #10000010001
    N = N.strip('0') #바깥의 0 제거 #10000010001
    N = N.strip('1') #바깥쪽 1 제거 #000001000
    N = N.split('1') #1을 기준으로 나누기 #['00000','000']
    max_gap = max(N) #
    return len(max_gap)


print(solution(1041))