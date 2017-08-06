''' database model '''
import peewee
import time
import config
from playhouse.db_url import connect

db = connect(config.DATABASE_URI, autocommit=True, autorollback=True)

class BaseModel(peewee.Model):
    class Meta:
        database = db

    @classmethod
    def get_by_pk(cls, value):
        try:
            return cls.get(cls._meta.primary_key == value)
        except cls.DoesNotExist:
            return

    @classmethod
    def get_all(cls):
        select_all = cls.select()
        if select_all.count() > 0:
            return select_all
        else:
            return

    @classmethod
    def exists_by_pk(cls, value):
        return cls.select().where(cls._meta.primary_key == value).exists()

    def remove(self):
        self.delete_instance()
