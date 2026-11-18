import hashlib
import secrets
from datetime import timedelta
from django.utils import timezone
from .models import PasswordReset

CODE_TTL_MINUTES = 30

def create_reset_code(user):
    # Генерация случайного кода
    raw_code = secrets.token_urlsafe(32)
    # Шифрование кода перед сохранением в БД
    code_hash = hashlib.sha256(raw_code.encode('utf-8')).hexdigest()
    
    PasswordReset.objects.create(
        user=user,
        code_hash=code_hash,
        expires_at=timezone.now() + timedelta(minutes=CODE_TTL_MINUTES),
    )
    return raw_code # Отправляется пользователю, в базе не хранится