import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:62742@localhost/ecommerce_etl')


top_customers= pd.read_sql("""
select customer_name, sum(sales) As total_sales from superstore
group by(customer_name)
order by(total_sales) desc""",con = engine)

top_selling_category=pd.read_sql("""
select Category, sum(sales) as total_sales
from superstore 
group by(Category) 
order by(total_sales) desc""",con = engine)


monthly_sales = pd.read_sql("""
select MONTH(order_date) as month, sum(sales) as total_sales
from superstore
group by (month)
order by total_sales desc""",con = engine)

print (top_customers.head())
print (top_selling_category.head())
print (monthly_sales.head())