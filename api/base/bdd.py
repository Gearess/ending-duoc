import psycopg2
from psycopg2 import DatabaseError

def get_connection():
  try:
    cx = psycopg2.connect("dbname='rdhiiudr' user='rdhiiudr' host='isabelle.db.elephantsql.com' password='w4TXVCV1cJtJCjxIebkYCIKdlKq9ZEdU'")
    return cx
  except DatabaseError as ex:
    raise ex