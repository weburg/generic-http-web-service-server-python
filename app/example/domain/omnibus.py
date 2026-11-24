from dataclasses import dataclass, field
from datetime import datetime
from typing import Annotated, Any, Dict, List, Optional

from app.example.domain.bus import Bus


@dataclass
class Omnibus(Bus):
    birthtime: Annotated[Optional[datetime], "localdatetime"] = None
    sendtime: Annotated[Optional[datetime], "offsetdatetime"] = None
    toppings: List[Any] = field(default_factory=list)
    sides: List[Any] = field(default_factory=list)
    onFire: bool = False
    document: Optional[Any] = None
    pairing: Dict[str, str] = field(default_factory=dict)

    def __post_init__(self):
        super().__init__("omni-58-87")