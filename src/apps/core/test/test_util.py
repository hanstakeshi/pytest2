'''
    util test's
'''
from logging import getLogger

from django.test import TestCase
from ..util.youtube import YoutubeVideo
from ..util.log import main
from ..util.util import choice_to_dict, chunks

log = getLogger('django')


class UtilTest(TestCase):
    # fixtures = ['.json']

    def setUp(self):
        self.yv = YoutubeVideo('https://www.youtube.com/watch?v=qrhRUOsKAsM')

    def test_youtube(self):
        log.info('test_youtube')
        self.assertEqual(self.yv.id, 'qrhRUOsKAsM')
        self.assertEqual(self.yv.embed_url,
            'https://www.youtube.com/embed/qrhRUOsKAsM')
        # miniaturas
        self.assertEqual(self.yv.get_img('m'),
            'https://img.youtube.com/vi/qrhRUOsKAsM/mqdefault.jpg')
        self.assertEqual(self.yv.get_img('no-size'),
            'https://img.youtube.com/vi/qrhRUOsKAsM/0.jpg')

    def test_log(self):
        log.info('test_youtube')
        main()

    def test_util(self):
        # choice_to_dict
        choice = (
            ('p', 'python'),
            ('d', 'dj')
        )

        self.assertEqual(choice_to_dict(choice), {'p': 'python', 'd': 'dj'})

        # chunks
        l = [1, 2, 3, 4, 5]
        self.assertEqual(tuple(chunks(l, 3)), ([1, 2, 3], [4, 5]))
