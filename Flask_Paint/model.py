import sqlite3
import json

class models():
    def inset(self,di,name):
        con = sqlite3.connect('img.db')
        con.execute("INSERT INTO images(NAME,SHAPE,X,Y,MX,MY,COLOR,SIZE) \
                VALUES(?,?,?,?,?,?,?,?)",(name,di["shape"],di["x"],di["y"],di["mx"],di["my"],di["color"],di["size"]));
        con.commit()
      
        con.close()
    def ret(self):
        l=[]
        con = sqlite3.connect('img.db')
        b=con.execute('SELECT NAME FROM images')
        for each in b:
            if each[0] in l:
                pass
            else:
                l.append(each[0])
        return l
    def retf(self,s):
        l=[]
       
        con = sqlite3.connect('img.db')
        b=con.execute('SELECT * FROM images where name=?',(s,))
        for each in b:
                l.append(each)
 
        return l
