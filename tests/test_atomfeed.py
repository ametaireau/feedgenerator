from datetime import datetime
from feedgenerator.generator import Atom1Feed


class TestAtom1Feed(object):

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
        
    def _get_feed(self, input_kwargs):
        return Atom1Feed(**input_kwargs)
    
    def test_feed(self):
        input_kwargs = self._get_feed_kwargs()
        feed = self._get_feed(input_kwargs)
        encoding = self._get_encoding()
        title_str = input_kwargs['title'].encode(encoding)
        assert title_str in feed.writeString(encoding), \
                "Feed output does not contain feed title."

    def test_feed_item(self):
        input_kwargs = self._get_feed_kwargs()
        feed = self._get_feed(input_kwargs)
        item_input_kwargs = self._get_feed_item_kwargs()
        feed.add_item(**item_input_kwargs)
        encoding = self._get_encoding()
        title_str = item_input_kwargs['title'].encode(encoding)
        assert title_str in feed.writeString(encoding), \
                "Feed output does not contain feed item title."
