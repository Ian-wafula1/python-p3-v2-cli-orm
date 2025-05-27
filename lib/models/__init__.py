import sqlite3
# from department import *
# from employee import *

import department
import employee

all = ['Department', 'Employee']

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()
