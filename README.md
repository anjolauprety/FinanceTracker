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
