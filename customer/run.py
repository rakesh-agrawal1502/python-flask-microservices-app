from flask import Flask
from flask import render_template

from controllers import customer

application = Flask( __name__ )

# enable CORS
# CORS( app )

# set config
# app_settings = os.getenv( 'APP_SETTINGS' )
# app.config.from_object( app_settings )

application.config.from_object( 'config' )

# export YOURAPPLICATION_SETTINGS=/path/to/settings.cfg
# app.config.from_envvar('YOURAPPLICATION_SETTINGS')
# print("======================", application.config["DEBUG"] )

application.register_blueprint( customer )

if __name__ == "__main__":
    application.run( host='0.0.0.0', debug=True )
