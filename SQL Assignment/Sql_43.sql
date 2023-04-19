/*Extract all the orders of Motika.*/
Select Onum from orders	where snum = ( select snum from salespeople where sname = 'Motika'); 