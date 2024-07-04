"""
from unittest.mock import MagicMock
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandsTestCase(SimpleTestCase):
    """Test cases for commands module"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if db ready"""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting operational error"""
        # Mock raise of two psycopg errors (mock db not started yet) and
        # three operational error (mock database is accepting connections but the db is not ready)
        # and finally return true
        patched_check.side_effect = [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        # check all 6 calls [2 + 3 + 1]
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
