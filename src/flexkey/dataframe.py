import pandas as pd
from .transformations import convert_cases

class DataFrame(pd.DataFrame):
    """
    Extension of pandas DataFrame that tries to unify variations
    in column key so that columns can be accessed with flexible naming.
    """
    def __getitem__(self, key):
        # 1) Try exact name
        try:
            return super().__getitem__(key)
        except KeyError:
            pass

        # 2) Generate variants
        variants = convert_cases(str(key))

        # 3) If any variant matches a column, return it
        for variant in variants.values():
            if variant in self.columns:
                return super().__getitem__(variant)

        # 4) Otherwise fail
        raise KeyError(
            f"Column '{key}' (or any recognized variant) not found in columns {list(self.columns)} "
            f"but tried {list(variants.values())}"
        )
