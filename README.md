# Flexkey

🎉 **Simplify your DataFrame workflows with effortless column access!** 🎉
Do you ever find yourself frustrated by mismatched column names in Pandas? Say goodbye to tedious renaming or case-sensitive headaches. With **Flexkey**, you can access your columns no matter how they’re written—quick, easy, and stress-free!

---

## Why You'll Love It ❤️

- 🔑 **Flexible Access**: Forget exact matches—access your columns with any format:
  - `'age group'`
  - `'AGE_GROUP'`
  - `'AgeGroup'`
  - They all work, instantly!
- 🚀 **Save Time & Energy**: Focus on your data insights, not debugging key errors.
- 🛠️ **Works Seamlessly**: Drop it into your existing Pandas workflows without skipping a beat.

---

## How It Works 💡

Just import **Flexkey**, and your column worries are gone:

```python
import pandas as pd
from pandas_key_alias.dataframe import DataFrame

# Your DataFrame, your rules
data = {
    'Age Group': [25, 30, 45],
    'Name': ['Alice', 'Bob', 'Charlie']
}
df = DataFrame(data)

# Flexible access
print(df['age-group'])   # Works!
print(df['AGE_GROUP'])   # Still works!
print(df['AgeGroup'])    # Works like magic!
```

✨ All point to the same column, `'Age Group'`. It’s that simple.

---

## Installation ⚙️

Get started in seconds:

### Install From GitHub

```bash
pip install git+https://github.com/velocitatem/flexkey.git
```

### Or Clone the Repository

```bash
git clone https://github.com/velocitatem/flexkey.git
cd flexkey
pip install .
```

---

## Perfect For:

✔️ Data scientists who want less debugging and more analyzing.
✔️ Analysts managing messy, inconsistent data.
✔️ Anyone who values **productivity** over **painful column mismatches**.

---


> **⚠️ Warning**
> While **Pandas Key Alias** makes column access flexible, always ensure your column names remain unique. Ambiguous names (e.g., multiple columns with the same alias) might lead to unexpected results.
>
> If you encounter issues, check your column headers or open an issue on GitHub for assistance!

## Ready to Try It?

### 🏗️ Getting Set Up

1. **Clone the repo**:
   ```bash
   git clone https://github.com/velocitatem/flexkey.git
   cd flexkey
   ```

2. **Install locally**:
   ```bash
   pip install .
   ```

3. **Start using today**!

---

## Why Flexkey?

We built **Flexkey** to make your life easier. Whether you're cleaning data, building dashboards, or crunching numbers, this tool saves you time and lets you focus on what really matters: **delivering results**.

---

## Support & Feedback 💬

We’d love to hear from you! Found a bug? Have a feature request? Contact us or open an issue on GitHub.
Install it today and make messy column names a thing of the past!
