from django import forms
from .models import *


class UserModelEditForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, disabled=True)  # disable username editing

    class Meta:
        model = User
        fields = ['username', 'group', 'email', 'status']

# class GroupModelEditForm(forms.ModelForm):
#     class Meta:
#         model = Group
#         fields = ['username', 'group', 'status']
