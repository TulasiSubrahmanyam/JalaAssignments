
/*Find all customers whose cnum is 1000 above the snum of serres.*/
Select cnum, cname from cust where cnum > ( select snum+1000  from salespeople where sname = 'Serres');