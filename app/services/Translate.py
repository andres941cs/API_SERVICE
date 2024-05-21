import pykakasi
from korean_romanizer.romanizer import Romanizer
class Translate:
    def __init__(self):
        # Initialize any necessary variables or resources here
        pass

    def romanize_japanese(self, lyric):
        kks = pykakasi.kakasi()
        kks.setMode("H","a") # Hiragana to ascii, default: no conversion
        kks.setMode("K","a") # Katakana to ascii, default: no conversion
        kks.setMode("J","a") # Japanese to ascii, default: no conversion
        kks.setMode("r","Hepburn")
        kks.setMode("s", True)

        conv = kks.getConverter()
        result = conv.do(lyric)
        return result

    def romanize_korean(self, lyric):
        r = Romanizer(lyric)
        result =r.romanize()
        return result

    def detect_language(self, text):
        caracteres_japoneses = set(range(0x3040, 0x30FF)) | set(range(0x31F0, 0x31FF)) | set(range(0xFF66, 0xFF9F))
        caracteres_coreanos = set(range(0xAC00, 0xD7A4)) | set(range(0x1100, 0x11FF)) | set(range(0x3130, 0x318F))

        caracteres_texto = set(ord(caracter) for caracter in text)
        isJaponese = bool(caracteres_texto & caracteres_japoneses)
        isKorean = bool(caracteres_texto & caracteres_coreanos)
        if isJaponese:
            return "JAPONESE"
        elif isKorean:
            return "KOREAN"
        else:
            return "OTHER"


