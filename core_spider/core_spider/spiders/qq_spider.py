import scrapy
import logging
import datetime


logger = logging.getLogger(__name__)


class QuotesSpider(scrapy.Spider):
    name = "core_spider"
    open_id = '?openid=o04IBAEpsIvhxsIBODS_vwLR2sjE'

    def start_requests(self):
        urls = [
            'https://kuaibao.qq.com/s/20170510A0AXAO00',
            'https://kuaibao.qq.com/s/20170512A0C7MK00',
            'https://kuaibao.qq.com/s/20170512A0C2BX00',
        ]
        # safari
        headers_safari = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
        # QQ browser
        headers_qq_browser = {'User-Agent': 'Mozilla/5.0 (iPhone 91; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.4.1 Mobile/14E304 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1'}
        # headers = []
        # headers.append(headers_safari)
        # headers.append(headers_qq_browser)
        for url in urls:
            yield scrapy.Request(url=url, headers=headers_qq_browser, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        datestring = datetime.datetime.now().strftime("%Y-%m-%d%H%M%S")
        filename = './scrapedata/%skuaibao-%s.html' % (datestring, page)
        logger.info(response.headers)
        logger.info(response.meta)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
