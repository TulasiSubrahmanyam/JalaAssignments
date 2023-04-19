/*Display all customers located in cities where salesman serres has customer.*/
SELECT cname, sname
FROM salespeople
JOIN cust ON salespeople.sname = cust.cname
WHERE salespeople.sname IN (
  SELECT sname
  FROM (
    SELECT sname
    FROM salespeople
    ORDER BY sname
    LIMIT 3
  ) AS subquery
)
ORDER BY cname;
