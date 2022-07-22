"""Run module tests."""
import pytest

@pytest.mark.test_modules
def test_main():
    """Test main package works."""
    from translator_template.main import spool_file  # pylint: disable=import-outside-toplevel, unused-import
    spool_file('tests/spooler/queued/file1.example')
    assert True
