'''
test_categories runs unit and integration tests on the category module
'''

import pytest

from transactions import Transaction, to_tra_dict


@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')


@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db


@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    tra1 = {'amount': '1200', 'category': 'home furniture',
            'date': '03/02/2022', 'desc': 'couch and coffee table'}
    tra2 = {'amount': '1400', 'category': 'electronics',
            'date': '03/19/2022', 'desc': 'tv and sound speaker'}
    tra3 = {'amount': '800', 'category': 'dining',
            'date': '03/22/2022', 'desc': 'groceries'}
    id1 = empty_db.add(tra1)
    id2 = empty_db.add(tra2)
    id3 = empty_db.add(tra3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)


@pytest.fixture
def med_db(small_db):
    ''' create a database with 10 more elements than small_db'''
    rowids = []
    # add 10 categories
    for i in range(10):
        s = str(i)
        tra = {'amount': 'amount '+s,
               'category': 'category '+s,
               'date': 'date '+s,
               'desc': 'description '+s,
               }
        rowid = small_db.add(tra)
        rowids.append(rowid)

    yield small_db

    # remove those 10 categories
    for j in range(10):
        small_db.delete(rowids[j])


@pytest.mark.simple
def test_to_tra_dict():
    ''' testing the to_cat_dict function '''
    a = to_tra_dict((7, 'testamount', 'testcategory', 'testdate', 'testdesc'))
    assert a['itemnum'] == 7
    assert a['amount'] == 'testamount'
    assert a['category'] == 'testcategory'
    assert a['date'] == 'testdate'
    assert a['desc'] == 'testdesc'
    assert len(a.keys()) == 5


@pytest.mark.add
def test_add(med_db):
    ''' add a category to db, the select it, then delete it'''

    tra0 = {'amount': 'testing_add',
            'desc': 'see if it works',
            }
    tras0 = med_db.select_all()
    rowid = med_db.add(tra0)
    tras1 = med_db.select_all()
    assert len(tras1) == len(tras0) + 1
    tra1 = med_db.select_one(rowid)
    assert tra1['amount'] == tra0['amount']
    assert tra1['category'] == tra0['category']


@pytest.mark.delete
def test_delete(med_db):
    ''' add a category to db, delete it, and see that the size changes'''
    # first we get the initial table
    tras0 = med_db.select_all()

    # then we add this category to the table and get the new list of rows
    tra0 = {'amount': 'testing_add',
            'desc': 'see if it works',
            }
    rowid = med_db.add(tra0)
    tras1 = med_db.select_all()

    # now we delete the category and again get the new list of rows
    med_db.delete(rowid)
    tras2 = med_db.select_all()

    assert len(tras0) == len(tras2)
    assert len(tras2) == len(tras1)-1


@pytest.mark.update
def test_update(med_db):
    ''' add a category to db, updates it, and see that it changes'''

    # then we add this category to the table and get the new list of rows
    tra0 = {'amount': 'testing_add',
            'desc': 'see if it works',
            }
    rowid = med_db.add(tra0)

    # now we upate the category
    tra1 = {'amount': 'new amount', 'desc': 'new desc'}
    med_db.update(rowid, tra1)

    # now we retrieve the transaction and check that it has changed
    tra2 = med_db.select_one(rowid)
    assert tra2['amount'] == tra1['amount']
    assert tra2['desc'] == tra1['desc']
