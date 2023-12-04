"""this file contains a basic template for starting a new web app attack script"""

from typing import Any
import requests
import json
import base64

requests.urllib3.disable_warnings()

url = "http://aws.amazon.com"
proxies = {
    "http": "http://localhost:8080",
    "https": "https://localhost:8080",
}
ok_codes = [200, 201, 204, 301, 304]
session = requests.Session()


def b64(s: str) -> str:
    return base64.b64encode(bytes(s, encoding="utf8")).decode()


def d64(s: str) -> str:
    return base64.b64decode(s).decode(encoding="utf8")


def json_to_dict(s: str) -> dict:
    return json.loads(s)


def ok(code: int) -> bool:
    return code in ok_codes


# send HTTP requests
def hit(
    method: str = "get",
    url: str = "",
    data: Any = None,
    as_json: bool = False,
    proxy: bool = False,
    headers: dict = {},
    verify: bool = False,
    redirects: bool = True,
) -> requests.Response:
    if as_json:
        headers["Content-Type"] = "application/json"
    return session.request(
        method=method,
        url=url,
        data=json.dumps(data) if as_json else data,
        headers=headers,
        proxies=proxies if proxy else None,
        verify=verify,
        allow_redirects=redirects,
    )


def main():
    # resp = hit(
    #    method="post",
    #    url=url,
    #    data={"hello": "universe"},
    #    as_json=True,
    #    verify=False,
    # )
    # resp = hit(url="http://aws.amazon.com.", redirects=False)
    # code = resp.status_code
    # if ok(code):
    #    if code == 301:
    #        resp2 = hit(
    #            url=resp.headers["Location"],
    #        )
    #        code2 = resp2.status_code
    #        if ok(code2):
    #            print(resp2.headers)
    # else:
    #    print(f"response code = {resp.status_code}")
    resp = hit(url=url)
    code = resp.status_code
    if ok(code):
        print(f"StatusCode: {code}")
    else:
        print(f"Failed with response code `{code}`")


if __name__ == "__main__":
    main()
