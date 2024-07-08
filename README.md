# [원티드X네이버클라우드] 생성형 AI 시대 직장인을 위한 프롬프톤
![image](https://github.com/LLM-Prompton-YDM/SOS/assets/87981867/259f513a-6a84-42d8-a219-1cabc472847a)

- 팀명 : YDM(Yura Data analyst Member) - 신재영, 정지혜
- 주제 : SOS(Subscription recOmmendation System) 구해줘 청약홈즈
- 배경 : 참가자가 직장인임을 생각하여 모두의 목표 중 하나인 내집 마련에 대한 목표를 달성하기 위해 청약 시스템을 본인이 직접 알아보고 조건을 알아야 한다는 불편함이 있음 
- 목적 : 청약 시스템 앱의 불편한 점을 하나로 통합해서 나의 조건에 맞는 추천해주기 위함
- 기대효과 : ① 생성형 AI를 활용하여 쉽게 청약 정보를 확인 ② 나의 조건에 맞는 청약 정보 확인  

## [SOS 서비스 설계]
* 중요점 : 새로나온것 / 지난것을 구분할 수 있어야 하고 업데이트는 주 1회정도 해주어야 함

## [활용 OPEN API] 
- 한국토지주택공사_공공임대주택 단지정보 조회 서비스(https://www.data.go.kr/data/15058476/openapi.do)
- 한국토지주택공사_임대주택단지 조회 서비스(https://www.data.go.kr/data/15059475/openapi.do)
- 한국토지주택공사_분양임대공고문 조회 서비스(https://www.data.go.kr/data/15058530/openapi.do)

☆ API를 이용해 최근 정보에 맞도록 사용자에게 맞춤 추천해주기 ☆

## [일정 계획 및 진행사항]
- 07/01 : 아이디어 선정 및 간단한 설계 진행
- 07/02 ~ 07/03 : 공공포털 데이터 API 키 호출 및 데이터 파악, API 키 에러 발생 (ERROR : 30)
- 07/04 : Figma로 Input/Output 필요 정보 선정 및 프롬프트 구조 설계
- 07/05 : OpenAPI 데이터 필요한 정보 추출 및 프롬프트 세부 설계
- 07/06 ~ 07/07 : RAG 컬렉션(rentalhouse.csv) 생성 및 등록
- 07/08 : 테스트 데이터(rentalhouse_test.xlsx) 등록 및 테스트 실행 

## [문제 및 해결]
- 공공데이터포털에서 제공하는 공공임대주택 단지정보 조회 서비스 OPEN API ServiceKey의 문제가 있어 데이터를 불러올 수 없음
- 원티드 LaaS API 호출 시 401 ERROR 발생
- SSL ERROR 발생으로 인한 방화벽 문제 해결
- Open API ServiceKey 문제 -> url 및 요청 메세지 명세 토대로 변경 후 해결

## [제출 마감기한]
07/01 ~ 07/14 23:59

## [참고자료]
- 원티드 Laas 활용가이드 (https://laas.wanted.co.kr/docs/guide/api/api-lang)
- Figma 프롬프트 데이터 설계 링크 (https://www.figma.com/board/pfqHRc2fZQ04SnamhHZf6I/SOS(Subscription-recOmmendation-System)?node-id=2-419&t=9v8XcJYbyYNaN3An-1)
