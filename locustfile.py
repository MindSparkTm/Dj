from locust import HttpLocust, TaskSet, task
from random import randrange
class UserActions(TaskSet):

    # @task
    # def get_tests(self):
    #     response = self.client.get("/library/book/api/v1")
    #     print('response',response)

    @task
    def put_tests(self):
        val = randrange(100)
        response = self.client.post("/library/book/api/v1/", {
            "title": "load testing" + str(val),
            "category": 1,
            "publication_date": "2019-09-22",
            "publisher": 1
        })

        print('response', response)


class WebsiteUser(HttpLocust):
    task_set = UserActions


