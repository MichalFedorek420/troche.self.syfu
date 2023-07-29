import csv
import mysql.connector

with mysql.connector.connect(user='sql7635727', password='qc4yj4GflZ', host='sql7.freemysqlhosting.net', database='sql7635727') as connection:
    cursor = connection.cursor()


    with open ('cities.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                previous_position = int(row['2021'])
            except:
                previous_position = 0
            sql = f"""INSERT INTO
            City(name, country, position, previous_position)
            VALUES('{row['City']}', '{row['Country']}', {int(row['2022'])}, {previous_position})
            """
            cursor.execute(sql)
        connection.commit()

# Server: sql7.freemysqlhosting.net
# Name: sql7635727
# Username: sql7635727
# Password: qc4yj4GflZ
# Port number: 3306
