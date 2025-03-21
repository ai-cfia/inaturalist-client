from typing import Optional

from pydantic import BaseModel, StrictInt, StrictStr

from inaturalist_client.models.taxon import Taxon


class ProjectObservationRule(BaseModel):
    id: Optional[StrictInt] = None
    operand_id: Optional[StrictInt] = None
    operand_type: Optional[StrictStr] = None
    operator: Optional[StrictStr] = None
    taxon: Optional[Taxon] = None
