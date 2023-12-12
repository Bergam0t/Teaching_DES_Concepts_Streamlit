from locust import HttpUser, task, between

class IntroPageUser(HttpUser):
    @task
    def load_page(self):
        self.client.get("/")
    wait_time = between(30, 300)

class ArrivalsUser(HttpUser):
    @task
    def load_page(self):
        self.client.get("/Simulating_Arrivals")
    wait_time = between(30, 300)

class SimpleResourceUser(HttpUser):
    @task
    def load_page(self):
        self.client.get("/Using_A_Simple_Resource")
    wait_time = between(30, 300)


class OptionalStepUser(HttpUser):
    @task
    def load_page(self):
        self.client.get("/Adding_an_Optional_Step")
    wait_time = between(30, 300)

class FullModelUser(HttpUser):
    @task
    def load_page(self):
        self.client.get("/Adding_an_Optional_Step")
    wait_time = between(30, 300)