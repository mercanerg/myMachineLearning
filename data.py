import main as mn
data = mn.data
print(data.head())
print('\nrows > ',data.shape[0], ' column > ', data.shape[1])

# Data info; row numbers, column name, null or non-null, Dtype and memory usage
print(data.info())
print(data.isnull()) # if data is null, return True else False

# sum null-data
print(data.isnull().sum())

# detecting data structures
print('\n', data.dtypes)
print('\n', data.describe())
print('\n', data.describe().T)
print(data['sex'])
print('\n', mn.smoke_data)
print("\n columns > ", data.columns)

