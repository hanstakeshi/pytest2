'''
    markup_tags test
'''
from logging import getLogger

from django.test import TestCase
from ..templatetags.markup_tags import mrkdwn

log = getLogger('django')


class MarkupTagsTest(TestCase):

    def test_mark(self):
        log.info('test_mark')
        self.assertEqual(mrkdwn('**bold**'), '<p><strong>bold</strong></p>')

        self.assertEqual(mrkdwn('<b>bold</b>'), '<p>bold</p>')

        self.assertEqual(mrkdwn('{@onclick=alert("hi")}some paragraph'),
            '<p>{@onclick=alert("hi")}some paragraph</p>')
