# conding:utf-8
from service import mainService
from typing import Optional, List

from fastapi import APIRouter, Header, Request, Body, Response

# main的分路由



main_app = APIRouter()


@main_app.get("/test", tags=["测试接口"])
async def read_item(req: Request, body: Optional[str] = Body(None), response: Response = Response):
    """
    测试调用服务
    """

    user = mainService.get_all_user()
    print(user)
    response.headers['x-fsm-test'] = "china no 1"
    return {"header": req.headers, "body": user, "response": response}


