create database pcp;
use pcp;
create table users(id int,pass varchar(20) default '',username varchar(20),grade int);
insert into users(id,username,grade) VALUES(1,"user1",124);
insert into users(id,username,grade) VALUES(1,"user2",125);
insert into users(id,username,grade) VALUES(1,"mukade",123);
insert into users(id,username,grade) VALUES(1,"OB",120);