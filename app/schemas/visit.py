from datetime import datetime
from pydantic import BaseModel, ConfigDict


class PageVisitCreate(BaseModel):
    page : str
    user_agent : str



class PageVisitResponse(BaseModel):
    id: int
    page: str
    user_agent: str
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)

