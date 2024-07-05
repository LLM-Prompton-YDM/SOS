import requests
import json
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

url = 'https://data.myhome.go.kr/rentalHouseList?serviceKey=SIMuYtPaPVHuKqIUXGQXnLCDnSXMWsyauPFvNDsI10qfpdQ7po0WKOaDryWxfEaseFwFbdJgmTIqydTZr31Wlw%3D%3D&brtcCode=11&si'
params ={'signguCode' : '140', 'numOfRows' : '10', 'pageNo' : '1' }

# 데이터프레임 초기화
all_page_df = pd.DataFrame()

# 반복문을 통해 여러 페이지의 데이터 가져오기
for page in range(1, 201):  # 200 페이지
    params['pageNo'] = str(page)
    response = requests.get(url, params=params, verify=False)
    contents = response.text
    json_ob = json.loads(contents)
    
    if 'hsmpList' in json_ob:
        data = json_ob['hsmpList']

        # 원하는 변수만 추출
        columns = ['brtcNm', 
                    'signguNm', 
                    'hsmpNm', 
                    'competDe',
                    'hshldCo',
                    'suplyTyNm',
                    'suplyPrvuseAr',
                    'houseTyNm',
                    'buldStleNm',
                    'bassRentGtn',
                    'bassMtRntchrg']

        extracted_data = []
        
        for item in data:
            extracted_item = {key: item.get(key, '') for key in columns}
            extracted_data.append(extracted_item)

        # 각 페이지의 데이터프레임 생성 및 결합
        page_df = pd.DataFrame(extracted_data)
        all_page_df = pd.concat([all_page_df, page_df], ignore_index=True)
    else:
        break  # 데이터가 없으면 반복문 종료

# 컬럼 이름 변경
all_page_df.columns = ['광역시도', 
                    '시군구', 
                    '단지', 
                    '준공 일자', 
                    '세대 수', 
                    '공급 유형', 
                    '공급 전용 면적', 
                    '주택 유형',
                    '건물 형태',
                    '기본 임대보증금',
                    '기본 월임대료']

# csv 파일 저장
all_page_df.to_csv('rentalhouse.csv', index=False)