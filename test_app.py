import os
from app import get_secret_status


def test_secret_exists():
    os.environ["APP_SECRET"] = "test-secret"
    assert get_secret_status() == "Secret is configured"


def test_secret_missing():
    os.environ.pop("APP_SECRET", None)
    assert get_secret_status() == "Secret is missing"
