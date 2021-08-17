import copy

security_info = [
    {'일자': '19.04.15', '종가': 785000, '거래량': 79620 },
    {'일자': '19.04.16', '종가': 785000, '거래량': 68203 },
    {'일자': '19.04.17', '종가': 754000, '거래량': 165929 },
    {'일자': '19.04.18', '종가': 779000, '거래량': 94462 },
    {'일자': '19.04.19', '종가': 770000, '거래량': 76814 },
    {'일자': '19.04.22', '종가': 774000, '거래량': 58079 },
    {'일자': '19.04.23', '종가': 775000, '거래량': 79128 },
    {'일자': '19.04.24', '종가': 771000, '거래량': 61650 },
    {'일자': '19.04.25', '종가': 757000, '거래량': 111805 },
    {'일자': '19.04.26', '종가': 764000, '거래량': 68237 },
]


def sort_security(input_data, sort_option, return_size=5):
    if sort_option not in ['수익률', '거래량']:
        print("두 번째 전달인자를 잘못 입력하였습니다.")
        return -2

    if return_size < 1 or return_size > len(input_data):
        print("세 번째 전달인자를 잘못 입력하였습니다.")
        return -3

    data = copy.deepcopy(input_data)

    if sort_option == '거래량':
        return list(sorted(data, key=lambda datum: datum['거래량'], reverse=True))[:return_size]

    if sort_option == '수익률':
        for i in range(1, len(data)):
            data[i]['수익률'] = round(float(data[i]['종가']-data[i-1]['종가'])/data[i-1]['종가'], 4)
        return list(sorted(data[1:], key=lambda datum: datum['수익률'], reverse=True))[:return_size]


# 테스트 0 : 모든 올바른 경우의 수에 대해 결과값을 출력한다.
for opt in ['거래량', '수익률']:
    for num in range(1, 10):
        print(sort_security(security_info, opt, num))

# 테스트 1: 모두 정상적인 전달인자를 입력하여 수익률 기준으로 내림차순 정렬한다.
print("전달인자 => security_info, '수익률', 4 : 수익률 기준으로 내림차순 정렬")
print(sort_security(security_info, '수익률', 4))

# 테스트 2: 세 번째 전달인자는 자동으로 5가 지정되며 거래량 기준으로 내림차순 정렬한다.
print("전달인자 => security_info, '거래량' : 거래량 기준으로 내림차순 정렬")
print(sort_security(security_info, '거래량'))

# 테스트 3: 두 번째 전달인자에 오류가 있는 경우다.
print("전달인자 => security_info, '시가', 2 : 두 번째 전달인자를 잘못 지정")
print(sort_security(security_info, '시가', 2))

# 테스트 4: 세 번째 전달인자에 오류가 있는 경우다.
print("전달인자 => security_info, '수익률', 11 : 세 번째 전달인자를 잘못 지정")
print(sort_security(security_info, '수익률', 11))
