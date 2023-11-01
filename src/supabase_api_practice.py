from flask import Flask, request
from flask_cors import CORS
from supabase import create_client


SUPABASE_URL = "https://qrrdskgekikwdmoppowg.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFycmRza2dla2lrd2Rtb3Bwb3dnIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5ODQyMDYyMCwiZXhwIjoyMDEzOTk2NjIwfQ.BeBXSFwmhbcLop9p8ipEHAZfWas0xNcttsapV0C5mUQ"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def func():
    return "Hello!"

@app.route('/getGames', methods = ['GET'])
def getGames():
    data = supabase.table("Games").select("*").execute()
    return dict(data)['data']

@app.route('/addGame', methods = ['post'])
def addGame():
    req = request.json

    if 'name' in req and req['name']:
        payload = {'name': req['name']}
        data = supabase.table("Games").insert(payload).execute()

        return  dict(data)['data'], 200
    else:
        return "Bad Request", 400

if __name__ == "__main__":
    app.run(debug = True)
