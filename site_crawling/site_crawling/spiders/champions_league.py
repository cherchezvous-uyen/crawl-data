import scrapy
from site_crawling.items import ChampionsLeagueItem
class ChampionsLeagueSpider(scrapy.Spider):
    name = "champions_league"
    allowed_domains = ["vnexpress.net"]
    start_urls = ["https://vnexpress.net/bong-da/champions-league"]
    visited_urls = set()

    def parse(self, response):
        articles = response.css('article.item-news h2.title-news a::attr(href)').getall()
        if not articles:
            self.logger.warning("Không thấy bài viết")
        for article in articles:
            yield response.follow(article, self.parse_article)

    def parse_article(self, response):
        content = response.xpath('//article//p').xpath('string(.)').getall()
        clean_content = [text.strip() for text in content if text.strip()]
        full_text = " ".join(clean_content)
        
        # Lấy nội dung description
        description = response.xpath('//p[@class="description"]/descendant-or-self::text()').getall()
        description_text = " ".join([desc.strip() for desc in description if desc.strip()])

        # Khởi tạo Item
        item = ChampionsLeagueItem()
        item['url'] = response.url
        item['title'] = response.xpath('//h1/text()').get()
        item['time'] = response.xpath('//meta[@itemprop="datePublished"]/@content').get()
        item['author'] = response.xpath('//p[@class="author_mail"]/text()').get()
        item['category'] = response.xpath('//ul[@class="breadcrumb"]/li[last()]/a/text()').get()
        item['content'] = full_text
        item['description'] = description_text if description_text else "Không có mô tả"
        item['tags'] = response.xpath('//meta[@name="keywords"]/@content').get()
        
        yield item