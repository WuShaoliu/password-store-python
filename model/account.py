''' accounts object '''
import model
from peewee import *
import time

class Account(model.BaseModel):
    ''' account object '''
    email = CharField(128, null=True)
    phone = CharField(20, null=True)
    username = CharField(40, null=False)
    password = CharField(40, null=False)
    website = CharField(512, null=False)
    remarks = CharField(512, null=True)
    edit_time = TimestampField(null=True)

    class Meta:
        db_table = 'accounts'

    @classmethod
    def new(cls, data):
        ''' add this username and account '''
        if cls.select().where((cls.username == data['username']) & (cls.website == data['website'])).exists():
            return None
        return cls.create(
            website=data['website'],
            username=data['username'],
            password=data['password'],
            email=data['email'],
            phone=data['phone'],
            remarks=data['remarks'],
            edit_time=time.time()
        )

    @classmethod
    def search(cls, keyword):
        return cls.select().where((keyword << cls.email) | (keyword << cls.username) | (keyword << cls.website))

    # @classmethod
    # def get_by_user(cls, user):
    #     return

    def edit(self, data):
        ''' edit account information '''
        Account.update(
            email=data['email'],
            phone=data['phone'],
            username=data['username'],
            password=data['password'],
            website=data['website'],
            remarks=data['remarks'],
            edit_time=time.time()
        ).where(Account._meta.primary_key == self.id).execute()

