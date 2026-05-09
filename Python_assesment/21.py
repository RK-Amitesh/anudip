# Q21. Generate a NumPy array of student marks
# and convert it into a Pandas DataFrame.
# Display highest marks, average marks,
# and subject-wise statistics.

import numpy as np
import pandas as pd

# creating numpy array
marks = np.array([
    [85, 90, 78],
    [88, 76, 95],
    [70, 80, 89]
])

# converting into dataframe
data = pd.DataFrame(
    marks,
    columns=["Maths", "Science", "English"]
)

print("Student Marks Data :\n")
print(data)

# highest marks
print("\nHighest Marks :")
print(data.max())

# average marks
print("\nAverage Marks :")
print(data.mean())

# subject-wise statistics
print("\nSubject-wise Statistics :")
print(data.describe())