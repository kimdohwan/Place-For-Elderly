from django.core.management import BaseCommand

from ...models import Facility
from ...utils.open_api import get_api_data


class Command(BaseCommand):
    def handle(self, *args, **options):
        # try,except 를 사용해 Exception 발생 시, 이전 DB 상태에 영향 주지 않도록 처리
        try:
            # facility 항목 모두 지운 후 진행
            Facility.objects.all().delete()
            # get_api_data() 로부터 시설 리스트를 받아옴
            api_data = get_api_data()
            # Facility obj 를 생성해 list 에 할당
            objs = [Facility(**kwargs) for kwargs in api_data]
            # bulk_create() 를 사용해 한번에 저장하도록 처리
            Facility.objects.bulk_create(objs)

            print('{} 개의 Facility 저장.'.format(Facility.objects.all().count()))

        except:
            print("Can't set API database")
