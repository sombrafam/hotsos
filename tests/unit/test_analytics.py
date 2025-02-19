import os

import datetime
import tempfile

import utils

from core import analytics
from core.searchtools import FileSearcher, SearchDef


SEQ_TEST_1 = """2021-07-19 09:01:58.498 iteration:0 start
2021-07-19 09:02:58.498 iteration:0 end
2021-07-19 09:03:58.498 iteration:1 start
2021-07-19 09:04:58.498 iteration:1 end
"""

SEQ_TEST_2 = """2021-07-19 09:01:58.498 iteration:1 start
2021-07-19 09:02:58.498 iteration:1 end
2021-07-19 09:03:58.498 iteration:0 start
2021-07-19 09:04:58.498 iteration:0 end
"""

SEQ_TEST_3 = """2021-07-19 09:01:58.498 iteration:0 start
2021-07-19 09:02:58.498 iteration:0 end
2021-07-19 09:03:58.498 iteration:1 start
2021-07-19 09:04:58.498 iteration:1 end
2021-07-19 09:05:58.498 iteration:0 start
2021-07-19 09:06:58.498 iteration:0 end
"""

SEQ_TEST_4 = """2021-07-19 09:01:58.498 iteration:0 start
2021-07-19 09:03:58.498 iteration:1 start
2021-07-19 09:04:58.498 iteration:1 end
2021-07-19 09:05:58.498 iteration:0 start
2021-07-19 09:06:58.498 iteration:0 start
2021-07-19 09:07:58.498 iteration:0 end
"""

SEQ_TEST_5 = """2021-07-19 09:01:58.498 iteration:0 start
2021-07-19 09:03:58.498 iteration:1 start
2021-07-19 09:04:58.498 iteration:1 end
2021-07-19 09:05:58.498 iteration:0 start
2021-07-19 09:05:58.498 iteration:1 start
2021-07-19 09:07:58.498 iteration:0 end
"""

SEQ_TEST_6 = """2021-07-19 09:01:58.498 iteration:0 start
2021-07-19 09:03:58.498 iteration:1 start
2021-07-19 09:04:58.498 iteration:1 end
2021-07-19 09:05:58.498 iteration:0 start
2021-07-19 09:06:58.498 iteration:1 start
2021-07-19 09:07:58.498 iteration:0 end
2021-07-19 09:08:58.498 iteration:0 start
2021-07-19 09:09:58.498 iteration:0 end
"""


class TestAnalytics(utils.BaseTestCase):

    def test_ordered_complete(self):
        start0 = datetime.datetime(2021, 7, 19, 9, 1, 58, 498000)
        end0 = datetime.datetime(2021, 7, 19, 9, 2, 58, 498000)
        start1 = datetime.datetime(2021, 7, 19, 9, 3, 58, 498000)
        end1 = datetime.datetime(2021, 7, 19, 9, 4, 58, 498000)
        expected = {'0': {'duration': 60.0,
                          'start': start0, 'end': end0},
                    '1': {'duration': 60.0, 'start': start1, 'end': end1}}
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ftmp:
            ftmp.write(SEQ_TEST_1)
            ftmp.close()
            s = FileSearcher()
            expr = r'^([0-9\-]+) (\S+) iteration:([0-9]+) start'
            s.add_search_term(SearchDef(expr, tag="eventX-start"),
                              path=ftmp.name)
            expr = r'^([0-9\-]+) (\S+) iteration:([0-9]+) end'
            s.add_search_term(SearchDef(expr, tag="eventX-end"),
                              path=ftmp.name)
            events = analytics.LogEventStats(s.search(), "eventX")
            os.remove(ftmp.name)

        events.run()
        top5 = events.get_top_n_events_sorted(5)
        self.assertEqual(top5, expected)
        stats = events.get_event_stats()
        expected = {'avg': 60.0, 'max': 60.0, 'min': 60.0, 'samples': 2,
                    'stdev': 0.0}
        self.assertEqual(stats, expected)

    def test_unordered_complete(self):
        start0 = datetime.datetime(2021, 7, 19, 9, 3, 58, 498000)
        end0 = datetime.datetime(2021, 7, 19, 9, 4, 58, 498000)
        start1 = datetime.datetime(2021, 7, 19, 9, 1, 58, 498000)
        end1 = datetime.datetime(2021, 7, 19, 9, 2, 58, 498000)
        expected = {'0': {'duration': 60.0,
                          'start': start0, 'end': end0},
                    '1': {'duration': 60.0, 'start': start1, 'end': end1}}
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ftmp:
            ftmp.write(SEQ_TEST_2)
            ftmp.close()
            s = FileSearcher()
            expr = r'^([0-9\-]+) (\S+) iteration:([0-9]+) start'
            s.add_search_term(SearchDef(expr, tag="eventX-start"),
                              path=ftmp.name)
            expr = r'^([0-9\-]+) (\S+) iteration:([0-9]+) end'
            s.add_search_term(SearchDef(expr, tag="eventX-end"),
                              path=ftmp.name)
            events = analytics.LogEventStats(s.search(), "eventX")
            os.remove(ftmp.name)

        events.run()
        top5 = events.get_top_n_events_sorted(5)
        self.assertEqual(top5, expected)
        stats = events.get_event_stats()
        expected = {'avg': 60.0, 'max': 60.0, 'min': 60.0, 'samples': 2,
                    'stdev': 0.0}
        self.assertEqual(stats, expected)

    def test_ordered_complete_clobbered(self):
        start0 = datetime.datetime(2021, 7, 19, 9, 5, 58, 498000)
        end0 = datetime.datetime(2021, 7, 19, 9, 6, 58, 498000)
        start1 = datetime.datetime(2021, 7, 19, 9, 3, 58, 498000)
        end1 = datetime.datetime(2021, 7, 19, 9, 4, 58, 498000)
        expected = {'0': {'duration': 60.0,
                          'start': start0, 'end': end0},
                    '1': {'duration': 60.0, 'start': start1, 'end': end1}}
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ftmp:
            ftmp.write(SEQ_TEST_3)
            ftmp.close()
            s = FileSearcher()
            expr = r'^([0-9\-]+) (\S+) iteration:([0-9]+) start'
            s.add_search_term(SearchDef(expr, tag="eventX-start"),
                              path=ftmp.name)
            expr = r'^([0-9\-]+) (\S+) iteration:([0-9]+) end'
            s.add_search_term(SearchDef(expr, tag="eventX-end"),
                              path=ftmp.name)
            events = analytics.LogEventStats(s.search(), "eventX")
            os.remove(ftmp.name)

        events.run()
        top5 = events.get_top_n_events_sorted(5)
        self.assertEqual(top5, expected)
        stats = events.get_event_stats()
        expected = {'avg': 60.0,
                    'max': 60.0,
                    'min': 60.0,
                    'samples': 2,
                    'stdev': 0.0}
        self.assertEqual(stats, expected)

    def test_ordered_incomplete_clobbered(self):
        start0 = datetime.datetime(2021, 7, 19, 9, 6, 58, 498000)
        end0 = datetime.datetime(2021, 7, 19, 9, 7, 58, 498000)
        start1 = datetime.datetime(2021, 7, 19, 9, 3, 58, 498000)
        end1 = datetime.datetime(2021, 7, 19, 9, 4, 58, 498000)
        expected = {'0': {'duration': 60.0,
                          'start': start0, 'end': end0},
                    '1': {'duration': 60.0, 'start': start1, 'end': end1}}
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ftmp:
            ftmp.write(SEQ_TEST_4)
            ftmp.close()
            s = FileSearcher()
            expr = r'^([0-9\-]+) (\S+) iteration:([0-9]+) start'
            s.add_search_term(SearchDef(expr, tag="eventX-start"),
                              path=ftmp.name)
            expr = r'^([0-9\-]+) (\S+) iteration:([0-9]+) end'
            s.add_search_term(SearchDef(expr, tag="eventX-end"),
                              path=ftmp.name)
            events = analytics.LogEventStats(s.search(), "eventX")
            os.remove(ftmp.name)

        events.run()
        top5 = events.get_top_n_events_sorted(5)
        self.assertEqual(top5, expected)
        stats = events.get_event_stats()
        expected = {'avg': 60.0,
                    'incomplete': 1,
                    'max': 60.0,
                    'min': 60.0,
                    'samples': 2,
                    'stdev': 0.0}
        self.assertEqual(stats, expected)

    def test_ordered_incomplete_clobbered2(self):
        start0 = datetime.datetime(2021, 7, 19, 9, 5, 58, 498000)
        end0 = datetime.datetime(2021, 7, 19, 9, 7, 58, 498000)
        start1 = datetime.datetime(2021, 7, 19, 9, 3, 58, 498000)
        end1 = datetime.datetime(2021, 7, 19, 9, 4, 58, 498000)
        expected = {'0': {'duration': 120.0,
                          'start': start0, 'end': end0},
                    '1': {'duration': 60.0, 'start': start1, 'end': end1}}
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ftmp:
            ftmp.write(SEQ_TEST_5)
            ftmp.close()
            s = FileSearcher()
            expr = r'^([0-9\-]+) (\S+) iteration:([0-9]+) start'
            s.add_search_term(SearchDef(expr, tag="eventX-start"),
                              path=ftmp.name)
            expr = r'^([0-9\-]+) (\S+) iteration:([0-9]+) end'
            s.add_search_term(SearchDef(expr, tag="eventX-end"),
                              path=ftmp.name)
            events = analytics.LogEventStats(s.search(), "eventX")
            os.remove(ftmp.name)

        events.run()
        top5 = events.get_top_n_events_sorted(5)
        self.assertEqual(top5, expected)
        stats = events.get_event_stats()
        expected = {'avg': 90.0, 'incomplete': 2, 'max': 120.0, 'min': 60.0,
                    'samples': 2, 'stdev': 30.0}
        self.assertEqual(stats, expected)

    def test_ordered_multiple(self):
        start0 = datetime.datetime(2021, 7, 19, 9, 8, 58, 498000)
        end0 = datetime.datetime(2021, 7, 19, 9, 9, 58, 498000)
        start1 = datetime.datetime(2021, 7, 19, 9, 3, 58, 498000)
        end1 = datetime.datetime(2021, 7, 19, 9, 4, 58, 498000)
        expected = {'0': {'duration': 60.0,
                          'start': start0, 'end': end0},
                    '1': {'duration': 60.0, 'start': start1, 'end': end1}}
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as ftmp:
            ftmp.write(SEQ_TEST_6)
            ftmp.close()
            s = FileSearcher()
            expr = r'^([0-9\-]+) (\S+) iteration:([0-9]+) start'
            s.add_search_term(SearchDef(expr, tag="eventX-start"),
                              path=ftmp.name)
            expr = r'^([0-9\-]+) (\S+) iteration:([0-9]+) end'
            s.add_search_term(SearchDef(expr, tag="eventX-end"),
                              path=ftmp.name)
            events = analytics.LogEventStats(s.search(), "eventX")
            os.remove(ftmp.name)

        events.run()
        top5 = events.get_top_n_events_sorted(5)
        self.assertEqual(top5, expected)
        stats = events.get_event_stats()
        expected = {'avg': 60.0, 'incomplete': 2, 'max': 60.0, 'min': 60.0,
                    'samples': 2, 'stdev': 0.0}
        self.assertEqual(stats, expected)
