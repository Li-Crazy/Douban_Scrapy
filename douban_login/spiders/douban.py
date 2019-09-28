# -*- coding: utf-8 -*-
import scrapy
from urllib import request


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/passport/login']

    def parse_before_login(self, response):
        print("登录前表单填充")
        captcha_id = response.xpath(
            '//input[@name="captcha-id"]/@value').extract_first()
        captcha_image_url = response.xpath(
            '//img[@id="captcha_image"]/@src').extract_first()
        if captcha_image_url is None:
            print(u"登录时无验证码")
            formdata = {
                "redir": "https://movie.douban.com/",
                "source": "movie",
                "form_email": "你的账号",
                # 请填写你的密码
                "form_password": "你的密码",
            }
            print(u"登录中")
            # 提交表单
            return scrapy.FormRequest.from_response(response, meta={
                "cookiejar": response.meta["cookiejar"]},
                                                    headers=self.headers,
                                                    formdata=formdata,
                                                    callback=self.parse_after_login)
        else:
            print("登录时有验证码")
            save_image_path = "D:/image/captcha.jpeg"
            # 将图片验证码下载到本地
            urllib.urlretrieve(captcha_image_url, save_image_path)
            # 打开图片，以便我们识别图中验证码
            try:
                im = Image.open('captcha.jpeg')
                im.show()
            except:
                pass
            # 手动输入验证码
            captcha_solution = raw_input('根据打开的图片输入验证码:')
            formdata = {
                "source": "None",
                "redir": "https://www.douban.com",
                "form_email": "你的账号",
                # 此处请填写密码
                "form_password": "你的密码",
                "captcha-solution": captcha_solution,
                "captcha-id": captcha_id,
                "login": "登录",
            }

        print("登录中")
        # 提交表单
        return scrapy.FormRequest.from_response(response, meta={
            "cookiejar": response.meta["cookiejar"]},
                                                headers=self.headers,
                                                formdata=formdata,
                                                callback=self.parse_after_login)


