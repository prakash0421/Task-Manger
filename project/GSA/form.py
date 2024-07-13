from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Register,Task


class Taskform(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'
        assigned_to = forms.ModelChoiceField(queryset=Register.objects.all(), widget=forms.Select())
        widgets = {
            'due_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
class Registerform(UserCreationForm):
    address=forms.CharField(max_length=200)
    class Meta:
        model=Register
        fields=['username','email','mobile','address','password1','password2',]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
        self.fields['password1'].error_messages = {'required': ''}
        self.fields['password2'].error_messages = {'required': ''}
        self.fields['email'].error_messages = {'required': ''}
        self.fields['username'].error_messages = {'required': ''}
        self.fields['mobile'].error_messages = {'required': ''}