import time
import feedparser
from pushbullet import Pushbullet


def send_pb_msg(title, msg):
    Pushbullet('YOUR_ACCESS_TOKEN').push_note(title, msg)


def url_is_new(urlstr):
    if urlstr in urls:
        return False
    else:
        return True


while True:
    time.sleep(10)
    try:
        with open('viewed_urls.txt', 'r') as f:
            urls = f.readlines()
            urls = [url.rstrip() for url in urls]  # remove the '\n' char
    except FileNotFoundError:
        with open('viewed_urls.txt', 'w') as fp:
            pass

    rss = "YOUR_RSS_FEED_URL"
    feed = feedparser.parse(rss)
    for key in feed["entries"][:5]:
        title = key['title']
        url = key['links'][0]['href']
        body = key['summary']
        if url_is_new(url):
            msgTitle = title
            msg = f'{body[:body.find("<")]}\n{url}'
            send_pb_msg(msgTitle, msg)

            with open('viewed_urls.txt', 'a') as f:
                f.write('{}\n'.format(url))
