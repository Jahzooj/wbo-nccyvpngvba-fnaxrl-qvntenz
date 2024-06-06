from fastapi import Depends

from app.app import app
from app.database import get_db
from app.models import Application
from app.config import logger

@app.get('/status/', tags=['utility'])
async def status():
    return {'message': '200-ok'}

@app.get("/status-db/", tags=['utility'])
async def read_root(db = Depends(get_db)):
    a = db.query(Application).first()
    print(a.name)
    return {"message": "Hello World"}


@app.post('/submit-application/', tags=['application'])
async def submit_application():
    pass

@app.get('/check-application/', tags=['application'])
async def submit_application():
    pass

@app.get('/build-report-sankey/', tags=['visualization'])
async def submit_application():
    pass

if __name__ == "__main__":
    # import hypercorn
    # hypercorn.run(app.main, host="0.0.0.0", port=8000)

    import uvicorn
    uvicorn.run(app.main, host='0.0.0.0', port=8000)