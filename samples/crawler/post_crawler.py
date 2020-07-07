import logging
import os
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG)

class Post:
    author = ""
    content = ""
    gender = ""
    age = 0
    vote = 0
    comment = 0

    def print_content(self):
        text = "Author: {}\nComment:{}, Vote:{}, Age:{}, Gender:{}\n{}".format(self.author, self.comment, self.vote, self.age, self.gender, self.content)
        logging.debug(text)
        return text

class PostCrawler:
    def get_posts(self, url):
        html = self.download_page(url)
        return self.parse_content(html)        
        
    def download_page(self, url):
        logging.debug("Download page: {}. ".format(url))
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
        r = requests.get(url, headers)
        return r.text

    def parse_content(self, html):
        posts = []
        soup = BeautifulSoup(html, 'html.parser')
        con = soup.find("div", {"id": "content"})
        con_list = con.find_all('div', {"class": "article"})
        for i in con_list:
           post = self.parse_post(i)
           posts.append(post)

        return posts

    def parse_post(self, i):
        post = Post()

        post.author = i.find('h2').string
        post.content = i.find('div', {"class": 'content'}).find('span').get_text().strip()
        stats = i.find('div', {"class": 'stats'})
        post.vote = stats.find('span', {"class": 'stats-vote'}).find('i', {"class": 'number'}).string
        post.comment = stats.find('span', {"class": 'stats-comments'}).find('i', {"class": 'number'}).string
        author_info = i.find('div', {"class":'stats-vote'})
        if author_info is not None:
            class_list = author_info['class']
            if "wonmenIcon" in class_list:
                post.gender = 'female'
            elif "manIcon" in class_list:
                post.gender = 'male'
            else:
                post.gender = ''
            post.age = author_info.string
        else:
            post.gender = ''
            post.age = ''
        return post

def main():
    logging.debug("Start crawler")

    posts = []
    crawler = PostCrawler()
    page = 1
    for page in range(1, 15):
        logging.debug("Start craw page {}".format(page))
        url = 'https://qiushibaike.com/text/page/{}'.format(page)        
        posts.extend(crawler.get_posts(url))

    

    with open('posts.txt', 'a', encoding='utf-8') as file:
        for p in posts: 
            text = p.print_content()
            file.write(text)    
    logging.debug("Current dir: {}".format(os.getcwd()))

if __name__ == '__main__':
    main()
