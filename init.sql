drop database if exists cmdb;
create database cmdb;
use cmdb;
drop table if exists user;


Create table user(
	id int not null auto_increment primary key,
	name varchar(200),
	password varchar(200)
);