import re

def normalize_string(s: str) -> str:
    """
    1) Replace non-alphanumeric chars (underscore, hyphen, dot, etc.) with spaces.
    2) Insert a space before an uppercase letter that follows a lowercase or digit.
    3) Strip.
    """
    # 1) Replace underscores etc. with spaces
    s = re.sub(r'[^a-zA-Z0-9]+', ' ', s)
    # 2) Insert space before uppercase letter that follows a lowercase or digit
    s = re.sub(r'(?<=[a-z0-9])([A-Z])', r' \1', s)
    return s.strip()

def to_camel_case(s: str) -> str:
    """
    "Age Group" -> "ageGroup"
    """
    words = normalize_string(s).split()
    if not words:
        return ""
    return words[0].lower() + "".join(w.capitalize() for w in words[1:])

def to_pascal_case(s: str) -> str:
    """
    "Age Group" -> "AgeGroup"
    """
    words = normalize_string(s).split()
    return "".join(w.capitalize() for w in words)

def to_snake_case(s: str) -> str:
    """
    "Age Group" -> "age_group"
    """
    words = normalize_string(s).split()
    return "_".join(w.lower() for w in words)

def to_kebab_case(s: str) -> str:
    """
    "Age Group" -> "age-group"
    """
    words = normalize_string(s).split()
    return "-".join(w.lower() for w in words)

def to_constant_case(s: str) -> str:
    """
    "Age Group" -> "AGE_GROUP"
    """
    words = normalize_string(s).split()
    return "_".join(w.upper() for w in words)

def to_dot_case(s: str) -> str:
    """
    "Age Group" -> "age.group"
    """
    words = normalize_string(s).split()
    return ".".join(w.lower() for w in words)

def to_path_case(s: str) -> str:
    """
    "Age Group" -> "age/group"
    """
    words = normalize_string(s).split()
    return "/".join(w.lower() for w in words)

def to_sentence_case(s: str) -> str:
    """
    "Age Group" -> "Age group"
    """
    words = normalize_string(s).split()
    if not words:
        return ""
    return words[0].capitalize() + (" " + " ".join(w.lower() for w in words[1:]) if len(words) > 1 else "")

def to_title_case(s: str) -> str:
    """
    "Age Group" -> "Age Group"
    """
    words = normalize_string(s).split()
    return " ".join(w.capitalize() for w in words)

def to_header_case(s: str) -> str:
    """
    "Age Group" -> "Age-Group"
    """
    words = normalize_string(s).split()
    return "-".join(w.capitalize() for w in words)

def to_mocking_case(s: str) -> str:
    """
    "Age Group" -> "aGe GrOuP"
    """
    raw = normalize_string(s)
    out = []
    i = 0
    for ch in raw:
        if ch.isspace():
            out.append(ch)
            continue
        out.append(ch.lower() if i % 2 == 0 else ch.upper())
        i += 1
    return "".join(out)

def convert_cases(s: str) -> dict:
    """
    Convert a given string into many different case styles.
    """
    return {
        "lowercase": normalize_string(s).lower(),
        "uppercase": normalize_string(s).upper(),
        "camelcase": to_camel_case(s),
        "pascalcase": to_pascal_case(s),
        "snakecase": to_snake_case(s),
        "kebabcase": to_kebab_case(s),
        "constantcase": to_constant_case(s),
        "dotcase": to_dot_case(s),
        "pathcase": to_path_case(s),
        "sentencecase": to_sentence_case(s),
        "titlecase": to_title_case(s),
        "headercase": to_header_case(s),
        "mockingcase": to_mocking_case(s),
        # Aliases for certain case libraries:
        "capitalcase": to_pascal_case(s),
        "paramcase": to_kebab_case(s),
        "nocase": normalize_string(s).lower()
    }
