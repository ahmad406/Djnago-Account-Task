
from reglogin.models import Profile
from django import  forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields, widgets



class SignUpForm(UserCreationForm):
    username:forms.TextInput()
    email = forms.EmailField()
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)
    

  
    def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'
    def _init_(self, *args, **kwargs):
        super(SignUpForm, self)._init_(*args, **kwargs)

        for field_name, field in self.fields.items():
            self.fields[field_name].widget.attrs['placeholder'] = field.label


# class ImageForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = ('profile_pic',)

#     def __init__(self, *args, **kwargs):
#             super(SignUpForm, self).__init__(*args, **kwargs)
#             for visible in self.visible_fields():
#                 visible.field.widget.attrs['class'] = 'form-control'

class LoginForm(AuthenticationForm):
    username:forms.TextInput()
    password:forms.PasswordInput()

    def __init__(self, *args, **kwargs):
            super(LoginForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'


class UpdateProfile(UserChangeForm):
    password= None

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login','is_active']
        labels = {'email':'Email'}
        widgets = {
        'date_joined':forms.TextInput(attrs={'readonly':'readonly'}),
        'last_login':forms.TextInput(attrs={'readonly':'readonly'}),
        'is_active':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'})
        }

    def __init__(self, *args, **kwargs):
        super(UpdateProfile, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ProfileP(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic',)


class SetPass(SetPasswordForm):
    class Meta:
            model =User
            fields = ("new_password1","new_password2")

    def __init__(self, *args, **kwargs):
            super(SetPass, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'