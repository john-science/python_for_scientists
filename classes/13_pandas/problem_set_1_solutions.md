# Data Analysis with Pandas - Solutions


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

12. df.loc[df.HAIR_COLOR=='red', 'HAIR_COLOR'] = "ginger"


#### Complex Queries

13. df[(df.AGE>30) & (df.GENDER=='F')]

    df.loc[(df.AGE>30) & (df.GENDER=='F'), :]

14. df[(df.AGE>30) & (df.GENDER=='F')][['HAIR_COLOR','EYE_COLOR']]

    df.loc[(df.AGE>30) & (df.GENDER=='F'), ['HAIR_COLOR','EYE_COLOR']]

15. df.loc[(df.GENDER=='F') & (df.AGE>25), ['HAIR_COLOR','EYE_COLOR']].drop_duplicates()

    df[(df.GENDER=='F') & (df.AGE>25)][['HAIR_COLOR','EYE_COLOR']].drop_duplicates()


#### Additional Dataframe Operations

16. df = pd.read_csv("client_list.csv")

    df.columns = [x.upper() for x in df.columns]
   
    ids = pd.read_csv("customer_id_list.csv")
    
    clients = pd.merge(left=df, right=ids, how='left', on=['LAST_NAME','FIRST_NAME','GENDER','AGE'])

17. sales = pd.read_csv("purchase_log.csv")

    detailed_sales = pd.merge(left=clients, right=sales, how='inner', on=['CUSTOMER_ID'])

18. spenders = detailed_sales.groupby(['CUSTOMER_ID','FIRST_NAME','LAST_NAME','GENDER','AGE'], as_index=False)['PRICE'].sum()

    spenders[spenders.PRICE==spenders.PRICE.max()]

19. top_spender_id = spenders[spenders.PRICE==spenders.PRICE.max()].reset_index(drop=True).loc[0,'CUSTOMER_ID']

    sales.loc[sales.CUSTOMER_ID==top_spender_id, 'ITEM_DESCRIPTION']

#### Writing Files

20. detailed_sales.to_csv("df_out.csv", index=False)

21. detailed_sales.to_pickle("df_out.p")
