from flask import Flask
from flask import render_template

from controllers import invoice

application = Flask( __name__ )

application.config.from_object( 'config' )

# export YOURAPPLICATION_SETTINGS=/path/to/settings.cfg
# app.config.from_envvar('YOURAPPLICATION_SETTINGS')
# print("======================", application.config["DEBUG"] )

application.register_blueprint( invoice )

if __name__ == "__main__":
    application.run( host='0.0.0.0', debug=True )
