import dataclasses
from marshmallow_dataclass import dataclass
from typing import List, Optional


@dataclass
class CaptchaSubmissionStatus:
    success: bool
    img: str

@dataclass
class ResponseModel:
    UUID:  str = dataclasses.field(metadata={'required':False, 'dump_default': "Exa"})
    submitSuccess: bool = dataclasses.field(metadata={'required':False})
    attemptAt: str = dataclasses.field(metadata={'required':False})
    completedAt: str = dataclasses.field(metadata={'required':False})
    attempts: int = dataclasses.field(metadata={'required':False})
    logs: str = dataclasses.field(metadata={'required':False})
    state: str = dataclasses.field(metadata={'required':False})
    captcha: List[CaptchaSubmissionStatus] = dataclasses.field(metadata={'required':False})
    error: List[str] = dataclasses.field(metadata={'required':False})

class CaptchaSubmissionStatus2:
    def __init__(self, success, img):
        self.success = success
        self.img = img

class ResponseModel2:
    def __init__(self, UUID, submitSuccess, attemptAt, completedAt, attempts, responseMessage):
        self.UUID = UUID
        self.submitSuccess = submitSuccess
        self.attemptAt = attemptAt
        self.completedAt = completedAt
        self.attempts = attempts
        self.responseMessage = responseMessage
