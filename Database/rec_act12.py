import sqlite3


def answers():
    '''Enter your SQL Queries to the questions in your recitation activity. 
        Do NOT modify the variable names or return statement'''


    question1 = '''
                    SELECT
                    FROM

                '''


    question2 = '''
                    SELECT
                    FROM
                    WHERE
                '''


    question3 = '''
                    SELECT
                    FROM
                    WHERE
                '''


    question4 = '''
                    SELECT
                    FROM
                    WHERE
                '''

    return question1, question2, question3, question4
   

def query(sqlStatement):
    conn = None
    try:
        conn = sqlite3.connect('survey.db')
        cur = conn.cursor()
        cur.execute(sqlStatement)
        result = cur.fetchall()
        for row in result:
            print(row)
            
        conn.commit()  
    except sqlite3.Error:
        print('Database error')
        raise
    except Exception:
        print('Runtime error')
        raise
    finally:
        if conn is not None:
            conn.close()

