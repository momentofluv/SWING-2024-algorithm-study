n, m = map(int, input().split())
answer = []

def backtracking(x):
    if len(answer) == m:     # 만일 M의 길이만큼 수를 선택했다면
        print(" ".join(map(str, answer)))    # 각 수를 공백으로 구분해 출력한다
        return

    for i in range(x, n+1):  # 인덱싱이 아니라 숫자를 사용하므로 x부터 n까지의 값 필요 (새로 등록되는 값은 x보다 작아선 안 됨)
        answer.append(i)
        backtracking(i)  # 재귀로 동일 동작 반복 (m개만큼 중복 없이 숫자 나열할 때까지)
        answer.pop()    # answer에 m개의 수가 저장되면 pop이 실행되어 가장 마지막 숫자 삭제
                            # 예를 들어, 1 2 3 4가 저장되었다면 4를 삭제 후 이후 동작 실행
            
backtracking(1)