import pytest
from television import Television


def test_init():
    tv = Television()
    assert tv.status is False
    assert tv.muted is False
    assert tv.volume == Television.MIN_VOLUME
    assert tv.channel == Television.MIN_CHANNEL


def test_power():
    tv = Television()
    tv.power()
    assert tv.status is True

    tv.power()
    assert tv.status is False


def test_mute():
    tv = Television()
    tv.mute()
    assert tv.muted is True

    tv.mute()
    assert tv.muted is False


def test_channel_up():
    tv = Television()
    tv.channel_up()
    assert tv.channel == Television.MIN_CHANNEL + 1

    for _ in range(Television.MAX_CHANNEL - Television.MIN_CHANNEL):
        tv.channel_up()

    tv.channel_up()
    assert tv.channel == Television.MIN_CHANNEL


def test_channel_down():
    tv = Television()
    tv.channel = Television.MAX_CHANNEL
    tv.channel_down()
    assert tv.channel == Television.MAX_CHANNEL - 1

    for _ in range(Television.MAX_CHANNEL - Television.MIN_CHANNEL):
        tv.channel_down()

    tv.channel_down()
    assert tv.channel == Television.MAX_CHANNEL


def test_volume_up():
    tv = Television()
    tv.volume_up()
    assert tv.volume == Television.MIN_VOLUME + 1

    for _ in range(Television.MAX_VOLUME):
        tv.volume_up()

    tv.volume_up()
    assert tv.volume == Television.MIN_VOLUME


def test_volume_down():
    tv = Television()
    tv.volume = Television.MAX_VOLUME
    tv.volume_down()
    assert tv.volume == Television.MAX_VOLUME - 1

    for _ in range(Television.MAX_VOLUME - Television.MIN_VOLUME):
        tv.volume_down()

    tv.volume_down()
    assert tv.volume == Television.MAX_VOLUME
