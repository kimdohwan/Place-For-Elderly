from django.db import models


class Facility(models.Model):
    SIGUN_CD = models.CharField(verbose_name='시군코드', max_length=255)
    SIGUN_NM = models.CharField(verbose_name='시군명', max_length=255)
    BIZPLC_NM = models.CharField(verbose_name='사업장명', max_length=255)
    LICENSG_DE = models.DateField(verbose_name='인허가일자', null=True)
    BSN_STATE_NM = models.CharField(verbose_name='영업상태명', max_length=255, null=True)
    CLSBIZ_DE = models.DateField(verbose_name='폐업일자', null=True)
    LOCPLC_AR = models.FloatField(verbose_name='소재지면적(㎡)', null=True)
    ENTRNC_PSN_CAPA = models.IntegerField(verbose_name='입소정원(명)', null=True)
    QUALFCTN_POSESN_PSN_CNT = models.IntegerField(verbose_name='자격소유인원수(명)', null=True)
    TOT_PSN_CNT = models.IntegerField(verbose_name='총인원수(명)', null=True)
    REFINE_LOTNO_ADDR = models.CharField(verbose_name='소재지지번주소', max_length=255, null=True)
    REFINE_ROADNM_ADDR = models.CharField(verbose_name='소재지도로명주소', max_length=255, null=True)
    REFINE_ZIP_CD = models.IntegerField(verbose_name='소재지우편번호', null=True)
    REFINE_WGS84_LAT = models.DecimalField(verbose_name='WGS84위도', max_digits=17, decimal_places=15, null=True)
    REFINE_WGS84_LOGT = models.DecimalField(verbose_name='WGS84경도', max_digits=18, decimal_places=15, null=True)
