import unittest
from unittest.mock import Mock
import index

Events = index.Events

class TestEvents(unittest.TestCase):
    def test_events_can_be_registered_then_triggered(self):
        events = Events()
        cb1 = Mock()

        events.on('click', cb1)
        events.trigger('click')

        self.assertEqual(cb1.call_count, 1)

    def test_multiple_events_can_be_registered_then_triggered(self):
        events = Events()
        cb1 = Mock()
        cb2 = Mock()

        events.on('click', cb1)
        events.on('click', cb2)
        print(events.events)
        events.trigger('click')
        print(events.__dict__)

        self.assertEqual(cb1.call_count, 1)
        self.assertEqual(cb2.call_count, 1)

    def test_events_can_be_triggered_multiple_times(self):
        events = Events()
        cb1 = Mock()
        cb2 = Mock()

        events.on('click', cb1)
        events.trigger('click')
        events.on('click', cb2)
        events.trigger('click')
        events.trigger('click')

        self.assertEqual(cb1.call_count, 3)
        self.assertEqual(cb2.call_count, 2)

    def test_events_can_have_different_names(self):
        events = Events()
        cb1 = Mock()
        cb2 = Mock()

        events.on('click', cb1)
        events.trigger('click')
        events.on('hover', cb2)
        events.trigger('click')
        events.trigger('hover')

        self.assertEqual(cb1.call_count, 2)
        self.assertEqual(cb2.call_count, 1)

    def test_events_can_be_toggled_off(self):
        events = Events()
        cb1 = Mock()
        cb2 = Mock()

        events.on('hover', cb2)
        events.on('click', cb1)
        events.trigger('click')
        events.off('click')
        events.trigger('click')
        events.trigger('hover')

        self.assertEqual(cb1.call_count, 1)
        self.assertEqual(cb2.call_count, 1)

if __name__ == '__main__':
    unittest.main()
