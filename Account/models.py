from django.db import models

from TypingPractice.views import account


# Create your models here.
class AccountCreation(models.Model):
    Account_id = models.CharField(max_length=25)
    Account_pw = models.CharField(max_length=25)
    Account_email = models.EmailField(max_length=25)
    data = [Account_id, Account_pw, Account_email]
    def __str__(self):
        return self.data