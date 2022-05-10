from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm, TextInput, Select

from app.models import Ai1, Ai2

from django.contrib.auth import authenticate
from django import forms


class UsersLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, )

    def __init__(self, *args, **kwargs):
        super(UsersLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            "name": "username"})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            "name": "password"})

    def clean(self, *args, **keyargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exists")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("User is no longer active")

        return super(UsersLoginForm, self).clean(*args, **keyargs)


class ReadOnlyFieldsMixin(object):
    readonly_fields = ()

    def __init__(self, *args, **kwargs):
        super(ReadOnlyFieldsMixin, self).__init__(*args, **kwargs)
        for field in (field for name, field in self.fields.iteritems() if name in self.readonly_fields):
            field.widget.attrs['disabled'] = 'true'
            field.required = False

    def clean(self):
        cleaned_data = super(ReadOnlyFieldsMixin, self).clean()
        for field in self.readonly_fields:
            cleaned_data[field] = getattr(self.instance, field)

        return cleaned_data


class AddPostFormAi1(ModelForm):
    class Meta:
        model = Ai1
        fields = ('id', 'current', 'sts',)
        labels = {
            'id': '',
            'current': '',
            'sts': '',
        }
        widgets = {
            'id': TextInput(attrs={
                'class': 'post-id',
                'required': True,
                'readonly': 'readonly',
            }),
            'current': TextInput(attrs={
                'class': 'post-current',
                'required': True,
                'readonly': 'readonly',
            }),
            'sts': Select(attrs={
                'class': 'post-sts',
                'required': True,

            }),
        }


class AddPostFormAi2(ModelForm):
    class Meta:
        model = Ai2
        fields = ('id', 'current', 'sts',)
        labels = {
            'id': '',
            'current': '',
            'sts': '',
        }
        widgets = {
            'id': TextInput(attrs={
                'class': 'post-id',
                'required': True,
                'readonly': 'readonly',
            }),
            'current': TextInput(attrs={
                'class': 'post-current',
                'required': True,
                'readonly': 'readonly',
            }),
            'sts': Select(attrs={
                'class': 'post-sts',
                'required': True,

            }),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))