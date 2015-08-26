# Data Analysis with Pandas - Problem Set

#### Reading in Data

1. df1 = pd.read_csv("client_list.csv")
2. df2 = pd.read_csv("client_list.table", sep=';')
3. df3 = pd.read_fwf("client_list.txt")
4. pd.read_csv("client_list.csv", skiprows=3, header=None)

5. df = pd.read_csv("client_list.csv")
   df.columns = [x.upper() for x in df.columns]
   
6. pd.read_csv("client_list_practice.csv", usecols=["FIRST_NAME","AGE","EYE_COLOR"])

#### Slicing a Data Set

7. df[4:11]
   df.loc[4:10, :]

8. df[['LAST_NAME','AGE','HAIR_COLOR']]
   df.loc[:, ['LAST_NAME','AGE','HAIR_COLOR']]

9. df[4:11][['LAST_NAME','AGE','HAIR_COLOR']]
   df.loc[4:10, ['LAST_NAME','AGE','HAIR_COLOR']]

#### Simple Queries

10. df[df.LAST_NAME=='Smith']
    df.loc[df.LAST_NAME=='Smith', :]

11. df.loc[df.HAIR_COLOR!='black',:]
    df.loc[~(df.HAIR_COLOR=='black'), :]
    df[df.HAIR_COLOR!='black']
    df[~(df.HAIR_COLOR=='black')]

#### Complex Queries
