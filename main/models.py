from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class TestUser(models.Model):
    first_name = models.CharField(
        max_length=255
    )

    @staticmethod
    def all():
        return TestUser.objects.all()


class Candidate(models.Model):
    first_name = models.CharField(
        max_length=255
    )
    second_name = models.CharField(
        max_length=255,
        blank=True
    )
    third_name = models.CharField(
        max_length=255,
        blank=True
    )
    phone = PhoneNumberField(unique=True)
    email = models.EmailField(null=True, blank=True)
    photo = models.BinaryField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    @staticmethod
    def find_candidate_by_id(candidate_id):
        candidate = Candidate.objects.get(id=candidate_id)
        return candidate

    @staticmethod
    def find_candidate_by_phone(phone_number):
        candidate = Candidate.objects.get(phone=phone_number)
        return candidate

    @staticmethod
    def all():
        return Candidate.objects.all()