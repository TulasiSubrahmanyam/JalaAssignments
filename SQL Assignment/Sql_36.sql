/*Calculate the amount of the salesperson’s commission on each order with a rating above 100*/
SELECT SNAME, orders.amt * salespeople.comm
FROM orders
JOIN cust ON cust.cnum = orders.cnum
JOIN salespeople ON salespeople.snum = cust.snum
WHERE cust.rating > 100;
