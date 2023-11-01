from flask import Flask, request
from flask_cors import CORS
from supabase import create_client

SUPABASE_URL = "https://qrrdskgekikwdmoppowg.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFycmRza2dla2lrd2Rtb3Bwb3dnIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5ODQyMDYyMCwiZXhwIjoyMDEzOTk2NjIwfQ.BeBXSFwmhbcLop9p8ipEHAZfWas0xNcttsapV0C5mUQ"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    response = supabase.table("BlogTable").select("title", "genre","id").execute()
    return dict(response)['data']

@app.route('/getBlog', methods=['POST'])
def getBlog():
    req = request.json #id incomming from frontend and stored in req
    try:
        response = supabase.table("BlogTable").select("*").eq("id",req["id"]).execute()
        return dict(response)['data'], 200
    except:
        return "Bad Request", 400
        

@app.route('/addBlog', methods=['POST'])
def addBlog():
    req = request.json
    try:
        data = supabase.table("BlogTable").insert(req).execute()
        return dict(data)['data'], 200
    except:
        return "Bad Request", 400


if __name__ == "__main__":
    app.run(debug = True)   