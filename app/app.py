from flask import Flask, render_template, request
import os
import psycopg2
# from dotenv import load_dotenv
# load_dotenv()

db_name = os.environ["POSTGRES_DB"]
usr = os.environ["POSTGRES_USER"]
usr_pwd = os.environ["POSTGRES_PASSWORD"]
hst = os.environ["POSTGRES_HOST"]
prt = os.environ["POSTGRES_PORT"]


app = Flask(__name__)
# Konfigurasi database
db_conn = psycopg2.connect(
    database = db_name,
    user = usr,
    password = usr_pwd,
    host = hst,
    port = prt
)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nama = request.form["nama"]
        nim = request.form["nim"]
        mata_kuliah = request.form["mata_kuliah"]
        jurusan = request.form["jurusan"]

        cursor = db_conn.cursor()
        cursor.execute("INSERT INTO absensi_table (nama, nim, mata_kuliah, jurusan) VALUES (%s, %s, %s, %s)", (nama, nim, mata_kuliah, jurusan))
        db_conn.commit()
        cursor.close()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
