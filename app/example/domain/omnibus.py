from dataclasses import dataclass, field
from datetime import datetime
from typing import Annotated, Any, Dict, List, Optional


@dataclass
class Omnibus:
    birthtime: Annotated[Optional[datetime], "localdatetime"] = None
    sendtime: Annotated[Optional[datetime], "offsetdatetime"] = None
    toppings: List[Any] = field(default_factory=list)
    sides: List[Any] = field(default_factory=list)
    onFire: bool = False
    document: Optional[Any] = None
    pairing: Dict[str, str] = field(default_factory=dict)