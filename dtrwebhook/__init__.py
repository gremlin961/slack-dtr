# Import Flask and all the API endpoints for the dtrwebhook application

from flask import Flask
from dtrwebhook.main.controllers import main
from dtrwebhook.addmanifest.controllers import addmanifest
from dtrwebhook.delete.controllers import delete
from dtrwebhook.delmanifest.controllers import delmanifest
from dtrwebhook.promote.controllers import promote
from dtrwebhook.push.controllers import push
from dtrwebhook.scan.controllers import scan
from dtrwebhook.scanfail.controllers import scanfail

app = Flask(__name__)

# Regiser all the api endpoints for the application and define the associated URL prefix 
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(addmanifest, url_prefix='/addmanifest')
app.register_blueprint(delete, url_prefix='/delete')
app.register_blueprint(delmanifest, url_prefix='/delmanifest')
app.register_blueprint(promote, url_prefix='/promote')
app.register_blueprint(push, url_prefix='/push')
app.register_blueprint(scan, url_prefix='/scan')
app.register_blueprint(scanfail, url_prefix='/scanfail')
