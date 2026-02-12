from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    text = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Автор')
    
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В работе'),
        ('done', 'Выполнена'),
    ]
    
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='new')
    
    additional_authors = models.ManyToManyField(User, blank=True, related_name='additional_tasks',verbose_name='Дополнительные авторы')

    priority = models.CharField(max_length=10,
        choices=[
            ('low', 'Низкий'),
            ('medium', 'Средний'),
            ('high', 'Высокий'),
        ],
        default='medium'
    )
    
    created_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    
    def __str__(self):
        return self.title