''' account view '''
import time
import json
import datetime
from view import router, BaseHandler, SecureHandler, get_post_json
from playhouse.shortcuts import model_to_dict
from peewee import DoesNotExist

from model.account import Account
from model.account_ask import AccountAsk
from config import RESP

@router('/accounts')
class AccountsHandler(BaseHandler):
    def get(self):
        account_list = []

        accounts = Account.get_all()
        if accounts:
            for account in accounts:
                account_dict = model_to_dict(account)
                account_dict['edit_time'] = float(time.mktime(account_dict['edit_time'].timetuple()))
                account_dict['asks'] = []
                account_asks = AccountAsk.get_by_account(account)
                if account_asks:
                    for account_ask in account_asks:
                        account_dict['asks'].append(model_to_dict(account_ask, exclude=[AccountAsk.account]))
                
                account_list.append(account_dict)
        return self.finish(
            {'code': RESP['SUCCESS']['CODE'], 'data': account_list, 'msg': RESP['SUCCESS']['MSG']}
            )

    def post(self):
        return self.finish({'code': RESP['FORBID'], 'msg': RESP['FORBID']['MSG']})

@router('/account/add')
class AccountAddHandler(BaseHandler):
    def get(self):
        return self.finish({'code': RESP['FORBID'], 'msg': RESP['FORBID']['MSG']})

    def post(self):
        request = get_post_json(self.request)
        if (not request):
            return self.finish(
                {'code': RESP['ERROR']['CODE'], 'msg': RESP['ERROR']['MSG']}
                )

        account = Account.new(request)
        if not account:
            return self.finish(
                {'code': RESP['REPEAT']['CODE'], 'msg': RESP['REPEAT']['MSG']}
                )

        for ask in request['asks']:
            ask['account'] = account
            AccountAsk.new(ask)
        return self.finish(
            {'code': RESP['SUCCESS']['CODE'], 'msg': RESP['SUCCESS']['MSG']}
            )

    def options(self):
        return self.finish(
            {'code': RESP['SUCCESS']['CODE'], 'msg': RESP['SUCCESS']['MSG']}
            )

@router('/account/edit')
class AccountAddHandler(BaseHandler):
    def get(self):
        return self.finish({'code': RESP['FORBID'], 'msg': RESP['FORBID']['MSG']})

    def post(self):
        request = get_post_json(self.request)
        if (not request):
            return self.finish(
                {'code': RESP['ERROR']['CODE'], 'msg': RESP['ERROR']['MSG']}
                )
        account = Account.get_by_pk(request['id'])
        account.edit(request)
        old_asks = AccountAsk.get_by_account(account)

        update_asks_id = []
        times = 0
        for new_ask in request['asks']:
            try:
                account_ask = AccountAsk.get_by_ask(account, new_ask['ask'])
                account_ask.edit(new_ask)
                update_asks_id.append(new_ask['id'])
            except DoesNotExist:
                new_ask['account'] = account
                pass_ask = AccountAsk.new(new_ask)
                update_asks_id.append(pass_ask.id)
        for old_ask in old_asks:
            if not old_ask.id in update_asks_id:
                old_ask.remove()

        return self.finish(
            {'code': RESP['SUCCESS']['CODE'], 'msg': RESP['SUCCESS']['MSG']}
            )
    def options(self):
        return self.finish(
            {'code': RESP['SUCCESS']['CODE'], 'msg': RESP['SUCCESS']['MSG']}
            )

@router('/account/delete')
class AccountDeleteHandler(BaseHandler):
    def get(self):
        account_id = self.get_argument('id', '')
        account = Account.get_by_pk(account_id)
        if not account:
            return self.finish(
                {'code': RESP['ERROR']['CODE'], 'msg': RESP['ERROR']['MSG']}
                )
        AccountAsk.remove_by_account(account)
        account.remove()
        return self.finish(
            {'code': RESP['SUCCESS']['CODE'], 'msg': RESP['SUCCESS']['MSG']}
            )

    def post(self):
        request = get_post_json(self.request)
        if (not request):
            return self.finish(
                {'code': RESP['FORBID']['CODE'], 'msg': RESP['FORBID']['MSG']}
                )
        new_account = Account.new(request)
        for ask in request['asks']:
            ask['account'] = new_account
            AccountAsk.new(ask)

    def options(self):
        return self.finish({'code': RESP['FORBID'], 'msg': RESP['FORBID']['MSG']})
