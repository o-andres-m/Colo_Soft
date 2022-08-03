"""Load configuration from .ini file."""
import configparser

# Read local `config.ini` file:
config = configparser.ConfigParser()
config.read('config.ini')

# If not exist, create it with default values:
if not config.sections():
    config['DATABASE'] = {  'HOST' : 'localhost',
                            'PORT' : '3306',
                            'USERNAME' : 'root',
                            'PASSWORD' : '',
                            'DB' : 'colo_soft'
                        }
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
