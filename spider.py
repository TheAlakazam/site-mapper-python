from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class Spider:
    
    # Class variable (shared among all instances)
    
    project_name = ''
    base_url = ''
    domain_name = ''
    crawl_file = ''
    queue_file = ''
    queue = set()
    crawled  = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.domain_name = domain_name
        Spider.base_url = base_url
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawl_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)
    
    @staticmethod
    def boot():
        createProjectDir(Spider.project_name)
        createDataFiles(Spider.project_name, Spider.base_url)
        Spider.queue = fileToSet(Spider.queue_file)
        Spider.crawled = fileToSet(Spider.crawl_file)
    
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if (response.getheader('content-type') == 'text/html'):
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
                finder = LinkFinder(Spider.base_url, page_url)
                finder.feed(html_string)
        except:
            print('error: can not crawl page')
            return set()
        
        return finder.page_links()
    
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        setToFile(Spider.queue, Spider.queue_file)
        setToFile(Spider.crawled, Spider.crawl_file)
    








