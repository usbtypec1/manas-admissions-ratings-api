from fastapi import FastAPI

import routes

app = FastAPI()
app.include_router(routes.departments.router)
app.include_router(routes.applications.router)
