Select ODATE, SNUM, max(AMT) from orders where AMT > 30 group by ODATE, SNUM order by ODATE,SNUM;
select * from orders