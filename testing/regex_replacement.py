import re
address = '140002 ЛЮБЕРЦЫ 2 ОКТЯБРЬСКИЙ ПР 123/4-115'
result = re.sub(r' \d{1} ',' ', address)
print(result)
