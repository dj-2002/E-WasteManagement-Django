from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUp(UserCreationForm):
    username=forms.CharField()
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()
    email=forms.EmailField()
    address=forms.CharField(max_length=200)

    class Meta:
        model=User
        fields=('username','email','password1','password2','address')
        help_texts={
            'email':None,
        }

    def save(self, commit=True):
        user=super(UserCreationForm,self).save(commit=False)
        user.address=self.cleaned_data['address']
        if commit:
            user.save()
        return super().save(commit=commit)    


class ImageHandler(forms.Form):
    image=forms.ImageField()        