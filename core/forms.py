from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from core.models import User

class AdminSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_auser = True
        user.save()
        # student = Student.objects.create(user=user)

        return user

class UserSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_nuser = True
        user.save()
        # student = Student.objects.create(user=user)
        return user