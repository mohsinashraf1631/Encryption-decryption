import MySQLdb
#if it gives an error then first download MySQL module
conn=MySQLdb.connect(host='localhost',user='',passwd='',db='test')
import mysql.connector
from mysql.connector.cursor import MySQLCursor
cnx = mysql.connector.connect(database='test')
cursor = MySQLCursor(cnx)
sentence=raw_input("Enter a sentence:")
salt_number=input("Enter a number:")
salt_binary=bin(salt_number)
salt_binary=salt_binary[2:].zfill(8)
print "salt binary="+salt_binary
b_variable=""
result_sentence=""
for i in range(len(sentence)):
    binary=bin(ord(sentence[i]))
    binary=binary[2:].zfill(8)
    print "binary="+binary
    a=0
    s_variable=""
    while a<len(binary):
        result=binary[a]
        result=str(int(result)^int(salt_binary[a]))
        print "result="+result
        s_variable=s_variable+str(result)
        a+=1
    number_loop=int(s_variable,2)
    print "number="+str(number_loop)
    character=chr(number_loop).encode('utf8')
    print "character=",character
    result_sentence+=character
result=result_sentence
cursor.execute('INSERT INTO encrypted_text(encryted_phrase) VALUES(\'' + result + '\')')
cursor.execute('commit')
