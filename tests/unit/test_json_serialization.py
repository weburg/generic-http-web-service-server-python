import json
from datetime import datetime, timezone
from unittest import TestCase

from app.example.domain.omnibus import Omnibus
from app.server import json_default


class TestJsonSerialization(TestCase):
    def test_omnibus_uses_bus_defaults(self):
        omnibus = Omnibus()

        self.assertEqual("omni-58-87", omnibus._Bus__callsign)
        self.assertEqual("yellow", omnibus.color)

        serialized = json.dumps(omnibus, default=json_default)
        self.assertNotIn('"_Bus__callsign"', serialized)
        self.assertIn('"color": "yellow"', serialized)

    def test_omnibus_datetime_fields_use_microseconds(self):
        omnibus = Omnibus(
            birthtime=datetime.fromisoformat("2016-05-11T12:00:00"),
            sendtime=datetime(2026, 11, 23, 9, 11, 36, 978197, tzinfo=timezone.utc),
        )

        serialized = json.dumps(omnibus, default=json_default)

        self.assertIn('"birthtime": "2016-05-11T12:00:00.000000"', serialized)
        self.assertIn('"sendtime": "2026-11-23T09:11:36.978197+00:00"', serialized)

    def test_localdatetime_rejects_timezone_offset(self):
        omnibus = Omnibus(
            birthtime=datetime(2016, 5, 11, 12, 0, tzinfo=timezone.utc),
        )

        with self.assertRaisesRegex(ValueError, "Must not include a timezone offset"):
            json.dumps(omnibus, default=json_default)
