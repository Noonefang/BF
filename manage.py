# !/usr/bin/env python
import os
from app import app_create

app = app_create(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run()