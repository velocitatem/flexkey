import pandas as pd
import re

def normalize_string(s: str) -> str:
    """
    1) Replace all non-alphanumeric (underscore, hyphen, dot, etc.) with spaces.
    2) Insert a space before an uppercase letter if it follows a lowercase or digit.
    3) Strip the result.

    Examples:
      "age-group" -> "age group"
      "AGE_GROUP" -> "AGE GROUP"
      "AgeGroup"  -> "Age Group"
      "PDFBox"    -> "P D F Box"
    """
    # 1) Turn underscores, hyphens, etc. into spaces
    s = re.sub(r'[^a-zA-Z0-9]+', ' ', s)
    # 2) Insert space before uppercase letter that follows a lowercase or digit
    s = re.sub(r'(?<=[a-z0-9])([A-Z])', r' \1', s)
    # 3) Trim
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
        # Aliases for certain libraries
        "capitalcase": to_pascal_case(s),  # same as pascal
        "paramcase": to_kebab_case(s),     # same as kebab
        "nocase": normalize_string(s).lower()
    }

class DataFrame(pd.DataFrame):
    """
    Extension that attempts to unify variations of the key (column name)
    so that "AGE_GROUP", "age-group", etc. map to "Age Group".
    """
    def __getitem__(self, key):
        # 1) Try exact name first
        try:
            return super().__getitem__(key)
        except KeyError:
            pass

        # 2) Generate all variants for the given key
        variants = convert_cases(str(key))

        # 3) Check if any variant is a direct match in self.columns
        for variant in variants.values():
            if variant in self.columns:
                return super().__getitem__(variant)

        # 4) If no match, raise the normal KeyError
        raise KeyError(
            f"Column '{key}' (or any recognized variant) not found in columns {list(self.columns)} "
            f"but tried {list(variants.values())}"
        )

def test():
    data = {
        'Age Group': [1, 2, 3],
        'Name': ['Alice', 'Bob', 'Charlie']
    }
    df = DataFrame(data)

    inputs = [
        'Age Group',    # exact
        'age group',    # all lowercase w/ space
        'age-group',    # kebab
        'age_group',    # snake
        'AGE_GROUP',    # constant
    ]

    for inp in inputs:
        result = df[inp]
        print(f"df[{inp!r}] -> {list(result)}")
    # All should produce [1, 2, 3]

    # If you also want to see how 'age.group' etc. behave, try them:
    # More test variants: 'age.group', 'AgeGroup', 'ageGroup', 'aGeGrOuP'
    # or anything else you want to unify.

if __name__ == '__main__':
    test()
