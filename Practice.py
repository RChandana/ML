# Pandas Basics
import pandas as pd
pd.DataFrame({'Yes' : [12, 23], 'No' : [54, 65]}, index = ['Person 1', 'Person 2'])


# Series Basics
import pandas as pd
list = pd.Series([1, 2, 3, 4], index = ['stu1', 'stu2', 'stu3', 'stu4'], name = 'Student')
print(list)
