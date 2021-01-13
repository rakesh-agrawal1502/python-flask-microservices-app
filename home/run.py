from flask import Flask
from flask import render_template

from controllers import home

application = Flask( __name__ )

application.config.from_object( 'config' )

application.register_blueprint( home )

if __name__ == "__main__":
    application.run( host='0.0.0.0', debug=True )
