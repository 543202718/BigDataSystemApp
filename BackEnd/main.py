from flask_cors import CORS
from app import app
import author
import AVDU_import
import AVDU_search
import AVDU_detail

if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(host='0.0.0.0')
