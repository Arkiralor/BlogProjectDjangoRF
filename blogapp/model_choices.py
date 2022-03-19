
GENRE_CHOICES = (
    ('Fiction', 'fiction'),
    ('Non-Fiction', 'non-fiction'),
    ('Poetry', 'poetry'),
    ('Journal', 'journal'),
    ('Biography', 'biography'),
    ('Textbook', 'textbook'),
    ('Self-Help', 'self-help'),
    ('Encyclopedia', 'encyclopedia'),
    ('Dictionary', 'dictionary'),
    ('Other', 'other'),
)

LANG_DICT = {
    "am": "Amharic",
    "ar": "Arabic",
    "as": "Assamese",
    "bn": "Bengali",
    "bo": "Tibetan",
    "ca": "Catalan",
    "de": "German",
    "default": "Unknown",
    "en": "English",
    "es": "Spanish",
    "fa": "Persian",
    "fr": "French",
    "gu": "Gujarati",
    "hi": "Hindi",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "lo": "Lao",
    "ml": "Malayalam",
    "mr": "Marathi",
    "ms": "Malay",
    "my": "Burmese",
    "ne": "Nepali",
    "no": "Norweigian",
    "or": "Oriya",
    "pa": "Punjabi",
    "pt": "Portuguese",
    "ru": "Russian",
    "sa": "Sanskrit",
    "sd": "Sindhi",
    "si": "Sinhala",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tl": "Tagalog",
    "tr": "Turkish",
    "ur": "Urdu",
    "vi": "Vietnamese",
    "zh-cn": "Chinese"
}

if __name__ == "__main__":
    from datetime import datetime
    from os import sep

    print(f"[{datetime.now()}]   [{__file__.split(sep)[-1]}]  as  [{__name__}]    IMPROPER EXECUTION")
    print(f"[Error]   [{__file__.split(sep)[-1]}]    INTENDED FOR IMPORT ONLY")
