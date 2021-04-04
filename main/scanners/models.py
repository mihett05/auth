from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class ScannerManager(BaseUserManager):
    def create_user(self, uuid, password, **extra):
        if not uuid:
            raise ValueError("UUID must be set")
        uuid = uuid.strip().lower()

        user = self.model(uuid=uuid, **extra)
        user.set_password(password)
        user.save()

        return user


class Scanner (AbstractBaseUser):
    uuid = models.UUIDField(unique=True)  # uuid = scanner login

    USERNAME_FIELD = "uuid"
    REQUIRED_FIELDS = []

    objects = ScannerManager()

    def __str__(self):
        return str(self.uuid)
