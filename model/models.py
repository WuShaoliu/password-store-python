''' Initialize database, such as tables, data '''
import peewee

from model import db

from model.account import Account
from model.account_ask import AccountAsk


try:
    db.create_tables([
        Account,
        AccountAsk
    ])
except peewee.OperationalError as event:
    print('OperationalError', event)
    pass
except peewee.ProgrammingError as event:
    # 错误:  关系 "bloglabels" 已经存在
    pass
