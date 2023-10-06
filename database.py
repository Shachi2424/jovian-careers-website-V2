from sqlalchemy import create_engine, text


db_connection_string = ("mysql+pymysql://mood2q2gk7vbr8697w7v:pscale_pw_KNfAms6O5Ii86gqbFYi9yyuAdU2ybcBufhGkV4Gf1Vc@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4")

engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.fetchall())

load_jobs_from_db()
  
      

    