select 
	DISTINCT 
	SECTION_COD, 
	SECTION_NAME,
	DEP_COD,
	DEP_NAME 
from data_product dp 
where 
	DEP_NAME = "BEBIDAS" or 
	DEP_NAME = "PADARIA"
ORDER by DEP_NAME asc;