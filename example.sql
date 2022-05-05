/*delete table */
drop table students;

/*creating table named students */
create table students(
    id number(30) not null,
    regno varchar2(30) not null,
    firstname varchar2(30) not null
 );
    
select * from students;
   
show tables;
describe students;

/*to add, a column to existing table*/
alter table students add lastname VARCHAR2(30);
describe students;

alter table students add course varchar(30);
describe students;
/*to delete column*/
ALTER TABLE students DROP COLUMN course;
describe students;

alter table students add balance number(7,2);
describe students;

/*to modify table*/
alter table students modify balance number(10,2);
describe students;

alter table students add newbalance number(10,2);
describe students;

alter table students add course varchar(30);
describe students;

/*inserting records*/
insert all 
into students (id, regno, firstname, lastname, course, balance) values (200, 'cs/mg/1145/09/19', 'Jane', 'Walker', 'cs', '4500.00')
into students (id, regno, firstname, lastname, course, balance) values(201, 'cs/mg/1142/09/19', 'Ruth', 'Marshall', 'bsc', '1500.00')
into students (id, regno, firstname, lastname, course, balance) values(202, 'bbit/mg/1175/09/19', 'Hanna', 'Marin', 'tlc', '300.00')
into students (id, regno, firstname, lastname, course, balance) values(203, 'bbit/mg/1156/09/19', 'Emily', 'Mandy', 'bsc', '5000.00')
into students (id, regno, firstname, lastname, course, balance) values(204, 'cs/mg/1183/09/19', 'Spencer', 'Hastings', 'cs', '2000.00')
into students (id, regno, firstname, lastname, course, balance) values(205, 'bbit/mg/2070/09/19', 'Alison', 'Parker', 'tlc', '34000.00')
into students (id, regno, firstname, lastname, course, balance) values(206, 'tlc/mg/2176/09/19', 'Peter', 'Colt', 'bsc', '30000.00')
into students (id, regno, firstname, lastname, course, balance) values(207, 'cs/mg/1111/09/19', 'John', 'Caine', 'tlc', '4000.00')
into students (id, regno, firstname, lastname, course, balance) values(208, 'tlc/mg/2003/09/19', 'Grace', 'Toner', 'cs', '9500.00')
into students (id, regno, firstname, lastname, course, balance) values(209, 'cs/mg/1273/09/19', 'Ralph', 'Adele', 'cs', '1200.00')
into students (id, regno, firstname, lastname, course, balance) values(210, 'cs/mg/1573/09/19', 'Aria', 'Montgomery', 'tlc', '600.00')
into students (id, regno, firstname, lastname, course, balance) values(211, 'bbit/mg/2473/09/19', 'Bill', 'Morgan', 'cs', '450.00')
into students (id, regno, firstname, lastname, course, balance) values(212, 'cs/mg/1109/09/19', 'Harry', 'Harrison', 'cs', '650.00')
into students (id, regno, firstname, lastname, course, balance) values(213, 'tlc/mg/3410/09/19', 'Temperance', 'Brennan', 'bsc', '800.00')
into students (id, regno, firstname, lastname, course, balance) values(214, 'cs/mg/5690/09/19', 'Seeley', 'Booth', 'cs', '100.00')
into students (id, regno, firstname, lastname, course, balance) values(215, 'tlc/mg/4536/09/19', 'Lance', 'Sweets', 'bsc', '550.00')
into students (id, regno, firstname, lastname, course, balance) values(216, 'tlc/mg/2356/09/19', 'Angela', 'Pookin', 'tlc', '20000.00')
into students (id, regno, firstname, lastname, course, balance) values(217, 'cs/mg/6723/09/19', 'Mary', 'Raferty', 'cs', '50000.00')
into students (id, regno, firstname, lastname, course, balance) values(218, 'tlc/mg/4501/09/19', 'Ashley', 'Palmer', 'cs', '30500.00')
into students (id, regno, firstname, lastname, course, balance) values(219, 'bbit/mg/6908/09/19', 'Madea', 'Mabelson', 'cs', '900.00')
into students (id, regno, firstname, lastname, course, balance) values(220, 'cs/mg/2371/09/19', 'Jennifer', 'Simms', 'bsc', '2000.00')
select * from dual; 

select * from students;
describe students;

select * from students;
    UPDATE students SET newbalance = balance * 0.95;
    
select * from students;
update students
set newbalance = balance *0.45
where firstname like '%a';

select * FROM students;
/*alter table students add fullname varchar2(20);
describe students;*/
select concat(firstname, concat(' ', lastname)) from students;
update students set fullname=concat(firstname, concat(' ', lastname));

SELECT * FROM students;   
alter table students add phone varchar(30);
update students set phone = '0712345678' where ROWNUM = 1;

SELECT * FROM students;
select CONCAT('+254', SUBSTR(phone, 2,9)) FROM students;
update students set phone = CONCAT('+254', SUBSTR(phone, 2,9));

/*
string	Required. The string to extract from
start	Required. The start position. Can be both a positive or negative number. If it is a positive number, this function extracts from the beginning of the string. If it is a negative number, this function extracts from the end of the string
length	Optional. The number of characters to extract. If omitted, the whole string will be returned (from the start position)
*/
SELECT * FROM students;
select upper(substr(lastname, 2, 5)) from students; 

SELECT * FROM students;
select upper(substr(lastname, -2, 5)) from students; 

/*returns the last day of the month of a given date*/ 
select last_day('01 feb 2022') from dual;

/*returns next day of a given date*/
select next_day('01 march 2022', 'fri') from dual;

/*returns current date*/
select SYSDATE FROM DUAL;

/*returns current date, last date and the number of days between the months*/
select SYSDATE,
       LAST_DAY(SYSDATE) "Last",
       LAST_DAY(SYSDATE) - SYSDATE "Days Left"
  FROM DUAL;
/*returns number of months between current day and the given date*/
select MONTHS_BETWEEN (sysdate, '01 jan 2000')FROM DUAL;

/*returns number of weeks between current day and the given date*/       
select MONTHS_BETWEEN (sysdate, '01 jan 2000')* 4 FROM DUAL;


create table student_bio(
    regno varchar2(30) not null,
    name varchar2(30) not null,
    feebalance number(7,2) not null
    );
    
create table student_fees(
    regno varchar2(30) not null,
    particulars number(12,2) not null,
    amount number(12,2) not null
);

drop table student_fees
drop table student_bio

create trigger fee_balancetrigger
    BEFORE INSERT
    ON student_fees
    FOR EACH ROW
    BEGIN
        UPDATE student_bio a INNER JOIN student_fees b ON a.regno=b.regno 
        SET a.feebalance=(100000-sum(b.amount)) GROUP BY b.regno
    END;


