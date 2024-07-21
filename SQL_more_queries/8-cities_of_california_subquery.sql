-- cities of california
SELECT id, name FROM cities WHERE state = (SELECT id FROM states WHERE name = "California") ORDER BY id ASC;
