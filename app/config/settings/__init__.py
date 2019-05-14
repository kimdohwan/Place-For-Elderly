import os
import re

DJANGO_SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE')

# - 기본적으로 dev.py 의 setting 을 사용하도록 설정
# - MODULE_NAME : base.py 에서 사용할 module 설정 변수
if not DJANGO_SETTINGS_MODULE or DJANGO_SETTINGS_MODULE == 'config.settings':
    MODULE_NAME = 'dev'
    from .dev import *
else:
    p = re.compile(r'config.settings.(?P<name>.*)')
    b = p.search(DJANGO_SETTINGS_MODULE)
    MODULE_NAME = b.group("name")

# 사용하는 setting 출력
print(DJANGO_SETTINGS_MODULE, MODULE_NAME)
