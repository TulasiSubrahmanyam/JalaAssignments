/*Produce names and cities of all customers with the same rating as Hoffman.*/
Select cname, city from cust where rating = (select rating from cust where cname = 'Hoffman') and cname != 'Hoffman';