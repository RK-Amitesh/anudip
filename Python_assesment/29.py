# Q29. Create a DataFrame containing student marks
# in multiple subjects. Calculate total marks,
# percentage, and assign grades using apply() function.

import pandas as pd

# creating dataframe
data = {
    "Name": ["Amit", "Rahul", "Riya"],
    "Maths": [85, 70, 92],
    "Science": [90, 75, 88],
    "English": [80, 65, 95]
}

df = pd.DataFrame(data)

# calculating total marks
df["Total"] = (
    df["Maths"] +
    df["Science"] +
    df["English"]
)

# calculating percentage
df["Percentage"] = df["Total"] / 3

# grade function
def grade(per):

    if per >= 90:
        return "A"

    elif per >= 75:
        return "B"

    elif per >= 50:
        return "C"

    else:
        return "Fail"

# applying grade function
df["Grade"] = df["Percentage"].apply(grade)

print(df)