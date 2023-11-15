class Television:
    """Represents a television."""

    MIN_VOLUME: int = 0  # Minimum volume level
    MAX_VOLUME: int = 2  # Maximum volume level
    MIN_CHANNEL: int = 0  # Minimum channel number
    MAX_CHANNEL: int = 3  # Maximum channel number

    def __init__(self) -> None:
        """Initializes a new television object."""
        self.__status: bool = False  # TV power status (on/off)
        self.__muted: bool = False  # Mute status (muted/unmuted)
        self.__volume: int = Television.MIN_VOLUME  # Current volume level
        self.__channel: int = Television.MIN_CHANNEL  # Current channel number
        self.__previous_volume: int = 0  # Temporary variable to store previous volume

    def power(self) -> None:
        """Toggles the TV power status (on/off)."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggles the mute status (muted/unmuted)."""
        if self.__status:
            if self.__muted:
                # Unmute and restore previous volume
                self.__muted = False
                self.__volume = self.__previous_volume
            else:
                # Save current volume and mute the TV
                self.__muted = True
                self.__previous_volume = self.__volume
                self.__volume = 0  # Mute by setting volume to zero

    def channel_up(self) -> None:
        """Changes the channel to the next higher channel number."""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Changes the channel to the next lower channel number."""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Increases the volume by one level."""
        if self.__status and self.__volume < Television.MAX_VOLUME and not self.__muted:
            self.__volume += 1

    def volume_down(self) -> None:
        """Decreases the volume by one level."""
        if self.__status and self.__volume > Television.MIN_VOLUME and not self.__muted:
            self.__volume -= 1

    def __str__(self) -> str:
        """Returns a string representation of the television's state."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
