-- cities of california
USE hbtn_0d_usa;
SELECT city.id, city.name FROM cities WHERE state.id = (SELECT id FROM states WHERE state.name = "California") ORDER BY id ASC;
