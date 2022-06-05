import os


basedir = os.path.abspath(os.path.dirname(__file__))
#SQLALCHEMY_DATABASE_URI = 'mysql://root:9173194253qQ@192.168.43.246/db'
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
MEDIA_SERVER_ADDRESS = 'http://thefir.ddns.net'
