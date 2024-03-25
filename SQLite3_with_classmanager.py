import sqlite3


class ClassManager:
    def __init__(self):
        self.conn = sqlite3.connect('test.db')
        self.cursor = self.conn.cursor()

    def setup_database(self):
        self.cursor.execute(''' 
        CREATE TABLE if not exists Advisor( 
            AdvisorID INTEGER NOT NULL, 
            AdvisorName TEXT NOT NULL, 
            PRIMARY KEY(AdvisorID) 
            )
        ''')
        self.cursor.execute('''
        CREATE TABLE if not exists Student(
            StudentID INTEGER PRIMARY KEY,
            StudentName TEXT NOT NULL,
            AdvisorIDs TEXT
            )
        ''')

        advisors = [
            (1, "John Paul"),
            (2, "Anthony Roy"),
            (3, "Raj Shetty"),
            (4, "Sam Reeds"),
            (5, "Arthur Clintwood")
        ]

        students = [
            (501, "Geek1", "1 2"),
            (502, "Geek2", "1"),
            (503, "Geek3", "3"),
            (504, "Geek4", "2"),
            (505, "Geek5", "4"),
            (506, "Geek6", "2 3"),
            (507, "Geek7", "2"),
            (508, "Geek8", "3 5"),
            (509, "Geek9", ""),
            (510, "Geek10", "1 4")
        ]

        self.cursor.executemany('INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES (?, ?)', advisors)
        self.cursor.executemany('INSERT INTO Student(StudentID, StudentName, AdvisorIDs) VALUES (?, ?, ?)', students)

        self.conn.commit()

    def count_function(self):
        self.cursor.execute('''
            SELECT Advisor.AdvisorID, Advisor.AdvisorName, COUNT(Student.StudentID) AS StudentCount
            FROM Advisor
            JOIN Student ON Student.AdvisorIDs LIKE '%' || Advisor.AdvisorID || '%'
            GROUP BY Advisor.AdvisorID
            ORDER BY Advisor.AdvisorID;
            ''')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()


# Example usage:
if __name__ == "__main__":
    manager = ClassManager()
    manager.setup_database()

    count_table = manager.count_function()
    for row in count_table:
        print(f"ID: {row[0]}, Name: {row[1]}, Number of Students: {row[2]}")

    manager.close()
