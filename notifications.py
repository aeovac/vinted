import smtplib
from abc import ABC, abstractmethod
from typing import Protocol
from dataclasses import dataclass


var = ""

@dataclass
class Message(object):
    title: str
    content: str

class Model(ABC):
    @abstractmethod
    def __call__(self, message: Message) -> int:
        ...
