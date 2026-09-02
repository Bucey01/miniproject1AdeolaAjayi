# INF601 - Advanced Programming in Python
# Adeola Ajayi
# Mini Project 1

import os
import requests

class PracticeHubClient:
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def handle_response(self, response):
        if response.status_code == 401:
            print("401 Unauthorized: Check your API token.")
            return False

        if response.status_code == 403:
            print("403 Forbidden: You can only modify your own posts.")
            return False

        if response.status_code == 404:
            print("404 Not Found: The requested post does not exist.")
            return False

        if response.status_code == 422:
            try:
                detail = response.json()["detail"]
            except (ValueError, KeyError):
                detail = "Invalid data."

            print(f"422 Invalid Data: {detail}")
            return False

        if not response.ok:
            print(
                f"Request failed with status code "
                f"{response.status_code}."
            )
            return False

        return True

    def create_post(self, title, body="", tags=None):
        response = requests.post(
            f"{self.base_url}/api/v1/posts",
            headers=self.headers,
            json={
                "title": title,
                "body": body,
                "tags": tags or []
            }
        )

        if not self.handle_response(response):
            return None

        return response.json()

    def list_posts(self, mine=False, tag=None):
        params = {
            "mine": mine
        }

        if tag:
            params["tag"] = tag

        response = requests.get(
            f"{self.base_url}/api/v1/posts",
            headers=self.headers,
            params=params
        )

        if not self.handle_response(response):
            return None

        return response.json()

    def get_post(self, post_id):
        response = requests.get(
            f"{self.base_url}/api/v1/posts/{post_id}",
            headers=self.headers
        )

        if not self.handle_response(response):
            return None

        return response.json()

