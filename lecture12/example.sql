
create table "user" (
    id bigint primary key,
    name VARCHAR(50),
    surname VARCHAR(70),
    phone varchar(15),
    email varchar(50)
);

-- CRUD
-- CREATE
-- READ
-- UPDATE
-- DELETE

SELECT * FROM "user";

INSERT INTO "user" (name, surname, phone, email, country, city, street, ) VALUES
  ('Stas', 'dumi', '21432', 'dnfl@gmail.com', 'Ukraine'),
  ('Igor', 'Ivanov', '245213', 'igor@gmail.com', 'Ukraine'),
  ('Andrew', 'Rsdf', '90345', 'andrew@gmail.com'),
  ('Anton', 'Hbihsdd', '134', 'anton@gmail.com')
 ;


CREATE TABLE Country (
    id serial primary key,
    name varchar(50) not null,
    unicode varchar(2) not null
);

Create table City (
    id serial primary key,
    name varchar(70) not null,
    postal_code varchar(10),
    country_id integer,
    constraint country_foreign_key FOREIGN KEY (country_id) REFERENCES Country(id)
);

create table address (
    id serial primary key ,
    city_id integer,
    street varchar(150),
    postal_code varchar(10),
    constraint city_foreign_key FOREIGN KEY (city_id) REFERENCES city(id)
);

alter table "user"
add column address_id int;
alter table "user"
add constraint address_foreign_key Foreign Key (address_id) references address(id);

select
    c.name as city,
    count(*) as count
from "user" u
join address a on u.address_id = a.id
join city c on a.city_id = c.id
join country c2 on c.country_id = c2.id
where u.name like '%ta%'
GROUP BY c.name
HAVING count(*) > 1;