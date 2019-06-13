# -*- encoding: utf-8 -*-

from app.app import create_app

app = create_app('settings.py')

if __name__ == "__main__":
    app.run()