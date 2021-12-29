from django.db import models

from commons.models import BaseModel


class ClientModel(BaseModel):
    client_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)
    seconds_delivered_per_month = models.IntegerField(null=False)
    is_archived = models.BooleanField()

    class Meta:
        db_table = 'clients'


class UserAccountModel(BaseModel):
    user_id = models.IntegerField(primary_key=True)
    client_id = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    user_type = models.IntegerField()
    email = models.CharField(max_length=254, null=False)
    password = models.CharField(max_length=255, null=True)
    remember_token = models.CharField(max_length=255, null=True)
    last_name_kanji = models.CharField(max_length=255, null=True)
    first_name_kanji = models.CharField(max_length=255, null=True)
    last_name_kana = models.CharField(max_length=255, null=True)
    first_name_kana = models.CharField(max_length=255, null=True)
    nickname = models.CharField(max_length=255, null=True)
    sex = models.CharField(max_length=255, null=True)
    is_sex_public = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(null=True)
    is_date_of_birth_public = models.BooleanField(max_length=255, null=True)
    phone = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'user_custom'
