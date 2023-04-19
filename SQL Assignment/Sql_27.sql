SELECT CONCAT('For ', DATE_FORMAT(ODATE, '%d/%m/%y'), ' there are ', COUNT(*), ' Orders')
FROM orders
GROUP BY ODATE;
