import camelot

tables = camelot.read_pdf('https://sedl.org/afterschool/toolkits/science/pdf/ast_sci_data_tables_sample.pdf', pages='all')
print(tables)

a = tables.export('WHO1.csv', f='csv', compress=True)
print(a[0])


# from tabula import read_pdf

# URL = "https://sedl.org/afterschool/toolkits/science/pdf/ast_sci_data_tables_sample.pdf"

# tabular_data = read_pdf(URL, pages = '1')
