from app.app import app

@app.get('/status/', tags=['utility'])
async def status():
    return {'message': '200-ok'}

@app.post('/submit-application/', tags=['application'])
async def submit_application(
    
):
    pass

@app.get('/check-application/', tags=['application'])
async def submit_application():
    pass

@app.get('/build-report-sankey/', tags=['visualization'])
async def submit_application():
    pass