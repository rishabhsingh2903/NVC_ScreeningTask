from fastapi import FastAPI
from app.database import engine, Base

from app.routes import taskRoutes
app = FastAPI(title="Car dealership Analytics API")

Base.metadata.create_all(bind=engine)


app.include_router(taskRoutes.router,prefix="/tasks",tags=["tasks"])


