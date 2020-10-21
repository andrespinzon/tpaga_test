from typing import Dict
from config.settings import API_TPAGA_URL

from requests import Session, Response
from requests.adapters import HTTPAdapter
from rest_framework.exceptions import NotFound
from urllib3.util.retry import Retry


class TpagaApi:
    __session: Session
    api_url: str = API_TPAGA_URL

    def __init__(self, max_retries: int = 0) -> None:
        self.__session = Session()
        if max_retries > 0:
            retry = Retry(
                total=max_retries,
                read=max_retries,
                connect=max_retries,
                backoff_factor=0.3,
                status_forcelist=(500, 502, 504)
            )
            adapter = HTTPAdapter(max_retries=retry)
            self.__session.mount('http://', adapter)
            self.__session.mount('https://', adapter)

    def payment_requests(self, data: Dict) -> Dict:
        endpoint: str = f'{self.api_url}/payment_requests/create'

        response: Response = self.__session.post(url=endpoint, data=data)
        if not response.ok:
            raise NotFound()

        return response.json()
