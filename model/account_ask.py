''' account ask object '''
import model
from peewee import *
import time
from model.account import Account

class AccountAsk(model.BaseModel):
    ''' account object '''
    account = ForeignKeyField(Account, related_name='account_ask')
    ask = CharField(64, null=False)
    answer = CharField(64, null=False)

    class Meta:
        db_table = 'accountAsk'

    @classmethod
    def new(cls, data):
        ''' add this username and account '''
        return cls.create(
            account=data['account'],
            ask=data['ask'],
            answer=data['answer']
        )

    @classmethod
    def get_by_account(cls, account):
        return cls.select().where(cls.account == account)

    @classmethod
    def remove_by_account(cls, account):
        ''' delete label '''
        cls.delete().where(cls.account == account).execute()

    @classmethod
    def get_by_ask(cls, account, ask):
        return cls.get((cls.account == account) & (cls.ask == ask))

    def edit(self, data):
        ''' edit account information '''
        AccountAsk.update(
            ask=data['ask'],
            answer=data['answer']
        ).where(AccountAsk._meta.primary_key == self.id).execute()

