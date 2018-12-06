
-- 1. find the location of campuses 3 characters  last 
USE STUDENTDB;
SELECT lastname, RIGHT(date, 3) FROM studentdb.list;



-- 2. find the location of campuses with 3 characters from starting

SELECT lastname, LEFT(date, 3) FROM studentdb.list;



-- 3. remove the ld from the location of all campuses

SELECT lastname, TRIM(trailing 'ex' From lastname) FROM studentdb.list;



-- 4. find the location on 'i' in location of all campuses

SELECT lastname,
       POSITION('N' IN lastname)
	FROM list;


	
	
-- 5. get the substring from index 4 to 2 characters from lastname column

SELECT lastname,
       SUBSTR(lastname, 4,2)
	FROM list;
	
	

	
-- 6. find the sum of mpg and also print the average mpg  from all the years of car data

select avg(some) from (select sum(mpg) as some from cars_data group by year) car_table; 






-- 7. show all the car ids those has modelname or not registered as a model in car_names table

SELECT car_names.id 
FROM car_names RIGHT JOIN cars_data 
ON cars_data.id = car_names.id

UNION  

SELECT cars_data.id 
FROM car_names RIGHT JOIN cars_data 
ON cars_data.id = car_names.id;




-- 8. display the cars who has  same horse power from cars_data

SELECT 
    c1.horsepower, c1.id, c2.id
FROM
    cars_data c1
        INNER JOIN
    cars_data c2 ON c1.id = c2.id
    AND c1.id > c2.id
ORDER BY c1.horsepower;



-- 9. find the count of all flights for airlines and make average of that

select avg(some) from (select count() as some from cars_data group by airline) car_table; 






-- 10. show all the airline id those having airline name and flights associated 

SELECT car_names.id 
FROM car_names RIGHT JOIN cars_data 
ON cars_data.id = car_names.id

UNION  

SELECT cars_data.id 
FROM car_names RIGHT JOIN cars_data 
ON cars_data.id = car_names.id;