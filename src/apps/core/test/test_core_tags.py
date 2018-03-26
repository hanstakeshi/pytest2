'''
    markup_tags test
'''
from logging import getLogger

from django.test import TestCase
from ..templatetags.core_tags import (br, floatdot, get_range, get_item,
    split as _split, tel)

log = getLogger('django')


class CoreTagsTest(TestCase):

    def test_br(self):
        log.info('test_br')
        self.assertEqual(br('texto//salto'), 'texto<br>salto')
        self.assertEqual(br('texto///salto'), 'texto<br>/salto')
        self.assertEqual(br('texto////<br>salto'), 'texto<br><br><br>salto')

    def test_floatdot(self):
        log.info('test_floatdot')
        self.assertEqual(floatdot('1.2'), '1.2000')
        self.assertEqual(floatdot(1.2), '1.2000')
        self.assertEqual(floatdot('1,2', 2), '1.20')
        self.assertEqual(floatdot('12'), '12.0000')
        self.assertEqual(floatdot(12), '12.0000')

    def test_get_range(self):
        log.info('test_get_range')
        self.assertEqual(list(get_range(5)), list(xrange(5)))

    def test_get_item(self):
        log.info('test_get_item')
        d = {'a': 1, 'b': 'c'}

        self.assertEqual(get_item(d, 'a'), 1)
        self.assertEqual(get_item(d, 'd'), '')

    def test_split(self):
        log.info('test_split')

        self.assertEqual(_split('hola-a-todos', '-'), ['hola', 'a', 'todos'])
        self.assertEqual(_split('hola//a//todos'), ['hola', 'a', 'todos'])

    def test_tel(self):
        log.info('test_tel')

        self.assertEqual(tel('543-1428'), '5431428')
        self.assertEqual(tel('543-14-28'), '5431428')
        self.assertEqual(tel('+511 543 14 28'), '5115431428')
