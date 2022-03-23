import sqlite3

def to_tra_dict(tra_tuple):
    ''' tra is a transation tuple (item #, amount, cat, date, desc)'''
    tra = {'item #':tra_tuple[0], 'amount':tra_tuple[1], 'cat':tra_tuple[2], 'date':tra_tuple[3], 'desc': tra_tuple[4]}
    return tra

def to_tra_dict_list(tra_tuples):
    ''' convert a list of transation tuples into a list of dictionaries'''
    return [to_tra_dict(tra) for tra in tra_tuples]

class Transaction():
    ''' Category represents a table of transactions'''

    def __init__(self,dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (amount text, cat text, date text, desc text)''')
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
        ''' return a category with a specified itemnum '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT 'item #',* from categories where 'item #'=(?)",(itemnum,) )
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tra_dict(tuples[0])


    def add(self,transact):
        ''' add a category to the categories table.
            this returns the rowid of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transations VALUES(?,?)",(transact['amount'],transact['cat'],transact['date'],transact['desc']))
        con.commit()
        cur.execute("SELECT last_insert_itemnum)")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def update(self,itemnum,transact):
        ''' add a category to the transactions table.
            this returns the itemnum of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''UPDATE transactions
                        SET amount=(?), cat=(?), date=(?), desc=(?)
                        WHERE 'item #'=(?);
        ''',(transact['amount'],transact['cat'],transact['date'],transact['desc'],itemnum))
        con.commit()
        con.close()

    def delete(self,itemnum):
        ''' add a category to the transactions table.
            this returns the itemnum of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE 'item #'=(?);
        ''',(itemnum,))
        con.commit()
        con.close()
