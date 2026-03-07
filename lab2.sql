sql 


CREATE TABLE Theaters (
    Name VARCHAR2(50) NOT NULL ,
    City VARCHAR2(50) NOT NULL,
    State VARCHAR2(2) NOT NULL ,
    Zip VARCHAR2(10) NOT NULL ,
    Phone VARCHAR2(15) NOT NULL,
    constraints Theaters_pk primary key(name)
    CONSTRAINT chk_phone 
);

CREATE TABLE movies (
    title VARCHAR2(50) NOT NULL,
    rating INT NOT NULL ,
    length INT NOT NULL,
    RealeaseDate DATE NOT NULL,
    primary key (title),
    constraints check_length 
    constraints check_rating check(rating BETWEEN 0 and 10),
    CONSTRAINT chk_RealeaseDate 
   CHECK (RealeaseDate  > TO_DATE('1900-Jan-01', 'yyyy-Mon-dd'))
);



CREATE TABLE ShownAt(
    TheaterName VARCHAR2(50) NOT NULL,
    MovieTitle VARCHAR2(50) NOT NULL,
    constraints ShownAt_pk primary key (TheaterName,MovieTitle ),
    foreign key (TheaterName) references Theaters(name),
    foreign key (MovieTitle) references movies(title),
);

INSERT INTO Theaters('Name','City','State','Zip','Phone') VALUES('Great Escape 14','Wilder','KY',41076,8594420000);
INSERT INTO Theaters('Name','City','State','Zip','Phone') VALUES('AMC Newport On the Levee 20 ','Newport','KY',41076,888AMC4FUN);
INSERT INTO Theaters('Name','City','State','Zip','Phone') VALUES('Danbarry Dollar Saver Eastgate','Cincinati','OH',45245,5139478111);
INSERT INTO Theaters('Name','City','State','Zip','Phone') VALUES('Danbarry Dollar Cinemas Turfway','Florence','KY',41072,8596472828);
INSERT INTO Theaters('Name','City','State','Zip','Phone') VALUES('Esquire Theatre ','Cincinati','OH',45220,5132818750);
INSERT INTO Theaters('Name','City','State','Zip','Phone') VALUES('Showcase Cinema De Lux Florence','Florence','KY',41042,8003154000);


INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('Big Hero 6','8.5','102','7-Nov-2014');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('Interstellar','9.1','169','7-Nov-2014');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('Gone Girl ','8.5','149','3-Oct-2014');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('Nightcrawler','8.3','117','31-Oct-2014');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('Schindler''s List' ,'8.9','195','4-Feb-1994');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('The Green Mile ' ,'8.5','189','10-Dec-1999');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('Fargo' ,'8.2','98','5-Apr-1996');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('District 9' ,'8.7','112','14-Aug-2009');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('A Perfect Getaway' ,'6.8','97','7-Aug-2009');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('Star Trek' ,'8.4','127','8-May-2009');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('Aliens in the Attic' ,'4.5','86','31-Jul-2009');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('Public Enemies' ,'7.5','140','1-Jul-2009');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('Away We Go' ,'7.5','98','26-Jun-2009');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('The Hurt Locker' ,'8.0','131','10-Oct-2008');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('The Dark Knight ' ,'8.9','152','18-Jul-2008');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('Up' ,'8.7','86','29-May-2009');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('The Departed' ,'8.5','151','6-Oct-2006');
INSERT INTO movies('title','rating','length','RealeaseDate') VALUES('The Pianist' ,'8.5','150','3-Jan-2003');



INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Great Escape 14','Big Hero 6');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Great Escape 14','Interstellar');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Great Escape 14','Gone Girl');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Great Escape 14','Public Enemies');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Great Escape 14','The Departed');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('AMC Newport On The Levee 20','Big Hero 6');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('AMC Newport On The Levee 20','Interstellar');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('AMC Newport On The Levee 20','Gone Girl');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('AMC Newport On The Levee 20','District 9');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('AMC Newport On The Levee 20','A Perfect Getaway');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('AMC Newport On The Levee 20','Away We Go');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('AMC Newport On The Levee 20','Up');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('AMC Newport On The Levee 20','The Departed');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Dabburry Dollar Saver Eastgate','Big Hero 6');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Dabburry Dollar Saver Eastgate','Interstellar');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Dabburry Dollar Saver Eastgate','Gone Girl');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Dabburry Dollar Saver Eastgate','Nightcrawler');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Dabburry Dollar Cinemas Turfway','Nightcrawler');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Dabburry Dollar Cinemas Turfway','The Green Mile');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Dabburry Dollar Cinemas Turfway','District 9 ');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Dabburry Dollar Cinemas Turfway','Star Trek');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Dabburry Dollar Cinemas Turfway','Ailens in the Attic');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Dabburry Dollar Cinemas Turfway','The Hurt Locker');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Dabburry Dollar Cinemas Turfway','The Green Mile');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Esquire Theatre','Interstellar');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Esquire Theatre','Schindler''s List');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Esquire Theatre','Fargo');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Esquire Theatre','The Pianist');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Showcase Cinema De Lux Florence ','Big Hero 6');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Showcase Cinema De Lux Florence ','Interstellar');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Showcase Cinema De Lux Florence ','Gone Girl');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Showcase Cinema De Lux Florence ','District 9');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Showcase Cinema De Lux Florence ','A perfect Getaway');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Showcase Cinema De Lux Florence ','Star Trek');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Showcase Cinema De Lux Florence ','Aliens in the Attic');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Showcase Cinema De Lux Florence ','Away We Go');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Showcase Cinema De Lux Florence ','The Hurt Locker');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Showcase Cinema De Lux Florence ','The Dark Knight');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Showcase Cinema De Lux Florence ','Up');
INSERT INTO ShownAt('TheatreName','MovieTitle')VALUES('Showcase Cinema De Lux Florence ','The Departed');

