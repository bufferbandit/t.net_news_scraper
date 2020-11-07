from core.driver import driver 
from pprint import pprint


NEWS_URL = "http://tweakers.net/nieuws/"


def accept_cookies():
    cookie_button = driver.find_element_by_class_name("ctaButton")
    cookie_button.click()

def get_news_content_blocks():
    news_content_blocks = driver.find_elements_by_class_name("newsContentBlock")
    return news_content_blocks

def process_new_content_block(news_content_block):
    news_content_block_dict = {}
    

    title_xpath = './/h1/a' #'//div[@class="newsContentBlock"]/h1'
    article_xpath = './/div[@class="article largeWidth"]'  #'//div[@class="newsContentBlock"]/div[@class="article largeWidth"]'
    date_xpath = './/div[@class="articleColumn wide"]/p[@class="author"]//span[2]' #'//div[@class="newsContentBlock"]/div[@class="articleColumn wide"]/p[@class="author"]//span[2]' 

    title   = news_content_block.at_xpath(title_xpath)
    article = news_content_block.at_xpath(article_xpath)
    date    = news_content_block.at_xpath(date_xpath)

    news_content_block_dict["title"] = title.text()
    news_content_block_dict["date_text"] = date.text()
    news_content_block_dict["date"] = convert_date(date)
    news_content_block_dict["article"] = article.text()

    return news_content_block_dict

def convert_date(date,format=""):
    pass


def get_articles(news_url):
    driver.get(news_url)
    accept_cookies()
    articles = []
    for news_content_block in get_news_content_blocks():
        articles_dict = process_new_content_block(news_content_block)
        articles.append(articles_dict)
    return articles


if __name__ == "__main__":
    pprint(get_articles(NEWS_URL))
