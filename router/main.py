# conding:utf-8
import os
import urllib
from typing import Optional

from fastapi import APIRouter, Request, Body, Response, UploadFile, File
from starlette.responses import FileResponse

from service import fileService

# main的分路由


main_app = APIRouter()


@main_app.get("/test", tags=["测试接口"])
async def read_item(req: Request, body: Optional[str] = Body(None), response: Response = Response):
    """
    测试调用服务
    """

    response.headers['x-fsm-test'] = "china no 1"
    return {"header": req.headers, "response": response}


@main_app.get("/file", tags=["文件查看"])
async def file():
    fileList = await fileService.get_filelist()
    return fileList


@main_app.post("/upload", tags=["文件上传"])
async def upload(file: UploadFile = File()):
    filename = file.filename
    with open(os.getcwd() + "/static/file/" + filename, "wb") as f:
        f.write(file.file.read())
    return {"success": True}


@main_app.get("/filedown/{filename}", tags=["文件下载"])
def file(filename: str):
    print('-------------------------'+filename)
    path = os.getcwd() + "/static/file/" + filename
    fileResponse = FileResponse(path)

    # 这个header还是必须要加的，因为前端需要用这个进行处理
    print('2222222222222222222222222222222222222'+filename)
    fileResponse.headers["Content-Disposition"] = "attachment; filename=" + filename
    return fileResponse
