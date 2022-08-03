import pymysql
import configparser

class Config():
    """File 'config.ini' have the conection settings
    if file does not exist, the class creat it with default settings.

    Metod set_conection_config recieves the conection settings and
    save the file with the new settings.
    """
    def __init__(self) -> None:
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

        self.host=  config['DATABASE']['HOST']
        self.port=  config['DATABASE']['PORT']
        self.user=  config['DATABASE']['USERNAME']
        self.passw= config['DATABASE']['PASSWORD']
        self.db=    config['DATABASE']['DB']

    def set_conection_config(self,host,port,usr,password,db):
        config = configparser.ConfigParser()
        config['DATABASE'] = {  'HOST' : host,
                                'PORT' : port,
                                'USERNAME' : usr,
                                'PASSWORD' : password,
                                'DB' : db
                                }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

class Conection():
    """Get the conection settings from class Config and set "connect_data"
    - method conection try to:
    1) conect to the db with connect_data
    2) create the cursor
    3) create necesaries tables

    """
    connect_data = Config()
    def conection(self) -> None:
        try:
            self.conn =pymysql.connect( host=     self.connect_data.host,
                                        port=     int(self.connect_data.port),
                                        user=     self.connect_data.user,
                                        passwd=   self.connect_data.passw,
                                        db=       self.connect_data.db
                                        )
            self.cursor=self.conn.cursor()
            try:
                mysql_table_register = """CREATE TABLE register (
                        id INT AUTO_INCREMENT, 
                        item TEXT,
                        value FLOAT,
                        date TEXT,
                        observations TEXT,
                        PRIMARY KEY (id))"""
                self.cursor.execute(mysql_table_register)
                mysql_table_items ="""CREATE TABLE items (
                        id INT AUTO_INCREMENT, 
                        item TEXT,
                        PRIMARY KEY (id))""" 
                self.cursor.execute(mysql_table_items)
            except:
                pass
        except:
            return False