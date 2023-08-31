--cartesian product
select last_name,department_name
from employees
cross join DEPARTMENTS

--natural joins;colums with same name
select department_id,department_name,location_id,city
from departments
natural join locations;

select * from LOCATIONS

select e.employee_id,e.last_name,d.location_id
from employees e join departments d
using (department_id);

select e.employee_id,e.last_name,e.department_id,d.department_id,d.location_id
from employees e join departments d
on (e.department_id=d.department_id);

--three tables joining with on clause
select employee_id,city,department_name
from employees e
join departments d
on d.department_id=e.department_id
join LOCATIONS l
on d.location_id=l.location_id;

select e.last_name,e.department_id,d.department_name
from employees e
left outer join departments d
on (e.department_id=d.department_id);

select e.last_name,e.department_id,d.department_name
from employees e
right outer join departments d
on (e.department_id=d.department_id);

select e.last_name,e.department_id,d.department_name
from employees e
full outer join departments d
on (e.department_id=d.department_id);

select e.employee_id,e.last_name,e.department_id,d.department_name,d.location_id
from employees e
 join departments d
on (e.department_id=d.department_id) and e.manager_id=149;