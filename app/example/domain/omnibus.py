from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, List, Optional, Dict


@dataclass
class Omnibus:
    birthtime: Optional[datetime] = None
    sendtime: Optional[datetime] = None
    toppings: List[Any] = field(default_factory=list)
    sides: List[Any] = field(default_factory=list)
    onFire: bool = False
    document: Optional[Any] = None
    pairing: Dict[str, str] = field(default_factory=dict)