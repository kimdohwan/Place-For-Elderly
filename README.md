[개요 및 작업내역](https://github.com/kimdohwan/MyStudy/blob/master/project/PlaceForElderly.md)

#### Requirements

- python(3.6.7)
- django(2.2.1)
- zappa(0.48.2)
- psycopg2(2.8.2)
- mysqlclient(1.4.2)
- requests(2.21.0)

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

  



