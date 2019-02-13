# Data Analysis with Pandas - Solutions


#### Reading in Data

1.Read in the comma-separated file "client_list.csv". Assign as variable `df1`.

```python
df1 = pd.read_csv("client_list.csv")
```

2. Read in the delimted file "client_list.table". Assign as variable as `df2`.

```python
df2 = pd.read_csv("client_list.table", sep=';')
```

3. Read in the fixed-width file "client_list.txt". Assign as variable `df3`

```python
df3 = pd.read_fwf("client_list.txt")
```

4. Read in the comma-separated file "client_list.csv", skip the first 3 rows, and ignore the header. Do not assign to variable (just return a view).

```python
pd.read_csv("client_list.csv", skiprows=3, header=None)
```

5. Read in the comma-separated file "client_list.csv". Set the column headers in all caps. Assign as variable `df`.

```python
df = pd.read_csv("client_list.csv")
df.columns = [x.upper() for x in df.columns]
```

6. Read in the comma-separated file "client_list_practice.csv" and only extract the columns `["FIRST_NAME","AGE","EYE_COLOR"]`. Do not assign to a variable.

```python
d.read_csv("client_list_practice.csv", usecols=["FIRST_NAME","AGE","EYE_COLOR"])
```


#### Slicing a Data Set

7. Slice rows 5 through 11 of `df`. Can you provide two ways of doing this?

```python
df[4:11]
df.loc[4:10, :]
```

8. Return only the columns ['LAST_NAME','AGE','HAIR_COLOR'] for `df`. Can you provide two ways of doing this?

```python
df[['LAST_NAME','AGE','HAIR_COLOR']]
df.loc[:, ['LAST_NAME','AGE','HAIR_COLOR']]
```

9. Combine problems 7 and 8: return rows 5 though 11 and columns  ['LAST_NAME','AGE','HAIR_COLOR'] for `df`. Can you provide two ways of doing this?

```python
df[4:11][['LAST_NAME','AGE','HAIR_COLOR']]
df.loc[4:10, ['LAST_NAME','AGE','HAIR_COLOR']]
```


#### Simple Queries

10. Find the subset of `df` where the client's last name is "Smith".

```python

df[df.LAST_NAME=='Smith']
df.loc[df.LAST_NAME=='Smith', :]
```

11. Find the subset of `df` where the client's hair color is not black.

```python
df.loc[df.HAIR_COLOR!='black',:]
df.loc[~(df.HAIR_COLOR=='black'), :]
df[df.HAIR_COLOR!='black']
df[~(df.HAIR_COLOR=='black')]
```

12. Find the subset of `df` where the client's hair color is red and reset the values to "ginger".

```python
df.loc[df.HAIR_COLOR=='red', 'HAIR_COLOR'] = "ginger"
```


#### Complex Queries


13. Find the subset of `df` where the clients are females older than 30 years.

```python
df[(df.AGE>30) & (df.GENDER=='F')]
df.loc[(df.AGE>30) & (df.GENDER=='F'), :]
```

14. Repeat problem 13, but return only the hair color and eye color.

```python
df[(df.AGE>30) & (df.GENDER=='F')][['HAIR_COLOR','EYE_COLOR']]
df.loc[(df.AGE>30) & (df.GENDER=='F'), ['HAIR_COLOR','EYE_COLOR']]
```

15. Find the unique combination of hair and eye color for women older than 25 years.

```python
df.loc[(df.GENDER=='F') & (df.AGE>25), ['HAIR_COLOR','EYE_COLOR']].drop_duplicates()
df[(df.GENDER=='F') & (df.AGE>25)][['HAIR_COLOR','EYE_COLOR']].drop_duplicates()
```


#### Additional Dataframe Operations


16. Perform a `merge` using "client_list.csv" and "customer_id_list.csv". Assign the resulting dataframe as `clients`.

```python
df = pd.read_csv("client_list.csv")
df.columns = [x.upper() for x in df.columns]
ids = pd.read_csv("customer_id_list.csv")
clients = pd.merge(left=df, right=ids, how='left', on=['LAST_NAME','FIRST_NAME','GENDER','AGE'])
```

17. Perform a `merge` using `clients` and "purchase_log.csv" and limit the subset to only clients who made purchases. Assign the resulting dataframe as `detailed_sales`.

```python
sales = pd.read_csv("purchase_log.csv")
detailed_sales = pd.merge(left=clients, right=sales, how='inner', on=['CUSTOMER_ID'])
```

18. Use `groupby` to find the client who spent the most money on purchases. Determine how much he/she spent. HINT: save the intermediate dataframe from using `groupby` as `spenders` before applying slicing to determine the client who spent the most money on purchases.

```python
spenders = detailed_sales.groupby(['CUSTOMER_ID','FIRST_NAME','LAST_NAME','GENDER','AGE'], as_index=False)['PRICE'].sum()
spenders[spenders.PRICE==spenders.PRICE.max()]
```

19. (BONUS) Modify the answer to problem 18 slightly to determine exactly what items where purchased by the top spending client.

```python
top_spender_id = spenders[spenders.PRICE==spenders.PRICE.max()].reset_index(drop=True).loc[0,'CUSTOMER_ID']
sales.loc[sales.CUSTOMER_ID==top_spender_id, 'ITEM_DESCRIPTION']
```
    

#### Writing Files

20. Save `detailed_sales` as a csv file named "df_out.csv" with no indices.

```python
detailed_sales.to_csv("df_out.csv", index=False)
```

21. Save `detailed_sales` to a pickle file named "df_out.p"

```python
detailed_sales.to_pickle("df_out.p")
```


[Back to Problem Set](problem_set_1_pandas.md)
