'''website config'''
PORT = 8000
XSRF_COOKIES = False
COOKIE_SECRET = 'bZJc2sWbSLKos6GkHn/VB9oXwWt8S0L0kRvJ5/xJ89E='
COOKIE_USER = 'user'
DEBUG = True

DATABASE_URI = 'sqlite:///./dist/database.db'
# DATABASE_URI = 'mysql://root:123456@localhost:3306/database'
# DATABASE_URI = 'postgresext://postgres:123456@localhost:5432/database'

OPRIGIN_ADDRESS = 'http://localhost:8080'


RESP = {
    'SUCCESS': {
        'CODE': 0,
        'MSG': '请求成功'
    },
    'FORBID': {
        'CODE': -10,
        'MSG': '非法请求'
    },
    'ERROR': {
        'CODE': -20,
        'MSG': '错误请求'
    },
    'OUTLIMIT': {
        'CODE': -30,
        'MSG': '请求数据超出范围'
    },
    'REPEAT': {
        'CODE': -40,
        'MSG': '数据重复'
    },
}
