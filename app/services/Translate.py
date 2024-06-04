import pykakasi
from korean_romanizer.romanizer import Romanizer

class Translate:
    def __init__(self):
        pass

    # ROMANIZE JAPANESE
    def romanize_japanese(self, lyric):
        kks = pykakasi.kakasi()
        kks.setMode("H","a")
        kks.setMode("K","a")
        kks.setMode("J","a")
        kks.setMode("r","Hepburn")
        kks.setMode("s", True)

        conv = kks.getConverter()
        result = conv.do(lyric)
        return result

    # ROMANIZE KOREAN
    def romanize_korean(self, lyric):
        r = Romanizer(lyric)
        result =r.romanize()
        return result

    # DETECT LANGUAGE
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


