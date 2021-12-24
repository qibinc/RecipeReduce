from typing import List, Optional


class Lang:
    ALL: List[str] = ["en", "zh"]
    DEFAULT: str = "en"
    lang: Optional[str] = None

    @classmethod
    def set(cls, lang: str):
        assert lang in cls.ALL
        cls.lang = lang

    @classmethod
    def get(cls):
        assert cls.lang is not None
        return cls.lang
