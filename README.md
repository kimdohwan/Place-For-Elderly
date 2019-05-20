## Place for elderly

#### Intro

- 경기도 노인 요양시설 현황 정보 제공
- URL: https://j6sqja4hg2.execute-api.ap-northeast-2.amazonaws.com/production
- python, django, aws lambda, aws rds(postgres, mysql), docker

#### Requirements

- python(3.6.7)
- django(2.2.1)
- zappa(0.48.2)
- psycopg2(2.8.2)
- mysqlclient(1.4.2)
- requests(2.21.0)

#### 작업 내역

- [x] : 구현 완료 

- [ ] : 미구현(진행중)



- 경기도 노인 요양시설 현황 데이터 
  - [x] 공공데이터 포털 api key 취득 및 url 요청([open_api.py](https://github.com/kimdohwan/Place-For-Elderly/blob/master/app/open_api/open_api.py))
  - [ ] 연관 데이터(의료 시설, 생활 시설 등) 
- Django app
  - facilities
    - [x] ```manage.py setapidata``` : 요양시설 api data 저장([setapidata.py](https://github.com/kimdohwan/Place-For-Elderly/blob/master/app/facilities/management/commands/setapidata.py))
    - [x] 시설 목록 및 상세 정보 페이지
    - [x] 주소 검색 / 이름 검색
  - members
    - [x] 로그인 / 로그아웃
    - [x] 관심 시설 목록
    - [ ] 유져 정보 수정
    - [ ] 로그인 API : Naver / Google
  - REST API
    - [ ] 시설 리스트 
    - [ ] 시설 상세 정보
    - [ ] 유져 로그인 / 회원 가입 등
- 지도 API

  - [ ] 네이버 지도 or 구글 지도

    - 자바스크립트 비동기 처리 - 요양 시설의 위도와 경도 활용
- 데이터베이스
  - [x] mysql
    - lambda 배포 시 mysqlclient 버젼 충돌 발생 / dev 환경에서만 사용 가능
  - [x] postgres
    - AWS RDS 사용 시 : private subnet 과 public subet 포함한 subnet 그룹 설정 필요
- 배포
  - [x] zappa 설정([zappa_settings.json](https://github.com/kimdohwan/Place-For-Elderly/blob/master/app/zappa_settings.json))
    - ```zappa init``` : AWS S3 버킷 설정 / 셋팅 모듈 설정(config.settings.production)
    - vpc_config : lambda 네트워크에 설정될 내용
      - 서브넷: private subnet 설정
      - 보안그룹: NAT 보안그룹 설정
  - [ ] 도메인 연결


- AWS Lambda 배포 전 사전작업
  - [x] VPC 설정
    - private subnet, public subnet 생성
    - routing table 생성 및 설정
      - main table : public subnet 연결 / internet gateway 연결
      - sub table : private subnet 연결 / NAT(EC2 instance) 연결
    - internet gateway 생성 및 vpc 연결
  - [x] NAT(EC2 instance)
    - 네트워크: 위와 동일한 VPC
    - 서브넷: 위에서 생성한 public subnet 연결
    - 퍼블릭 IP 자동 할당: 활성화
    - 소스/대상 확인: 비활성화
    - 탄력적 IP 주소 연결

#### app/.secret

- app/.secret/base.json 

  ```
  {
    "API_KEY": "공공데이터 포털 API Key",
    "SECRET_KEY": "Django SECRET KEY"
  }              
  ```

- app/.secret/dev.json

  ```
  {
    "LOCAL_POSTGRES_DATABASES": {
      "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "USER": "",
        "NAME": "",
        "HOST": "localhost",
        "PORT": "",
        "PASSWORD": ""
      }
    },
    "AWS_POSTGRES_DATABASES": {
      "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "USER": "",
        "NAME": "",
        "HOST": "",
        "PORT": "",
        "PASSWORD": ""
      }
    },
    "AWS_MYSQL_DATABASES": {
      "default": {
        "ENGINE": "django.db.backends.mysql",
        "USER": "",
        "NAME": "",
        "HOST": "",
        "PORT": "",
        "PASSWORD": ""
      }
    },
    "ALLOWED_HOSTS": [
      "localhost",
      "127.0.0.1"
    ]
  }
  ```

- app/.secrets/production.json

  ```
  {
    "AWS_MYSQL_DATABASES": {
      "default": {
        "ENGINE": "django.db.backends.mysql",
        "USER": "",
        "NAME": "",
        "HOST": "",
        "PORT": "3306",
        "PASSWORD": "",
        "OPTIONS": {
          "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
          "charset": "utf8mb4"
        }
      }
    },
  
    "AWS_POSTGRES_DATABASES": {
      "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "USER": "",
        "NAME": "",
        "HOST": "",
        "PORT": "5432",
        "PASSWORD": ""
      }
    },
  
    "ALLOWED_HOSTS": [
      ".execute-api.ap-northeast-2.amazonaws.com"
    ]
  }
  ```

  



#### 