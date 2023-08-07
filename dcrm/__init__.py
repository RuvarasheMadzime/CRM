import pymysql

pymysql.version_info = (2, 1, 0, "final", 0)  # Set the PyMySQL version to mimic mysqlclient
pymysql.install_as_MySQLdb()