from marshmallow import Schema
from marshmallow_dataclass import dataclass

class Failed_Captcha:
    def __init__(self, dateAndTime, base64Value):
        self.dateAndTime = dateAndTime
        self.base64Value = base64Value
