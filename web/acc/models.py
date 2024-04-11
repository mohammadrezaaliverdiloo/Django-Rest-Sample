from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        
    
