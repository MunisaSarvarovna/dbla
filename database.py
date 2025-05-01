import psycopg2

def add_user(chat_id):
    conn = psycopg2.connect("dbname=bank user=postgres,password=6066")
    cur = conn.cursor()


    cur.execute(f"INSERT INTO users(chat_id) values ('{chat_id}');")

    conn.commit()
    cur.close()
    conn.close()