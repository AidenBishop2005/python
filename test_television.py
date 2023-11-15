import pytest
from television import *

class Test:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.tv.power()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.tv.power()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        self.tv.power()
        self.tv.mute() #mute
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv.mute() #unmute
        self.tv.volume_up()
        self.tv.mute() #mute
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"

    def test_channel_up(self):
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = True, Channel = 1, Volume = 0"

        for _ in range(Television.MAX_CHANNEL):
            self.tv.channel_up()

        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_channel_down(self):
        self.tv.power()
        self.tv.channel_down()
        self.tv.channel_down()
        assert self.tv.__str__() == "Power = True, Channel = 2, Volume = 0"

        for _ in range(Television.MAX_CHANNEL):
            self.tv.channel_down()

        assert self.tv.__str__() == "Power = True, Channel = 3, Volume = 0"

        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == "Power = False, Channel = 3, Volume = 0"

    def test_volume_up(self):
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"

        for _ in range(Television.MAX_VOLUME):
            self.tv.volume_up()

        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 2"

        self.tv.volume_down()
        self.tv.power()
        self.tv.volume_up()

        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 1"

    def test_volume_down(self):
        self.tv.power()
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"

        for _ in range(Television.MAX_VOLUME):
            self.tv.volume_up()

        self.tv.volume_down()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"
