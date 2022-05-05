from unittest.mock import patch

from pythonit_toolkit.emails.utils import SafeString, get_email_backend, mark_safe
from ward import test, raises


class TestBackend:
    pass


class TestBackendWithEnv:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b


@test("get email backend")
async def _():
    loaded_backend = get_email_backend("tests.emails.test_utils.TestBackend")
    assert "tests.emails.test_utils.TestBackend" in str(type(loaded_backend))


@test("loading the same backend path uses the cache")
async def _():
    loaded_backend = get_email_backend("tests.emails.test_utils.TestBackend")
    assert "tests.emails.test_utils.TestBackend" in str(type(loaded_backend))

    with patch("pythonit_toolkit.emails.utils.importlib.import_module") as mock:
        loaded_backend = get_email_backend(
            "tests.emails.test_utils.TestBackend")

    assert "tests.emails.test_utils.TestBackend" in str(type(loaded_backend))
    assert not mock.called

    mock.reset_mock()

    with patch("pythonit_toolkit.emails.utils.importlib.import_module") as mock:
        get_email_backend("tests.emails.test_utils.TestBackend2")

    assert mock.called


@test("get email backend passing environment variables")
async def _():
    loaded_backend = get_email_backend(
        "tests.emails.test_utils.TestBackendWithEnv", a=1, b=2
    )
    assert loaded_backend.a == 1
    assert loaded_backend.b == 2


@test("mark safe")
async def _():
    safe_string = mark_safe("abc")

    assert isinstance(safe_string, SafeString)
    assert str(safe_string) == "abc"


@test("mark safe with empty string")
async def _():
    safe_string = mark_safe("")

    assert isinstance(safe_string, SafeString)
    assert str(safe_string) == ""


@test("None cannot be converted to safe string")
async def _():
    with raises(ValueError):
        mark_safe(None)
