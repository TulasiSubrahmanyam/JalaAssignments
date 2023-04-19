/*Count the customers with rating above San Jose’s average.*/
Select cnum, rating from cust where rating > ( select avg(rating)  from cust where city = 'San Jose'); 