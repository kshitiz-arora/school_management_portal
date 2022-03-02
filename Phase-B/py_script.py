import random

def make_movies(file_name):

    num = 1000000
    cap = num/20
    count = 0
    table = 'movie'
    
    f = open('D:/WORK/Sem5/CS301 Databases/Phase-B/'+file_name,'w')
    
    f.write('drop table if exists %s;\n' % (table))
    
    f.write('create table %s (m_id int PRIMARY KEY, name char(10), year int, imdb numeric(2,1), pc_id int, \n\
    constraint fk_pc foreign key(pc_id) references production_company(pc_id));\n' % (table))

    for i in range(num):
        name = '\''
        for j in range(10):
            x = random.randint(0,25)
            name+=chr(ord('a')+x)
        name+='\''

        year = random.randint(1900,2000)

        imdb = random.randint(0,50)/10


        pc_id = random.randint(1, 80000)

        f.write('insert into %s values(%d, %s, %d, %d, %d);\n' % (table, i+1, name, year, imdb, pc_id))

    f.close()

def make_production_company(file_name):
    num = 80000
    f = open('D:/WORK/Sem5/CS301 Databases/Phase-B/'+file_name,'w')
    f.write('drop table if exists production_company;\n')
    f.write('create table production_company(pc_id int PRIMARY KEY, name char(10), address char(30));\n')
    for i in range(num):
        name = '\''
        for j in range(10):
            x = random.randint(0,25)
            name+=chr(ord('a')+x)
        name+='\''
        
        address = '\''
        for j in range(30):
            x = random.randint(0,25)
            address+=chr(ord('a')+x)
        address+='\''
        f.write('insert into production_company values('+str(i+1)+','+name+','+address+');\n')

# make_production_company('pc_table.sql')
make_movies('movies_table.sql')