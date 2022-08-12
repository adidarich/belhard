from requests import Session


class ResponseServer:

    @staticmethod
    def add_response():
        with Session() as session:
            response = session.put(
                url="https://d474-80-93-191-82.eu.ngrok.io/api/1/article/add",
                json={
                    "title": "Junior_Developer",
                    "body": "name: Didar",
                    "category_id": 1,
                    "user_id": 1
                }
            )
            print(response.json())
            print(response.status_code)

    add_response()

    @staticmethod
    def get_response():
        with Session() as session:
            response = session.get(
                url='https://d474-80-93-191-82.eu.ngrok.io/api/1/article/get',
                params={
                    "article_id": 184
                }
            )
            print(response.json())
            print(response.status_code)

    get_response()

    @staticmethod
    def get_all():
        with Session() as session:
            response = session.get(
                url='https://d474-80-93-191-82.eu.ngrok.io/api/1/article/all',
                params={
                    "category_id": 1
                }
            )
            print(response.json())
            print(response.text)
            print(response.status_code)

    get_all()