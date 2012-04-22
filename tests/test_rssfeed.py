from datetime import datetime
from feedgenerator.generator import Rss201rev2Feed, RssUserland091Feed


class TestRssFeed(object):

    def _get_encoding(self):
        return 'utf8'

    def _get_feed_kwargs(self):
        return {
            'title': u'Feed Generator Updates',
            'description': u'Updates about releases of the feedgenerator package.',
            'link': u'https://github.com/ametaireau/feedgenerator',
        }

    def _get_feed_item_kwargs(self):
        return {
            'title': u'New Release',
            'link': u'https://github.com/ametaireau/feedgenerator',
            'description': u'Release notes for fresh release of the feed ' \
                    'generator.',
            'pubdate': datetime.now()
        }
        
    def _get_Rss201rev2Feed(self, input_kwargs):
        return Rss201rev2Feed(**input_kwargs)

    def _get_RssUserland091Feed(self, input_kwargs):
        return RssUserland091Feed(**input_kwargs)
    
    def test_Rss201rev2Feed(self):
        input_kwargs = self._get_feed_kwargs()
        feed = self._get_Rss201rev2Feed(input_kwargs)
        encoding = self._get_encoding()
        title_str = input_kwargs['title'].encode(encoding)
        assert title_str in feed.writeString(encoding), \
                "Feed output does not contain feed title."

    def test_RssUserland091Feed(self):
        input_kwargs = self._get_feed_kwargs()
        feed = self._get_RssUserland091Feed(input_kwargs)
        encoding = self._get_encoding()
        title_str = input_kwargs['title'].encode(encoding)
        assert title_str in feed.writeString(encoding), \
                "Feed output does not contain feed title."

    def test_Rss201rev2Feed_item(self):
        input_kwargs = self._get_feed_kwargs()
        feed = self._get_Rss201rev2Feed(input_kwargs)
        item_input_kwargs = self._get_feed_item_kwargs()
        feed.add_item(**item_input_kwargs)
        encoding = self._get_encoding()
        title_str = item_input_kwargs['title'].encode(encoding)
        assert title_str in feed.writeString(encoding), \
                "Feed output does not contain feed item title."

    def test_RssUserland091Feed_item(self):
        input_kwargs = self._get_feed_kwargs()
        feed = self._get_RssUserland091Feed(input_kwargs)
        item_input_kwargs = self._get_feed_item_kwargs()
        feed.add_item(**item_input_kwargs)
        encoding = self._get_encoding()
        title_str = item_input_kwargs['title'].encode(encoding)
        assert title_str in feed.writeString(encoding), \
                "Feed output does not contain feed item title."
