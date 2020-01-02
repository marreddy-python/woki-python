import os

from src.app import create_app

if __name__ == '__main__':
    print('RUN FILE CALLED')
    env_name = os.getenv('FLASK_ENV')
    app = create_app(env_name)
    # app.run(host='192.168.1.3',port=5000)
    app.run()

