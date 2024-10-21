
#*** select all employes who work in production dept.

SELECT * FROM darbuotojai WHERE skyriaus_pavadinimas = "Gamybos"

#*** Insert new record to employees table filling all the tabs

INSERT INTO darbuotojai (vardas, pavarde, gimimo_data, pareigos)
VALUES ("Jonas", "Jonaitis","1989-05-06","programuotojas")

#**** or ****

INSERT INTO darbuotojai
VALUES ("Jonas", "Jonaitis","1989-05-06","programuotojas") #jeigu visi stulpeliai atitinka, tai nereik stulpeliu pavadinimu

#*** change job possition of employee Pakenas to Tester

UPDATE darbuotojai
SET pareigos = "Testuotojas"
WHERE pavarde = "Pakenas"

#*** delete user

DELETE FROM darbuotojai
WHERE gimimo_data = "1989-05-05" # galima pagal bet kuri stupleli irasant po where


#*** between + and

SELECT * FROM cars
WHERE year >= 1990 AND year <= 1993 # by year collumn

#*** or

SELECT * FROM cars
WHERE year BETWEEN 1990 AND 1993 # easier sollution

#**** using IN and OR

SELECT * FROM cars
WHERE make = "audi" OR make = "ford" OR make = "subaru" # list 1 by 1

#*** or

SELECT * FROM cars
WHERE make IN("audi", "ford", "subaru") # everything in this list

#*** from few letters to find something using LIKE

SELECT * FROM cars
WHERE model LIKE "_" # 1 simbol
WHERE model LIKE "__" # 2 simbols
WHERE model LIKE "_F" # 2 simbols but F is second
WHERE model LIKE "F_" # 2 simbols but F is first
WHERE model LIKE "F__" # 3 simbols but F is first
WHERE model LIKE "F%" # F is first and unlimited leters afterwards or none
WHERE model LIKE "%F" # Unlimited letters or none and finish with F
WHERE model LIKE "%F%" # Unlimited letters in front or none, F , and unlimited letters or none
WHERE model LIKE "F%A" # F is in front , unlimited or none in middle and A at the back

#*** selecting NULL collum

SELECT * FROM cars
WHERE color IS NULL # we cannot use = sign on null statement
WHERE color = "red" # finding by collum color and choosing red

#*** Filtering with AND and OR

SELECT * FROM cars
WHERE make = "BMW" AND year = "2010"
WHERE make = "BMW" OR year = "2010"

#*** Using NOT statement

SELECT * FROM cars
WHERE make NOT IN("audi", "ford", "subaru") # using not we exluding items in a list
WHERE year NOT BETWEEN 1990 AND 1993 # excluding cars between this years
WHERE color IS NOT NULL # getting all items exlcuding these dont have color

#**** Sorting by ORDER BY

SELECT * FROM cars
WHERE make = "Audi" ORDER BY year ASC # Ascending
WHERE make = "Audi" ORDER BY year DESC # Descending

#*** case sensitive

SELECT * FROM cars
WHERE make = "auDi" COLLATE NOCASE # removed case restrictions

#*** adding "random" string

SELECT "LABAS: " || make, model , color FROM cars # adds string to collum LABAS: Audi, A3, red
SELECT "LABAS: " ||" " || make, model , color FROM cars

#*** using  AS for renaming colloms

SELECT make , model AS "labas" FROM cars # changing colums names

#*** Using math

SELECT year, 2024 - year AS "age" FROM cars # subtract 2024 from year car to find out car age
SELECT year, 2024 - year ROUND(prince / 121 * 100) AS "VAT" FROM cars # calculate VAT

#*** Using GROUP BY

SELECT * FROM person GROUP BY first_name , last_surname
HAVING gender = "female" # HAVING is optional, but only works with GROUP BY

#*** or


SELECT price FROM cars
SELECT MIN(price) FROM cars #Groups by min price
SELECT MAX(price) FROM cars #Groups by max price
SELECT make COUNT(make) FROM cars #Groups by counting items in a make collums

#*** Joining tables

SELECT person.first_name, person.last_name, car.plate
FROM person
JOIN car
ON person.car_id = car.id

#*** Joining couple tables

SELECT person.first_name, person.last_name, car.plate, company.name # selecting from persnon table
FROM person
JOIN car ON person.car_id = car.id #added car table
JOIN company ON person.company.id = company.id #added company table
WHERE company.name = "Apple" AND car.make = "Ford" # we still can filter if needed , by adding WHERE

#*** another example

SELECT company.name COUNT(*) # Counting how many ppl working in all companies without grouping them
FROM person
JOIN company ON person.company_id = company.id
# If we want grouping, we add GROUP BY
GROUP BY company.name
HAVING COUNT(*) <=3 #counting ppl who work in company 3 or less employes


SELECT person.first_name, person.last_name, car.make, company.name
FROM person
JOIN car ON person.car_id = car.id
JOIN company ON person.company.id = company.id
WHERE person.company_id IN (
    SELECT person.company_id #getting only 1 collum here
    FROM person 
    GROUP BY person.company_id
    HAVING COUNT (*) <=3
)                                # This is where we put second table into company list, and now we can see name,surname, make and company name
                                 # where employee is 3 or less

#*** Creating table

CREATE TABLE coder (
    f_name STRING, #collumn name
    l_name STRING, #collumn name
    email STRING, #collumn name
    age INTEGER, #collumn name
    xp_years INTEGER #collumn name
);

#*** to add content to table

INSERT INTO coder (f_name, l_name, email, age, xp_years) VALUES ('Aurimas', 'Pakenas', 'aurimasjp@gmail.com', 35, 10);

#** Setting id for a table

CREATE TABLE coder (
    id PRIMARY KEY NOT NULL,#PRIMARY KEY – sets the column as the primary key (unique identifier) of the table.
    f_name STRING NOT NULL,#NOT NULL – indicates that the column value cannot be empty.
    l_name STRING NOT NULL,#UNIQUE – specifies that values in the column must be unique
    email STRING UNIQUE,
    age INTEGER CHECK (age > 17 AND age < 75),#CHECK (condition) – verifies that the value meets the condition.
    xp_years INTEGER CHECK (xp_years < 40)
);

DEFAULT – specifies a default value if no data is provided for the column.

#*** Alter table contents

ALTER TABLE coder ADD COLUMN project_id INTEGER;
ALTER TABLE coder RENAME COLUMN project_id TO team_id;
ALTER TABLE coder RENAME TO coders;


#*** adding tables together

CREATE TABLE coders_skills (
    coder_id INTEGER,
    skill_id INTEGER,
    FOREIGN KEY (coder_id) REFERENCES coders (id),
    FOREIGN KEY (skill_id) REFERENCES skills (id)
);























