/*All orders that are greater than the average for Oct 4.*/
Select *  from orders where amt > ( select avg(amt)  from orders where odate = '1994-10-3'); 