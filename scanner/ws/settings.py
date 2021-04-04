import json
import os
import string
from random import sample

from uuid import uuid4


class BaseSettings:
    uuid: str
    password: str
    url: str
    api: str


settings_path = os.path.join(os.path.dirname(__file__), "settings.json")


class Settings(BaseSettings):
    _settings = None

    @classmethod
    def load(cls):
        if cls._settings is None:
            with open(settings_path, "r") as f:
                cls._settings = json.load(f)

        if "uuid" not in cls._settings or not cls._settings["uuid"]:
            cls.generate()

        obj = Settings()

        return obj

    @classmethod
    def save(cls):
        with open(settings_path, "w") as f:
            json.dump(cls._settings, fp=f)

    @classmethod
    def generate(cls):
        cls._settings["uuid"] = str(uuid4())
        cls._settings["password"] = "".join(sample("".join([
            string.ascii_lowercase,
            string.ascii_uppercase,
            string.digits,
            string.punctuation
        ]), 64))
        cls.save()

    def __getattr__(self, item):
        if item in Settings._settings:
            return Settings._settings[item]

    def __setattr__(self, key, value):
        Settings._settings[key] = value
        Settings.save()


settings = Settings.load()
