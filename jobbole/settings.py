BOT_NAME = 'jobbole'

SPIDER_MODULES = ['jobbole.spiders']
NEWSPIDER_MODULE = 'jobbole.spiders'

ROBOTSTXT_OBEY = False


DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

DOWNLOADER_MIDDLEWARES = {
   'jobbole.middlewares.UserAgentDownloadMiddleware': 543,
}

ITEM_PIPELINES = {
   'jobbole.pipelines.JobbolePipeline': 1,
}

#git is amzi