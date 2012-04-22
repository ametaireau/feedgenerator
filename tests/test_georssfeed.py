from feedgenerator.contrib.gis.feeds import GeoRSSFeed
from feedgenerator.contrib.gis.geometry import Geometry


class TestGeoRssFeed(object):

    def _get_encoding(self):
        return 'utf8'

    def _get_feed_kwargs(self):
        return {
            'title': u'Feed Generator Updates',
            'description': u'Updates about releases of the feedgenerator package.',
            'link': u'https://github.com/ametaireau/feedgenerator',
        }
        
    def _get_feed(self, input_kwargs):
        return GeoRSSFeed(**input_kwargs)

    def _get_feed_item_kwargs(self):
        return {
            'title': u'New Release',
            'link': u'https://github.com/ametaireau/feedgenerator',
            'description': u'Release notes for fresh release of the feed ' \
                    'generator.'
        }

    def _get_point(self):
        lat, lon = (37.804359, -122.271116)
        # Swap because by default mixing expects these backwards.
        return Geometry('point', (lon, lat))
    
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
        point = self._get_point()
        item_input_kwargs['geometry'] = point
        feed.add_item(**item_input_kwargs)
        encoding = self._get_encoding()
        title_str = item_input_kwargs['title'].encode(encoding)
        feed_str = feed.writeString(encoding)
        assert title_str in feed_str, \
                "Feed output does not contain feed item title."
        assert str(point.coords[0]) in feed_str, \
                "Feed output does not contain feed item coordinate."
        assert str(point.coords[1]) in feed_str, \
                "Feed output does not contain feed item coordinate."
