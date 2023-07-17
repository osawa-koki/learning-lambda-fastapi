from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/", status_code=200)
async def root():
  return {"message": "Hello Get."}

# @app.post("/", status_code=200)
# async def root():
#   return {"message": "Hello POST."}

# @app.put("/", status_code=200)
# async def root():
#   return {"message": "Hello PUT."}

# @app.delete("/", status_code=200)
# async def root():
#   return {"message": "Hello DELETE."}

lambda_handler = Mangum(app)
