import pymysql

class Config():
    """File 'config.txt' have the conection settings
    if file does not exist, the class creat it with default settings.
    1) method get_conection_config returns a list [host,port,usr,passw,db]
    2) metod set_conection_config recieves the conection settings and
    save the file the new settings.
    """
    def __init__(self) -> None:
        try:
            file = open('config.txt','r')
            self.data = file.readlines()
            if not self.data:
                file = open('config.txt', 'w')
                file.write('host=localhost\nport=3306\nusr=admin\npassw=\ndb=colo_soft')
        except:
            try:
                file = open('config.txt', 'w')
                file.write('host=localhost\nport=3306\nusr=admin\npassw=\ndb=colo_soft')
            except:
                print ('Error, no se pudo obtener ni crear el archivo de configuracion.')
    
    def get_conection_config(self):
        host = self.data[0][5:-1]
        port=self.data[1][5:-1]
        usr= self.data[2][4:-1]
        passw= self.data[3][6:-1]
        db= self.data[4][3:]
        config_list = [host,port,usr,passw,db]
        return config_list

    def set_conection_config(self,host,port,usr,password,db):
        try:
            file = open('config.txt', 'w')
            file.write(f'host={host}\nport={port}\nusr={usr}\npassw={password}\ndb={db}')
        except:
            print ('Error, no se pudo modificar la configuracion.')

class Conection():
    """Get the conection settings from class Config and set "connect_data"
    - method conection try to:
    1) conect to the db with connect_data
    2) create necesaries tables
    3) return a tuple with the conection and cursor
    """
    connect_data = Config().get_conection_config()
    def conection(self):
        try:
            conn =pymysql.connect(host=self.connect_data[0],
                                  port=int(self.connect_data[1]),
                                  user=self.connect_data[2],
                                  passwd=self.connect_data[3],
                                  db=self.connect_data[4]
                                  )
            cursor=conn.cursor()
            try:
                cursor.execute("""CREATE TABLE register (
                        id INT AUTO_INCREMENT, 
                        item TEXT,
                        value FLOAT,
                        date TEXT,
                        observations TEXT,
                        PRIMARY KEY (id))""")
                cursor.execute("""CREATE TABLE items (
                        id INT AUTO_INCREMENT, 
                        item TEXT,
                        PRIMARY KEY (id))""")
            except:
                pass
                #print('Tablas ya creadas')
        except:
            print ('Error al conectar a la DB.')

        else:
            return conn,cursor