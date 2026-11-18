from django.conf import settings
from django.db import models
from django.utils import timezone

class Entry(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='entries', 
        verbose_name='Владелец'
    )
    content = models.TextField('Текст записи')
    mood_score = models.IntegerField('Оценка настроения')
    ai_analysis = models.TextField('ИИ-анализ', blank=True, null=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='entries', blank=True)

    class Meta:
        db_table = 'entries'
        ordering = ['-created_at']

class Tag(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    class Meta:
        db_table = 'tags'

class PasswordReset(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='reset_codes'
    )
    code_hash = models.CharField(max_length=64, unique=True)
    expires_at = models.DateTimeField()
    used_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'password_resets'