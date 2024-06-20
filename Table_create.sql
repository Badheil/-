CREATE TABLE IF NOT EXISTS salaries(
   employee VARCHAR(5)
  ,salary   INT
  ,date     DATE
);
INSERT INTO salaries(employee,salary,date) VALUES ('tom','2342','2023-01-14');
INSERT INTO salaries(employee,salary,date) VALUES ('tom','2345','2023-03-17');
INSERT INTO salaries(employee,salary,date) VALUES ('nick','5424','2022-04-01');
INSERT INTO salaries(employee,salary,date) VALUES ('nick','5500','2023-02-30');
INSERT INTO salaries(employee,salary,date) VALUES ('juli','4566','2021-04-03');
INSERT INTO salaries(employee,salary,date) VALUES ('juli','6000','2024-01-12');
INSERT INTO salaries(employee,salary,date) VALUES ('axel','12444','2022-05-17');
INSERT INTO salaries(employee,salary,date) VALUES ('axel','14000','2023-11-12');
INSERT INTO salaries(employee,salary,date) VALUES ('henry','1244','2021-03-19');
INSERT INTO salaries(employee,salary,date) VALUES ('henry','7000','2023-02-09');
INSERT INTO salaries(employee,salary,date) VALUES ('tomas','2345','2024-02-02');
INSERT INTO salaries(employee,salary,date) VALUES ('tomas','4000','2024-02-09');
INSERT INTO salaries(employee,salary,date) VALUES ('fiona','1000','2023-07-31');
INSERT INTO salaries(employee,salary,date) VALUES ('fiona','1200','2024-01-29');
INSERT INTO salaries(employee,salary,date) VALUES ('ben','1244','2021-12-14');
INSERT INTO salaries(employee,salary,date) VALUES ('ben','7001','2023-03-27');
INSERT INTO salaries(employee,salary,date) VALUES ('shen','6000','2022-02-18');
INSERT INTO salaries(employee,salary,date) VALUES ('shen','7001','2024-01-28');
INSERT INTO salaries(employee,salary,date) VALUES ('lora','4050','2023-08-30');
INSERT INTO salaries(employee,salary,date) VALUES ('lora','7400','2024-01-19');


CREATE TABLE IF NOT EXISTS employees(
   head     VARCHAR(6)
  ,employee VARCHAR(5)
);
INSERT INTO employees(head,employee) VALUES ('donald','tom');
INSERT INTO employees(head,employee) VALUES ('olaf','nick');
INSERT INTO employees(head,employee) VALUES ('jacob','juli');
INSERT INTO employees(head,employee) VALUES ('donald','axel');
INSERT INTO employees(head,employee) VALUES ('olaf','henry');
INSERT INTO employees(head,employee) VALUES ('jacob','tomas');
INSERT INTO employees(head,employee) VALUES ('donald','fiona');
INSERT INTO employees(head,employee) VALUES ('olaf','ben');
INSERT INTO employees(head,employee) VALUES ('jacob','shen');
INSERT INTO employees(head,employee) VALUES ('doanld','lora');