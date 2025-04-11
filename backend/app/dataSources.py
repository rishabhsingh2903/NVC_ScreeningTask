import pandas as pd
from datetime import datetime as dt
from typing import List,Dict


SourceAPath = "data/sourceA.json"
SourceBPath = "data/sourceB.csv"

def loadFilteredData(filters:Dict) -> List[Dict]:
    start_year = filters['start_year']
    end_year = filters['end_year']
    company_names = filters.get("company_names",[])
    model_names = filters.get("model_names",[])
    min_price = filters.get("min_price")
    max_price = filters.get("max_price")
    sources = filters.get("sources",["A","B"])

    rows =[]
    if "A" in sources:
       rows+= loadSourceA(start_year,end_year,company_names,model_names,min_price,max_price)
    if "B" in sources:
        rows+= loadSourceB(start_year,end_year,company_names,model_names,min_price,max_price)

    return rows

def applyFilters(df: pd.DataFrame, start_year: int, end_year: int, company_names: List[str], model_names: List[str], min_price: float, max_price: float) -> pd.DataFrame:
    df['date'] = pd.to_datetime(df['date'])
    df = df[df['date'].dt.year.between(start_year, end_year)]

    if company_names:
        df = df[df['company'].isin(company_names)]  # ✅ fixed column name
    if model_names:
        df = df[df['model'].isin(model_names)]      # ✅ fixed column name
    if min_price is not None:
        df = df[df['price'] >= min_price]
    if max_price is not None:
        df = df[df['price'] <= max_price]
    return df


def loadSourceA(start_year:int,end_year:int,company_names:List[str],model_names:List[str],min_price:float,max_price:float) -> List[Dict]:
    df = pd.read_json(SourceAPath)
    df["source"] = "A"
    df = applyFilters(df,start_year,end_year,company_names,model_names,min_price,max_price)
    return df.to_dict(orient='records')

def loadSourceB(start_year:int,end_year:int,company_names:List[str],model_names:List[str],min_price:float,max_price:float) -> List[Dict]:
    df = pd.read_csv(SourceBPath)
    df["source"] = "B"
    df = applyFilters(df,start_year,end_year,company_names,model_names,min_price,max_price)
    return df.to_dict(orient='records')




