/*List each order number followed by the name of the customer who made the order.*/
Select onum, cname from orders, cust where orders.cnum = cust.cnum; 