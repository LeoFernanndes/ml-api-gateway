import sys
sys.path.append("../../")

import fastapi
import iris

app = fastapi.FastAPI()
app.include_router(iris.router, prefix="/boston-housing", tags=["iris"])
