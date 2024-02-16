
from enum import Enum

VALID_IMAGE = ["image", "i"]
VALID_VIDEO = ["video", "v"]
VALID_AUDIO = ["audio", "a"]
VALID_TEXT = ["text", "t"]
VALID_MULTIMODAL = ["multimodal", "mm"]

class Modality(Enum):
    IMAGE = 1
    VIDEO = 2
    AUDIO = 3
    TEXT = 4
    MULTIMODAL = 5
    
    @staticmethod
    def from_string(modality):
        modality = modality.lower()
        if modality in VALID_IMAGE:
            return Modality.IMAGE
        elif modality in VALID_VIDEO:
            return Modality.VIDEO
        elif modality in VALID_AUDIO:
            return Modality.AUDIO
        elif modality in VALID_TEXT:
            return Modality.TEXT
        elif modality in VALID_MULTIMODAL:
            return Modality.MULTIMODAL
        else:
            raise ValueError("Invalid modality: {}".format(modality))
    
    def __str__(self):
        if self == Modality.IMAGE:
            return "image"
        elif self == Modality.VIDEO:
            return "video"
        elif self == Modality.AUDIO:
            return "audio"
        elif self == Modality.TEXT:
            return "text"
        elif self == Modality.MULTIMODAL:
            return "multimodal"
        else:
            raise ValueError("Invalid modality: {}".format(self))
        
    def __repr__(self):
        if self == Modality.IMAGE:
            return "Modality.IMAGE"
        elif self == Modality.VIDEO:
            return "Modality.VIDEO"
        elif self == Modality.AUDIO:
            return "Modality.AUDIO"
        elif self == Modality.TEXT:
            return "Modality.TEXT"
        elif self == Modality.MULTIMODAL:
            return "Modality.MULTIMODAL"
        else:
            raise ValueError("Invalid modality: {}".format(self))