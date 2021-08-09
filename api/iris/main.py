import sys
sys.path.append("../../")

import fastapi
import iris

app = fastapi.FastAPI(title='Boston Housing',
                      docs_url='/docs',
                      redoc_url='/redoc',
                      openapi_url='/openapi.json',
                      root_path='')

app.include_router(iris.router, prefix="/iris", tags=["iris"])
