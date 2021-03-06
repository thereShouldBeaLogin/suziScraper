from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from celery.schedules import crontab
from suziScraper.celeryapp import app
import urllib.request
import os
from scrapy.crawler import CrawlerProcess
from scrapy_app.scrapy_app.spiders.bottoms import ScrapeBottoms


logger = get_task_logger(__name__)


@app.task
def scrape_bottoms():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0)'
    })

    process.crawl(ScrapeBottoms)
    process.start()


@app.task
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y


@shared_task(bind=True, autoretry_for=(NameError,),
             retry_kwargs={'max_retries': 5})  # retry in 30 minutes.
def ask_exc(self, x, y):
    try:
        # to get exception for retries
        something_raising()
    except Exception as exc:
        # overrides the default delay to retry after 1 minute
        raise self.retry(exc=exc, countdown=30)


@shared_task
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@shared_task(bind=True)
def upload_files(self, filenames):
    """
    created custom state 'PROGRESS'
    can be used to create progress bar
    """
    for i, file in enumerate(filenames):
        if not self.request.called_directly:
            self.update_state(state='PROGRESS',
                meta={'current': i, 'total': len(filenames)})


@app.task
def log_error(request, exc, traceback):
    with open(os.path.join('/suziScraper/errors', request.id), 'a') as fh:
        print('--\n\n{0}  {1}  {2}'.format(
            request.id, exc, traceback), file=fh)
