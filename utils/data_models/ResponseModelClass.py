from marshmallow_dataclass import dataclass
from typing import List


@dataclass
class CaptchaSubmissionStatus:
    success: bool
    img: str

@dataclass
class PersonModel:
    UUID: str
    submitSuccess: bool
    attemptAt: str
    completedAt: str
    attempts: int
    logs: str
    state: str
    captcha: List[CaptchaSubmissionStatus]
    error: str