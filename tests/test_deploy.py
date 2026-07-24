from django.conf import settings


def test_debug_is_false():
    assert settings.DEBUG is False, "DEBUG musí byť False v produkcii!"