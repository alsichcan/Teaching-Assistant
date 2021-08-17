gpa_list = []
gpa_dict = {'A': 4, 'B': 3, 'C': 2, 'D': 1}

# Input : (credit, gpa) >> gpa_list
cnt = 1
while True:
    try:
        credit = int(input("%d회: 해당 교과목의 학점 수를 1 이상 4 이하의 자연수로 입력하세요(-1 입력시 종료): " %cnt))
    except ValueError:
        print("정수를 입력해야 합니다.")
    else:
        if credit == -1: break
        elif credit not in [-1, 1, 2, 3, 4]: print("학점 수를 잘못 입력하였습니다.")
        else:
            while True:
                try:
                    gpa = gpa_dict[input("%d회: 평점을 대문자 알파벳으로 입력하세요: " %cnt)]
                    gpa_list.append((credit, gpa))
                    break
                except KeyError:
                    print("평점을 잘못 입력하였습니다.")
            cnt += 1

# Output : average_gpa >> print()
weighted_sum = 0
credit_sum = 0

for credit, gpa in gpa_list:
    credit_sum += credit
    weighted_sum += gpa * credit

try:
    print("평균 평점: %.2f" %round(float(weighted_sum)/credit_sum, 2))
except ZeroDivisionError:
    print("입력이 없어 결과를 출력하지 않고 종료합니다.")
