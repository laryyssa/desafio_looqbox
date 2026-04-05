select 
	sc.BUSINESS_NAME,
	SUM(ss.SALES_VALUE) as TOTAL_SALES_VALUE
from data_store_cad sc
inner join data_store_sales ss on sc.STORE_CODE = ss.STORE_CODE 
WHERE 
	ss.DATE >= "2019-01-01" AND 
	ss.DATE < "2019-05-01"
group by sc.BUSINESS_NAME 