# Data Analysis with Pandas - Problem Set

**I recommend doing these problems in a Jupyter notebook.**


#### Reading in Data

1. Read in the comma-separated file "client_list.csv". Assign as variable `df1`.
2. Read in the delimted file "client_list.table". Assign as variable as `df2`.
3. Read in the fixed-width file "client_list.txt". Assign as variable `df3`
4. Read in the comma-separated file "client_list.csv", skip the first 3 rows, and ignore the header. Do not assign to variable (just return a view).
5. Read in the comma-separated file "client_list.csv". Set the column headers in all caps. Assign as variable `df`.
6. Read in the comma-separated file "client_list_practice.csv" and only extract the columns ["FIRST_NAME","AGE","EYE_COLOR"]. Do not assign to a variable.


#### Slicing a Data Set

7. Slice rows 5 through 11 of `df`. Can you provide two ways of doing this?
8. Return only the columns ['LAST_NAME','AGE','HAIR_COLOR'] for `df`. Can you provide two ways of doing this?
9. Combine problems 7 and 8: return rows 5 though 11 and columns  ['LAST_NAME','AGE','HAIR_COLOR'] for `df`. Can you provide two ways of doing this?


#### Simple Queries

10. Find the subset of `df` where the client's last name is "Smith".
11. Find the subset of `df` where the client's hair color is not black.
12. Find the subset of `df` where the client's hair color is red and reset the values to "ginger".


#### Complex Queries

13. Find the subset of `df` where the clients are females older than 30 years.
14. Repeat problem 13, but return only the hair color and eye color.
15. Find the unique combination of hair and eye color for women older than 25 years.


#### Additional Dataframe Operations

16. Perform a `merge` using "client_list.csv" and "customer_id_list.csv". Assign the resulting dataframe as `clients`.
17. Perform a `merge` using `clients` and "purchase_log.csv" and limit the subset to only clients who made purchases. Assign the resulting dataframe as `detailed_sales`.
18. Use `groupby` to find the client who spent the most money on purchases. Determine how much he/she spent. HINT: save the intermediate dataframe from using `groupby` as `spenders` before applying slicing to determine the client who spent the most money on purchases.
19. (BONUS) Modify the answer to problem 18 slightly to determine exactly what items where purchased by the top spending client.

#### Writing Files

20. Save `detailed_sales` as a csv file named "df_out.csv" with no indices.
21. Save `detailed_sales` to a pickle file named "df_out.p"

## Solutions

 * [Solutions](problem_set_1_solutions.md)

[Back to Lecture](lecture_13.md)
