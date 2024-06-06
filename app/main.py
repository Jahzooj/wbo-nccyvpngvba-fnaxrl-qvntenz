from fastapi import Depends, HTTPException

from app.app import app
from app.database import get_db
from app.models import Application
from app.schemas import ApplicationBase, ApplicationCreate
from app.config import logger

@app.get('/status/', tags=['utility'])
async def status():
    return {'message': '200-ok'}


@app.post('/submit-application/', tags=['application'])
async def submit_application(submitted: ApplicationCreate, db=Depends(get_db)) -> ApplicationBase:
    try:
        data = submitted.dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f'invalid data: {e}')
    new_application = Application(**data)
    
    db.add(new_application)
    db.commit()
    return data


@app.post('/update-application/{app_name}', tags=['application'])
async def update_application(app_name: str, to_update: ApplicationCreate, db=Depends(get_db)) -> ApplicationBase:
    try:
        data = to_update.dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f'Invalid data: {e}')
    
    submitted = db.query(Application).filter(Application.name == app_name).first()
    if not submitted:
        raise HTTPException(status_code=404, detail=f'application not found')

    update_data = to_update.dict(exclude_unset=True)

    for key, value in update_data.items():
        if update_data[key] != getattr(submitted, key):
            setattr(submitted, key, value)
    db.commit()
    db.refresh(submitted)

    return data


@app.get('/check-application/{app_name}', tags=['application'])
async def check_application(app_name: str, db=Depends(get_db)) -> ApplicationBase:
    application = db.query(Application).filter(Application.name == app_name).first()
    if not application:
        raise HTTPException(status=404, detail=f'application not found')
    
    return ApplicationBase.from_orm(application)


@app.delete('/delete-application/{app_name}', tags=['application'])
async def check_application(app_name: str, db=Depends(get_db)):
    application = db.query(Application).filter(Application.name == app_name).first()
    if not application:
        raise HTTPException(status_code=404, detail=f'application not found')
    
    db.delete(application)
    db.commit()


@app.get('/build-report-sankey/', tags=['visualization'])
async def submit_application():
    pass

if __name__ == "__main__":
    # import hypercorn
    # hypercorn.run(app.main, host="0.0.0.0", port=8000)

    import uvicorn
    uvicorn.run(app.main, host='0.0.0.0', port=8000)