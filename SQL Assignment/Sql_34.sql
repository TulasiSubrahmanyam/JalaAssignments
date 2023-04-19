/*Names of salesperson and customer for each order after the order number.*/
Select onum, sname, cname from orders, cust, salespeople where orders.cnum = cust.cnum and orders.snum = salespeople.snum;