/*Find all pairs of customers served by single salesperson.*/
Select cname from cust where city = ( select city  from cust, salespeople
where cust.snum = salespeople.snum and sname = 'Serres');
Select cname  from cust where city in ( select city from cust, orders where cust.cnum = orders.cnum and orders.snum in ( select snum  from salespeople where sname = 'Serres'));