/*Produce all customer serviced by salespeople with a commission above 12%.*/
Select cname, sname, comm from cust, salespeople where comm > 0.12 and cust.snum = salespeople.snum; 