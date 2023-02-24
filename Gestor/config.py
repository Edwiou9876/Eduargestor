import sys


if "pytest" in sys.argv[0]:
    DATABASE_PATH = 'tests/clientes_test.csv'

else: DATABASE_PATH = 'clientes.csv'



