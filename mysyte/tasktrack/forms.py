from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'text', 'priority', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
User = get_user_model()

class RegisterForm(UserCreationForm):
    """
    Форма регистрации нового пользователя.
    Расширяет стандартную UserCreationForm, добавляя email.
    """
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@mail.com'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Придумайте имя пользователя'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем CSS классы ко всем полям
        for field_name in self.fields:
            if field_name not in ['username', 'email']:
                self.fields[field_name].widget.attrs.update({
                    'class': 'form-control'
                })
    
    def clean_email(self):
        """Проверка уникальности email."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Этот email уже используется.')
        return email


class LoginForm(AuthenticationForm):
    """
    Форма входа пользователя.
    Можно кастомизировать, если нужно.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Добавляем CSS классы и placeholder'ы
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Имя пользователя или email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Пароль'
        })

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'text', 'priority', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        } 
        from django import forms
from .models import Task
from django.utils import timezone

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        #fields = ['title', 'text', 'priority', 'deadline', 'additional_authors']
        fields = ['title', 'text', 'priority', 'deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'additional_authors': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
    
    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        if deadline and deadline < timezone.now().date():
            raise forms.ValidationError("Срок выполнения не может быть в прошлом!")
        return deadline     