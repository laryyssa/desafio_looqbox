select 
	PRODUCT_COD,
	PRODUCT_NAME,
	PRODUCT_VAL 
from data_product 
order by PRODUCT_VAL desc
limit 10;