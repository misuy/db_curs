/* DDL */

create type sex_enum as enum ('male', 'female', 'other');
create type goal_enum as enum ('work', 'study', 'science', 'relationship', 'friendship');
create type reaction_type_enum as enum ('like', 'skip');

drop table if exists service_user cascade;
create table service_user (
	id serial primary key,
	created timestamp,
	active boolean not null,
	reactions_from int not null check (reactions_from >= 0),
	reactions_to int not null check (reactions_to >= 0)
);

drop table if exists profile cascade;
create table profile (
	id serial primary key,
	user_id int unique not null references service_user (id),
	name varchar(64) not null,
	age int check (age > 0),
	sex sex_enum,
	country varchar(64),
	city varchar(64),
	about text,
	goal goal_enum not null,
	modified timestamp
);

drop table if exists image cascade;
create table image (
	id serial primary key,
	profile_id int not null references profile (id),
	file_path varchar(256) not null,
	uploaded timestamp
);

drop table if exists reaction cascade;
create table reaction (
	id serial primary key,
	from_id int not null references service_user (id),
	to_id int not null references service_user (id),
	type reaction_type_enum not null,
	at timestamp
);

drop table if exists area_of_interest cascade;
create table area_of_interest (
	id serial primary key,
	name varchar(64) not null
);

drop table if exists interest cascade;
create table interest (
	id serial primary key,
	area_id int not null references area_of_interest (id),
	name varchar(64) not null,
	created timestamp
);

drop table if exists profile_interest_relation cascade;
create table profile_interest_relation (
	profile_id int references profile (id),
	interest_id int references interest (id),
	primary key (profile_id, interest_id)
);

drop table if exists university cascade;
create table university (
	id serial primary key,
	name varchar(64) not null,
	country varchar(64),
	city varchar(64)
);

drop table if exists faculty cascade;
create table faculty (
	id serial primary key,
	university_id int not null references university (id),
	name varchar(64) not null
);

drop table if exists field_of_study cascade;
create table field_of_study (
	id serial primary key,
	faculty_id int not null references faculty (id),
	profile_id int references profile (id),
	name varchar(64) not null,
	year int check (year > 0)
);
