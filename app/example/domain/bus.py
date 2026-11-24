from dataclasses import dataclass, field


@dataclass(init=False)
class Bus:
    __callsign: str = field(init=False)
    color: str = field(default="yellow", init=False)

    def __init__(self, callsign: str):
        self.__callsign = callsign
