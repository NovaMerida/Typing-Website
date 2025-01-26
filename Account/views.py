from django.shortcuts import render
from django.db.models import F
from django.views import generic
# Create your views here.
from .models import AccountCreation
class AccountCreateView(generic.ListView):
    def set_user_name(self):
        return AccountCreation.Account_id
    def set_password(self):
        return AccountCreation.Account_pw
    def set_email(self):
        return AccountCreation.Account_email
    pass
class AccountUpdateView:
    def change_user_name(self):
        pass
    def change_password(self):
        pass
    def change_email(self):
        pass
    pass
class AccountDeleteView:
    def delete_user(self):
        pass
class AccountLoginView:
    def login(self):
        pass