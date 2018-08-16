import sqlite3

def connect():
    conn=sqlite3.connect("onsiteplans.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS onsite (id INTEGER PRIMARY KEY, status text, country text, city text, startdate text, enddate text, \
                team text, name text, maintask text, address text, telno text)")
    conn.commit()
    conn.close()

def insert(id,status,country,city,startdate,enddate,team,name,maintask,address,telno):
    conn=sqlite3.connect("onsiteplans.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO onsite VALUES (?,?,?,?,?,?,?,?,?,?,?)",(id,status,country,city,startdate,enddate,team,name,maintask,address,telno))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("onsiteplans.db")
    cur=conn.cursor()
    #cur.execute("SELECT * FROM onsite")
    cur.execute("SELECT * FROM onsite ORDER BY enddate DESC")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="",team=""):
    conn=sqlite3.connect("onsiteplans.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM onsite WHERE name=? OR team=?", (name,team))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("onsiteplans.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM onsite WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,status,country,city,startdate,enddate,team,name,maintask,address,telno):
    conn=sqlite3.connect("onsiteplans.db")
    cur=conn.cursor()
    cur.execute("UPDATE onsite SET status=?, country=?, city=?, startdate=?, enddate=?, team=?, name=?, maintask=?, address=?, telno=? WHERE id=?"\
    ,(status,country,city,startdate,enddate,team,name,maintask,address,telno,id))
    
    conn.commit()
    conn.close()

connect()
#insert(599710,"Ongoing","USA","San Francisco","05282018","05292018","AIT CT2","Mavis","Walleye Premium VVM","HYATT HOUSE SANTA CLARA","650-524-1870")
#insert(599690,"Ongoing","USA","San Francisco","07192018","08242018","AIT CT1","Joanne","OMA/DM/FOTA Marlin/Sailfish/Walleye/B1/C1 customer report test","HYATT HOUSE SANTA CLARA 3915 RIVERMARK PLAZA","650-214-7324")
#insert(599695,"Ongoing","Japan","San Tokyo","07152018","08042018","AIT CT1","Angela","H2 Mobile Felica Certification and H4 Service Providor Certification","Remm Roppongi","N/A")
#print(search("Joanni","AIT CT1"))
#print(view())
#update(599710,"Done","USA","San Francisco","05282018","05292018","AIT CT2","Mavis","Walleye Premium VVM","HYATT HOUSE SANTA CLARA 3915 RIVERMARK PLAZA","650-524-1870")
#delete(599685)
#print(view())

#insert("The Sun","John Smith",1918,913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(author="John Smooth"))
