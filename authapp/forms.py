from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms as forms_lib


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class UserCreateForm(UserCreationForm):
    username = forms_lib.CharField(widget=forms_lib.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'username'}),
                                   required=True)
    full_name = forms_lib.CharField(widget=forms_lib.TextInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Иванов Иван Иванович'}),
                                    required=True)
    email = forms_lib.EmailField(widget=forms_lib.EmailInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'ivanov@mail.ru'}),
                                 required=True)
    photo = forms_lib.ImageField(widget=forms_lib.FileInput(attrs={'class': 'custom-file-input'}),
                                 required=False)
    number = forms_lib.IntegerField(widget=forms_lib.NumberInput(attrs={'class': 'form-control',
                                                                        'placeholder': '1234'}),
                                    required=True)
    telegram_id = forms_lib.IntegerField(widget=forms_lib.NumberInput(attrs={'class': 'form-control',
                                                                             'placeholder': '12345678'}),
                                         required=False)

    class Meta:
        model = get_user_model()
        fields = ('username', 'full_name', 'number', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class UserProfileForm(UserChangeForm):
    username = forms_lib.CharField(widget=forms_lib.TextInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'username',
                                                                     'readonly': True}))
    full_name = forms_lib.CharField(widget=forms_lib.TextInput(attrs={'class': 'form-control',
                                                                      'placeholder': 'Иванов Иван Иванович'}),
                                    required=True)
    email = forms_lib.EmailField(widget=forms_lib.EmailInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'ivanov@mail.ru'}),
                                 required=True)
    photo = forms_lib.ImageField(widget=forms_lib.FileInput(attrs={'class': 'custom-file-input'}),
                                 required=False)
    number = forms_lib.IntegerField(widget=forms_lib.NumberInput(attrs={'class': 'form-control',
                                                                        'placeholder': '1234'}),
                                    required=True)
    telegram_id = forms_lib.IntegerField(widget=forms_lib.NumberInput(attrs={'class': 'form-control',
                                                                             'placeholder': '12345678'}),
                                         required=False)

    class Meta:
        model = get_user_model()
        fields = ('username', 'full_name', 'number', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
