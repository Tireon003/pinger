import aiohttp
import logging

from client.exceptions import ApiServerErrorException, UnprocessableEntityException

logging.basicConfig(level=logging.ERROR)


class UserApi:

    def __init__(self, domain: str) -> None:
        self.domain = domain

    async def check_user_exists(self, user_id: int) -> bool:
        async with aiohttp.ClientSession() as session:
            url = f"{self.domain}/api/users/{user_id}"
            async with session.get(url) as response:
                if response.status == 404:
                    logging.info(f"User {user_id} does not exist, need to create")
                    return False
                elif response.status >= 500:
                    logging.error(f"Server error, returned status {response.status}")
                    raise ApiServerErrorException(status_code=response.status)
                elif response.status == 422:
                    logging.info("Api got unprocessable entity")
                    raise UnprocessableEntityException()
                else:
                    return True

    async def create_user(self, user_id: int, chat_id: int) -> True | None:
        async with aiohttp.ClientSession() as session:
            url = f"{self.domain}/api/users?user_id={user_id}&chat_id={chat_id}"
            async with session.get(url) as response:
                if response.status >= 500:
                    logging.error(f"Server error while creating user, returned status {response.status}")
                    raise ApiServerErrorException(status_code=response.status)
                if response.status == 400:
                    logging.info(f"User {user_id} already exists")
                    return None
                if response.status == 201:
                    logging.info(f"User {user_id} created")
                    return True
