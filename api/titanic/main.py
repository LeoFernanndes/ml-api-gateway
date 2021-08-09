import sys
sys.path.append("../../")

import fastapi
import titanic

app = fastapi.FastAPI(title='Titanic',
                      docs_url='/titanic/docs',
                      redoc_url='/titanic/redoc',
                      openapi_url='/titanic/openapi.json',
                      root_path='')

app.include_router(titanic.router, prefix="/titanic", tags=["titanic"])

