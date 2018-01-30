import MySQLdb
conn=MySQLdb.connect(host='localhost',user='',passwd='',db='test')
import mysql.connector
from mysql.connector.cursor import MySQLCursor
cnx = mysql.connector.connect(database='test')
cursor = MySQLCursor(cnx)
cursor.execute('SELECT encryted_phrase FROM encrypted_text')
for row in cursor.fetchall():
    import sys
previous_binary_result =""
salt_number=input("Enter the previous salt number=")
salt_binary=bin(salt_number)
salt_binary=salt_binary[2:].zfill(8)
aa_variable = ""
for character in row[0]:
    number=character.decode('utf8')
    number_result=bin(ord(number))
    previous_binary_result=number_result[2:].zfill(8)
    given_character_value=""
    variable=0
    ascii=""
    while variable<len(previous_binary_result):
        result=int(salt_binary[variable])^int(previous_binary_result[variable])
        variable=variable+1
        given_character_value+=str(result)
        answer=chr(int(given_character_value,2))
    sys.stdout.write(answer)
print aa_variable



    
    
    
    
