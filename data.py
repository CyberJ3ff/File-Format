IMAGE = {
    "JPG": {
        "HEAD": ["FF D8 FF DB", "FF 4F FF 51", "FF D8 FF EE", "FF D8 FF E0 00 10 4A 46 49 46 00 01", "FF D8 FF E1 ?? ?? 45 78 69 66 00 00", "FF D8 FF E0"],
        "TAIL": []
    },
    "PNG": {
        "HEAD": ["89 50 4E 47 0D 0A 1A 0A"],
        "TAIL": ["00 00 00 00 49 45 4E 44 AE 42 60 82"]
    },
    "GIF": {
        "HEAD": ["47 49 46 38 37 61", "47 49 46 38 39 61"],
        "TAIL": [],
    },
    "WEBP": {
        "HEAD": ["52 49 46 46 ?? ?? ?? ?? 57 45 42 50"],
        "TAIL": [],
    },
    "BMP": {
        "HEAD": ["42 4D"],
        "TAIL": [],
    },
    "BPG": {
        "HEAD": ["42 50 47 FB"],
        "TAIL": [],
    },
    "TIF": {
        "HEAD": ["49 49 2A 00"],
        "TAIL": [],
    }
}

COMPRESS = {
    "ZIP/APK/DOCX/XLSX": {
        "HEAD": ["50 4B 03 04"],
        "TAIL": ["50 4B 05 06 ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ??"],
    },
    "RAR v1.5 onwards": {
        "HEAD": ["52 61 72 21 1A 07 01 00"],
        "TAIL": [],
    },
    "RAR v5.0 onwards": {
        "HEAD": ["52 61 72 21 1A 07 01 00"],
        "TAIL": []
    },
    "7ZIP": {
        "HEAD": ["37 7A BC AF 27 1C"],
        "TAIL": []
    }
}

AUDIO = {
    "MP3": {
        "HEAD": ["FF FB", "FF F3", "FF F2", "49 44 33"],
        "TAIL": []
    },
    "WAV": {
        "HEAD": ["52 49 46 46 ?? ?? ?? ?? 57 41 56 45"],
        "TAIL": []
    },
    "OGG": {
        "HEAD": ["4F 67 67 53"],
        "TAIL": []
    },
}

VIDEO = {
    "MP4": {
        "HEAD": ["?? ?? ?? ?? 66 74 79 70 69 73 6F 6D"],
        "TAIL": []
    },
    "3GP/3G2": {
        "HEAD": ["?? ?? ?? ?? 66 74 79 70 33 67"],
        "TAIL": []
    },
    "MP4/3GP/3G2": {
        "HEAD": ["?? ?? ?? ?? 66 74 79 70"],
        "TAIL": []
    },
    "AVI": {
        "HEAD": ["52 49 46 46 ?? ?? ?? ?? 41 56 49 20"],
        "TAIL": []
    }
}

OTHER = {
    "PDF": {
        "HEAD": ["25 50 44 46 2D"],
        "TAIL": []
    },
    "DOC/XLS/PPT/MSI/MSG": {
        "HEAD": ["D0 CF 11 E0 A1 B1 1A E1"],
        "TAIL": []
    },
    "MKV/MKA/MKS/MK3D/WEBM": {
        "HEAD": ["1A 45 DF A3"],
        "TAIL": []
    }
}

FILE_DATA = [IMAGE, COMPRESS, AUDIO, VIDEO, OTHER]
