SELECT cust.CNAME
FROM cust, orders
WHERE orders.SNUM = cust.CNUM
AND orders.SNUM IN (SELECT snum FROM salespeople WHERE sname IN ('Peel', 'Mohan'));
