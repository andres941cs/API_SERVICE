from app import create_app
import argparse
# import datetime
# from json import loads,dumps
# import os

app = create_app()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', help='Activates debug mode, require value port', action="store_true" , required=False)
    parser.add_argument('-p', help='Port number for the webservice', type=int, default=3000, required=False)
    args = parser.parse_args()
    
    with app.app_context():
        app.run(host='0.0.0.0', port=args.p , debug=args.d)