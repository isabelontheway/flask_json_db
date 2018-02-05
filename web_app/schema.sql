drop table if exists students;
create table students (
    id integer primary key autoincrement,
    name text not null,
    age integer not null
);