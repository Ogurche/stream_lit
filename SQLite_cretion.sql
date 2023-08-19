-- SQLite
PRAGMA foreign_keys= ON;

CREATE TABLE IF NOT EXISTS unit (
    id INTEGER PRIMARY KEY
    , unit_name varchar(100) NOT NULL); 

INSERT INTO unit (unit_name) VALUES ('Снабжение'), ('Инженерное подразделение'), ('Поддержка');

CREATE TABLE IF NOT EXISTS user (
     id INTEGER PRIMARY KEY 
    , "name" varchar(50) NOT NULL
    , surname varchar(50) NOT NULL
    , patronimic varchar(50) 
    , unit int 
    , CONSTRAINT unit_fk FOREIGN KEY (unit) REFERENCES unit(id)) ;
                                                                                         
INSERT INTO user ("name", surname, patronimic, unit)
VALUES 
("Смирнов","Алексей","Макарович",2)
,("Моргунов","Евгений", "Александрович", 3)
,("Вицин", "Георгий", "Михайлович", 2)
,("Никулин", "Юрий","Владимирович", 1) ;

CREATE TABLE IF NOT EXISTS server_num (
    id INTEGER PRIMARY KEY
    , "№ розетки" int 
    , "№ порта розетки" int
    , "№ порта на патчпанели" int
    , "Длина" decimal (10,2)
);

INSERT INTO server_num( "№ розетки","№ порта розетки","№ порта на патчпанели","Длина"  )
VALUES 
(12, 5402,663,12.52), (11, 1403,6363,122.52),(121, 5453,772,10),(213, 5401,6213,12234);

CREATE TABLE IF NOT EXISTS arm (
    id INTEGER PRIMARY KEY
    , arm_name varchar(100)
    , ip_arm varchar(20)
    , mac_arm varchar(20)
);

INSERT INTO arm (arm_name, ip_arm, mac_arm)
VALUES
    ("АРМ 1", '12.443.645.75', 'MA12356S') 
,   ("АРМ 2", '13.123.245.23', 'QS11246D')
,   ("АРМ 3", '12.532.721.12', 'RV13256S');

CREATE TABLE IF NOT EXISTS accounting(
    id INTEGER PRIMARY KEY
    , server_num_id INT
    , user_id INT
    , arm_id INT
    , create_datetime datetime DEFAULT CURRENT_TIMESTAMP 
    , FOREIGN KEY (server_num_id) REFERENCES server_num(id)
    , FOREIGN KEY (user_id) REFERENCES user(id) 
    , FOREIGN KEY (arm_id) REFERENCES arm(id)
); 

INSERT INTO accounting (server_num_id,user_id,arm_id) 
VALUES 
    (1,2,3),(3,1,2),(4,4,1);
