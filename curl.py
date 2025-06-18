
class MainUrl:
    main_site = 'https://stellarburgers.nomoreparties.site'
    api_base = f'{main_site}/api'
    login = f'{main_site}/login'
    account_profile = f'{main_site}/account/profile'
    auth_register = f"{main_site}/api/auth/register"
    auth_login = f"{main_site}/api/auth/login"


class Endpoints:

    CREATE_USER = f'{MainUrl.api_base}/auth/register'
    LOGIN = f'{MainUrl.api_base}/auth/login'
    DELETE_USER = f'{MainUrl.api_base}/auth/user'
    CREATE_ORDER = f'{MainUrl.api_base}/orders'
    GET_ORDERS = f'{MainUrl.api_base}/orders'

