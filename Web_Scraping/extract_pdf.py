
import camelot

tables = camelot.read_pdf('WHO.pdf', pages='3')
print(tables)

tables.export('WHO_csv.csv', f='csv', compress=True)
