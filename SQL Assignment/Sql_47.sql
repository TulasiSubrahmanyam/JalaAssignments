/*Find all orders attributed to salespeople servicing customers in london.*/
Select snum, cnum  from orders where cnum in (select cnum  from cust where city = 'London'); 