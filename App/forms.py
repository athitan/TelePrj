from django import forms

from django.forms import ModelForm
from App.models import prepaid,recs,postpaids,postpayment1,postrecs,payment1,prepayment

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class pForm(forms.ModelForm):
    class Meta:
        model=prepaid
        fields='__all__'
class pm(forms.ModelForm):
    class Meta:
        model=prepayment
        fields='__all__'

#class pm1(forms.ModelForm):
#    class Meta:
#        model=payment1
#        fields='__all__'

class postForm(forms.ModelForm):
    class Meta:
        model=postpaids
        fields='__all__'
class postm(forms.ModelForm):
    class Meta:
        model=postpayment1
        fields='__all__'
#class postm1(forms.ModelForm):
#    class Meta:
#        model=upipayment
#        fields='__all__'

class recf(forms.ModelForm):
    class Meta:
        model = recs
        fields = '__all__'

class postrecf(forms.ModelForm):
    class Meta:
        model = postrecs
        fields = '__all__'

class pm1(forms.ModelForm):
    class Meta:
        model=payment1
        fields='__all__'

# class pm5(forms.ModelForm):
#     class Meta:
#         model=prepayment5
#         fields='__all__'


