from django.contrib.auth.models import AbstractUser
from django.db import models

from facilities.models import Facility


# - ForeignKey 작성 시 사용해 줄수 있는 model 경로
# Facility = 'facilities.Facility'

class User(AbstractUser):

    @property
    def facility_list(self):
        facility_list = []
        # like_queryset = self.likefacility_set.prefetch_related()
        like_queryset = self.likefacility_set.all()

        for like_obj in like_queryset:
            facility_obj = like_obj.facility
            facility_list.append(facility_obj)

        return facility_list


class LikeFacility(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    facility = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
    )
