from fastapi import FastAPI
from pydantic import BaseModel
from typing import List,Dict,Any,Optional
import pandas as pd
from svdf_engine import analyze
app=FastAPI(title='SVDF Decision Studio API',version='2.0.0')
class Request(BaseModel):
    projects:List[Dict[str,Any]]
    draws:int=2000
    seed:int=2026
    budget:Optional[float]=None
@app.get('/health')
def health():return {'status':'ok','service':'SVDF Decision Studio'}
@app.post('/analyze')
def run(req:Request):return analyze(pd.DataFrame(req.projects),req.draws,req.seed,req.budget)
