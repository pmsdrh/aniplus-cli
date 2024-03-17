import base64
from ui.captcha import Captcha
import requests

from apihelper.basicHelper import Basic


class Login(Basic):
    def __init__(self):
        super(Login, self).__init__()
        self.email = input('Email: ')
        self.password = input('Password: ')
        self.captcha = self.getCaptcha()
        decoded_image = base64.b64decode(self.captcha['captcha']['img'].split(',')[1])
        with open('cache/captcha.png', 'wb') as f:
            f.write(decoded_image)
        self.ui = Captcha('cache/captcha.png', self.setLogin)
        self.ui.main()

    def getCaptcha(self):
        return requests.request("GET", 'https://anips.ir/api/auth/refresh-captcha', headers=self.defaultHeaders,
                                verify=False).json()

    def setLogin(self):
        print('hehe')
        self.ui.destroy()
        options: dict = {"email": self.email, "password": self.password, "captcha": self.ui.value.get(),
                         "captcha_key": self.captcha['captcha']['key']}
        print(self.ui.value.get())
        login: requests = requests.post("https://anips.ir/api/auth/login", headers=self.defaultHeaders, params=options,
                                        verify=False)
        if login.status_code != 200:
            print(login.json())
        else:
            with open('cache/.token.cache') as t:
                token = login.json()['item']['access_token']
                t.write(token)
