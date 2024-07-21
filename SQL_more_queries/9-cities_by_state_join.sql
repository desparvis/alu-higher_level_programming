-- comment section
SELECT cities.id, cities.name, states.name INNER JOIN states cities.state_id = states.id ORDER BY cities.id DESC;
