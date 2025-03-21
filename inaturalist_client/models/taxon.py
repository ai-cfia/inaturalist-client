from typing import Optional

from pydantic import BaseModel, StrictInt, StrictStr


class Taxon(BaseModel):
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
