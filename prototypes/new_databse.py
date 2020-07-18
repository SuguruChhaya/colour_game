import sqlite3
connection =sqlite3.connect('highscores.db')
cursor = connection.cursor()


cursor.execute("""CREATE TABLE highscores (
                username text,
                easy_highscore text,
                medium_highscore text,
                hard_highscore text
                )""")

connection.commit()
connection.close()