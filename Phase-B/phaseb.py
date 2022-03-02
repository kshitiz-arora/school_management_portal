import random
def make_actors(file_name):
    num = 300000
    f = open('C:/Coding/dbms_b/'+file_name,'w')
    f.write('drop table if exists actor;\n')
    f.write('create table actor(a_id int PRIMARY KEY, name char(15));\n')
    for i in range(num):
        s = '\''
        for j in range(15):
            x = random.randint(0,25)
            s+=chr(ord('a')+x)
        s+='\''
        f.write('insert into actor values('+str(i+1)+','+s+');\n')
        

def make_production_company(file_name):
    num = 80000
    f = open('C:/Coding/dbms_b/'+file_name,'w')
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
        
def make_casting(file_name):
    f = open('C:/Coding/dbms_b/'+file_name,'w')
    f.write('drop table if exists casting;\n')
    f.write('create table casting(m_id int, a_id int, PRIMARY KEY (m_id,a_id), FOREIGN KEY (a_id) REFERENCES actor(a_id), FOREIGN KEY (m_id) REFERENCES movie(m_id));\n')
    cnt = 0
    for i in range(1000000):
        s = '\''
        l = []
        while(len(l)<4):
            x = random.randint(1,300000)
            
            if x>1000 and cnt == 200000:
                x = random.randint(1,1000)
            
            if x in l:
                continue
            
            if x>1000:
                cnt+=1
                
            l.append(x)
        for j in l:
            f.write('insert into casting values(' + str(i+1) + ',' + str(j) + ');\n')
     
def make_movie(file_name):

    num = 1000000
    more = num/20
    less = num - (num/20)
    table = 'movie'
    
    f = open('C:/Coding/dbms_b/'+file_name,'w')
    
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

        imdb = float(random.randint(0,50)/10)
        if more == 0 and less > 0:
            imdb = float(random.randint(0,20))/10
        if less == 0 and more > 0:
            imdb = float(random.randint(21,50))/10
        if imdb > 2:
            more-=1
        else:
            less-=1

        pc_id = random.randint(1, 80000)

        f.write('insert into %s values(%d, %s, %d, %0.1f, %d);\n' % (table, i+1, name, year, imdb, pc_id))

    f.close()
make_actors('actor_table.sql')
make_production_company('production_company.sql')
make_movie('movie.sql')
make_casting('casting.sql')
