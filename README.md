# pa02-team10
Script started on Thu Mar 24 21:17:44 2022
[?1034hbash-3.2$ pylint r[Ktrcker[K[K[K[Kacker.py
************* Module tracker
tracker.py:62:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:62:0: R0912: Too many branches (13/12) (too-many-branches)
tracker.py:62:0: R0915: Too many statements (57/50) (too-many-statements)
tracker.py:143:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:148:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:152:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:156:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)

------------------------------------------------------------------
Your code has been rated at 9.20/10 (previous run: 9.20/10, +0.00)

bash-3.2$ pylint transactions.y[Kpy

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

bash-3.2$ pytest test_category.py
[1m=========================================================== test session starts ===========================================================[0m
platform darwin -- Python 3.9.7, pytest-7.1.1, pluggy-1.0.0
rootdir: /Users/kaysmith/Documents/GitHub/pa02-team10, configfile: pytest.ini
plugins: anyio-3.5.0
[1mcollecting ... [0m[1m
collected 4 items                                                                                                                         [0m

test_category.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                                                                               [100%][0m

[32m============================================================ [32m[1m4 passed[0m[32m in 0.28s[0m[32m ============================================================[0m
bash-3.2$ pytest test_transaction.pt[Ky
[1m=========================================================== test session starts ===========================================================[0m
platform darwin -- Python 3.9.7, pytest-7.1.1, pluggy-1.0.0
rootdir: /Users/kaysmith/Documents/GitHub/pa02-team10, configfile: pytest.ini
plugins: anyio-3.5.0
[1mcollecting ... [0m[1m
collected 4 items                                                                                                                         [0m

test_transaction.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                                                                            [100%][0m

[32m============================================================ [32m[1m4 passed[0m[32m in 0.15s[0m[32m ============================================================[0m
bash-3.2$ exit 
exit

Script done on Thu Mar 24 21:18:26 2022

Script started on Thu Mar 24 22:03:45 2022
bash-3.2$ python3 tracker.py

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this MENU

> 1
id  name4      description                   
---------------------------------------------
1   3          4                             
2   testing category hello                         
3   testing    hello                         
4   team10     github                        
5   pa02       hello                         
6                                            
8   hey        hello                         
9   hey        hello                         
> 2
category name: tim      
category description: hickey
> 3
modifying category
rowid: 10
new category name: HICKEY
new category description: TIM       
> 1
id  name4      description                   
---------------------------------------------
1   3          4                             
2   testing category hello                         
3   testing    hello                         
4   team10     github                        
5   pa02       hello                         
6                                            
8   hey        hello                         
9   hey        hello                         
10  HICKEY     TIM                           
> 4


item # amount     category   date       description                   
----------------------------------------
item # 300        hello      3          test                          
item # 300        hello      3          hello                         
item # 300        testing    3          hello                         
item # 300        hello      3          hello                         
item # 500        pa02       4          adder                         
item # 3000       hi1        3          um                            
item # 600        nice       3          nice nice                     
item # 400        4          4          4                             
item # 400        new money  5          some mula                     
item # 300        hello      3032022    na                            
item # 30         heyyy      3032022    na                            
item # 300        hello      3032022    na                            
> 5
add transaction
amount: 623
transaction category: tim      
transaction day: 05302021
new transaction description: hickey
> 4


item # amount     category   date       description                   
----------------------------------------
item # 300        hello      3          test                          
item # 300        hello      3          hello                         
item # 300        testing    3          hello                         
item # 300        hello      3          hello                         
item # 500        pa02       4          adder                         
item # 3000       hi1        3          um                            
item # 600        nice       3          nice nice                     
item # 400        4          4          4                             
item # 400        new money  5          some mula                     
item # 300        hello      3032022    na                            
item # 30         heyyy      3032022    na                            
item # 300        hello      3032022    na                            
item # 623        tim        5302021    hickey                        
> 6
delete transaction
rowid: 4
Traceback (most recent call last):
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 166, in <module>
    toplevel()
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 130, in toplevel
    choice = process_choice(choice)
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 93, in process_choice
    tra = {'amount':amount, 'category':tracat, 'date':date, 'desc':desc}
UnboundLocalError: local variable 'amount' referenced before assignment
bash-3.2$  /usr/bin/env /usr/local/bin/python3 /Users/kaysmith/.vscode/extensioniles/lib/ppython3 tracker.py

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this MENU

> 7
summarize transactions by date
Traceback (most recent call last):
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 166, in <module>
    toplevel()
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 130, in toplevel
    choice = process_choice(choice)
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 97, in process_choice
    tras = transaction.sort_date()
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/transactions.py", line 78, in sort_date
    return to_tra_dict_list(tuples)
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/transactions.py", line 14, in to_tra_dict_list
    return [to_tra_dict(tra) for tra in tra_tuples]
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/transactions.py", line 14, in <listcomp>
    return [to_tra_dict(tra) for tra in tra_tuples]
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/transactions.py", line 8, in to_tra_dict
    'category': tra_tuple[2], 'date': tra_tuple[3], 'desc': tra_tuple[4]}
IndexError: tuple index out of range
bash-3.2$ python3 tracker.py

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this MENU

> 8
summarize transactions by month
rowid: 5
category name: hey
category description: hello
> 9
summarize transactions by year
Traceback (most recent call last):
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 166, in <module>
    toplevel()
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 130, in toplevel
    choice = process_choice(choice)
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 108, in process_choice
    tras = transaction.sort_year()
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/transactions.py", line 84, in sort_year
    cur.execute("SELECT * from transactions ORDER BY year")
sqlite3.OperationalError: no such column: year
bash-3.2$ python3 tracker.py

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this MENU

> 9
summarize transactions by year
Traceback (most recent call last):
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 166, in <module>
    toplevel()
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 130, in toplevel
    choice = process_choice(choice)
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 108, in process_choice
    tras = transaction.sort_year()
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/transactions.py", line 84, in sort_year
    cur.execute("SELECT * from transactions ORDER BY year")
sqlite3.OperationalError: no such column: year
bash-3.2$ python3 tracker.py

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this MENU

> 10
summarize transactions by category
Traceback (most recent call last):
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 166, in <module>
    toplevel()
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 130, in toplevel
    choice = process_choice(choice)
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/tracker.py", line 112, in process_choice
    tras = transaction.sort_category()
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/transactions.py", line 68, in sort_category
    return to_tra_dict_list(tuples)
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/transactions.py", line 14, in to_tra_dict_list
    return [to_tra_dict(tra) for tra in tra_tuples]
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/transactions.py", line 14, in <listcomp>
    return [to_tra_dict(tra) for tra in tra_tuples]
  File "/Users/kaysmith/Documents/GitHub/pa02-team10/transactions.py", line 8, in to_tra_dict
    'category': tra_tuple[2], 'date': tra_tuple[3], 'desc': tra_tuple[4]}
IndexError: tuple index out of range
bash-3.2$ python3 tracker.py

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this MENU

> 11

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this MENU

> 0
bye
bash-3.2$ 
bash-3.2$ exit
exit

Script done on Thu Mar 24 22:06:32 2022
(base) MacBookPro:pa02-team10 kaysmith$ 

