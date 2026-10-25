import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            count INTEGER
        );
    ''')
    cur.execute('SELECT COUNT(*) FROM visits;')
    if cur.fetchone()[0] == 0:
        cur.execute('INSERT INTO visits (count) VALUES (0);')
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def hello():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE visits SET count = count + 1 RETURNING count;')
        count = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(message="Connected successfully!", visit_count=count)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    # Initialize table on startup
    init_db()
    app.run(host='0.0.0.0', port=5000)