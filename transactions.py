import sqlite3

def to_tra_dict(tra_tuple):
    ''' tra is a transation tuple (item #, amount, category, date, desc)'''
    tra = {'item #':tra_tuple[0], 'amount':tra_tuple[1], 'category':tra_tuple[2], 'date':tra_tuple[3], 'desc': tra_tuple[4]}
    return tra

def to_tra_dict_list(tra_tuples):
    ''' convert a list of transation tuples into a list of dictionaries'''
    return [to_tra_dict(tra) for tra in tra_tuples]

class Transaction():
    ''' Transaction represents a table of transactions'''

    def __init__(self,dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (amount text, category text, date text, desc text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT 'item #',* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tra_dict_list(tuples)

    def select_one(self,itemnum):
        ''' return a transaction with a specified itemnum '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT 'item #',* from transactions where 'item #'=(?)",(itemnum,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tra_dict(tuples[0])


    def sort_date(self):
        ''' return all transactions sorted by date '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * from transactions ORDER BY date")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tra_dict_list(tuples)
    
    def sort_year(self):
        ''' return all transactions sorted by year '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * from transactions ORDER BY year")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tra_dict_list(tuples)

    def add(self,transact):
        ''' add a transaction to the transactions table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?)",(transact['item #'],transact['amount'],transact['category'],transact['date'],transact['desc']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def update(self,itemnum,transact):
        ''' update a transaction to the transactions table.
            this returns the itemnum of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''UPDATE transactions
                        SET amount=(?), category=(?), date=(?), desc=(?)
                        WHERE 'item #'=(?);
        ''',(transact['amount'],transact['category'],transact['date'],transact['desc'],itemnum))
        con.commit()
        con.close()

    def delete(self,itemnum):
        ''' delete a transaction to the transactions table.
            this returns the itemnum of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE 'item #'=(?);
        ''',(itemnum,))
        con.commit()
        con.close()
