from main_products import execute_products
from main_sessions import execute_sessions
from main_visitors import execute_visitors
from main_koppeltabellen import execute_koppeltabel_order
from main_koppeltabellen import execute_koppeltabel_buids

execute_products()
execute_sessions()
execute_visitors()
execute_koppeltabel_order()
execute_koppeltabel_buids()


# FIX execute many per 10000 resultaten invoeren in SQL zoek op SQL execute many