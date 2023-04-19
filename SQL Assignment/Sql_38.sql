/*Policy is to assign three salesperson to each customers. Display all such combinations.*/
SELECT a.cname, b.cname, a.rating
FROM cust a, cust b
WHERE a.rating = b.rating AND a.cnum != b.cnum AND a.cnum <= b.cnum;
