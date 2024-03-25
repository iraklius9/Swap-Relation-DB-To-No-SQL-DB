from pymongo import MongoClient


class ClassManagerMongo:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['test_database']
        self.advisor_collection = self.db['advisors']
        self.student_collection = self.db['students']

    def setup_database(self):
        advisors = [
            {"AdvisorID": 1, "AdvisorName": "John Paul"},
            {"AdvisorID": 2, "AdvisorName": "Anthony Roy"},
            {"AdvisorID": 3, "AdvisorName": "Raj Shetty"},
            {"AdvisorID": 4, "AdvisorName": "Sam Reeds"},
            {"AdvisorID": 5, "AdvisorName": "Arthur Clintwood"}
        ]

        students = [
            {"StudentID": 501, "StudentName": "Geek1", "AdvisorIDs": [1, 2]},
            {"StudentID": 502, "StudentName": "Geek2", "AdvisorIDs": [1]},
            {"StudentID": 503, "StudentName": "Geek3", "AdvisorIDs": [3]},
            {"StudentID": 504, "StudentName": "Geek4", "AdvisorIDs": [2]},
            {"StudentID": 505, "StudentName": "Geek5", "AdvisorIDs": [4]},
            {"StudentID": 506, "StudentName": "Geek6", "AdvisorIDs": [2, 3]},
            {"StudentID": 507, "StudentName": "Geek7", "AdvisorIDs": [2]},
            {"StudentID": 508, "StudentName": "Geek8", "AdvisorIDs": [3, 5]},
            {"StudentID": 509, "StudentName": "Geek9", "AdvisorIDs": []},
            {"StudentID": 510, "StudentName": "Geek10", "AdvisorIDs": [1, 4]}
        ]

        self.advisor_collection.insert_many(advisors)
        self.student_collection.insert_many(students)

    def count_function(self):
        advisors = self.advisor_collection.find()
        count_results = []

        for advisor in advisors:
            student_count = self.student_collection.count_documents({"AdvisorIDs": advisor["AdvisorID"]})
            count_results.append({
                "AdvisorID": advisor["AdvisorID"],
                "AdvisorName": advisor["AdvisorName"],
                "StudentCount": student_count
            })

        return count_results

    def clear(self):
        self.advisor_collection.delete_many({})

        self.student_collection.delete_many({})

    def close(self):
        self.client.close()


if __name__ == "__main__":
    manager = ClassManagerMongo()
    manager.setup_database()

    # manager.clear()

    count_table = manager.count_function()
    for row in count_table:
        print(f"ID: {row['AdvisorID']}, Name: {row['AdvisorName']}, Number of Students: {row['StudentCount']}")

    manager.close()
