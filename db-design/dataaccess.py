from var import Var
from db import DB

class DataAccess:

    # DONE
    def save_sensor_data(self, ax, ay, az):
        query = "INSERT INTO sensor ( ax, ay, az " \
                ") VALUES ( %s, %s, %s ) "
        data = (str(ax), str(ay), str(az))
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        db.update(query, data)

    # DONE
    def get_sensor_data(self):
        query = "SELECT * FROM sensor"
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

if __name__ == "__main__":

    da = DataAccess()
    da.save_sensor_data(1, 1, 1)
    r = da.get_sensor_data()
    print(r)

