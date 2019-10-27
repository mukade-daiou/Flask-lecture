create database pcp;
use pcp;
create table users(id int,pass varchar(20) default '',username varchar(20),grade int);
insert into users(id,username,grade) VALUES(1,"user1",124);
insert into users(id,username,grade) VALUES(2,"user2",125);
insert into users(id,username,grade) VALUES(3,"mukade",123);
insert into users(id,username,grade) VALUES(4,"OB",120);