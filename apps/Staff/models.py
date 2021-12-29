from django.db import models

# Create your models here.
class UserModel(models.Model):
    job_title_code = models.CharField(max_length=32)
    company_code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True)
    phone_family = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=255, null=True)
    gender = models.BooleanField(null=True)
    birthday = models.DateField(null=True)
    other_email = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employees'
