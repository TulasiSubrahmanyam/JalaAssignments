/*Extract commissions of all salespeople servicing customers in London.*/
Select comm from salespeople where snum in (select snum from cust where city = 'London');