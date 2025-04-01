from pydantic import BaseModel
from typing import Optional, List
from datetime import date

class TaskInfo(BaseModel):
    start_year: int
    end_year:int
    company_names: Optional[List[str]]=None
    model_names: Optional[List[str]]=None
    min_price: Optional[float]=None
    max_price: Optional[float]=None
    sources: Optional[List[str]]= ["A","B"]

class TaskSummary(BaseModel):
    id : int
    status: str
    filters: str

    class Config:
        orm_mode = True

class TaskData(BaseModel):
    source:str
    company_name:str
    model_name:str
    date:date
    price:float

    class Config:
        orm_mode = True
        
    