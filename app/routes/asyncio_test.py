from fastapi import APIRouter
import asyncio 
import requests
import aiohttp
from models import NameResponse

router = APIRouter()


def requests_get_sync(url):
    return requests.get(url) 

async def get_name_sync():
    return requests.get("http://dummy-api:8001/").text.replace('"', "")

async def get_name_async():
    async with aiohttp.ClientSession() as aiohttp_session:
        async with aiohttp_session.get("http://dummy-api:8001/") as resp:
            text = await resp.text()
            return text.replace('"', "")

@router.get("/names/async/{count}", summary="Get a list of names. Gathering is async")
async def get_names_from_dummy_api(count: int) -> NameResponse:
    executions = []
    counter = 0
    while counter < count:
        executions.append(get_name_async())
        counter += 1
    names = await asyncio.gather(*executions)
    return {"message" : names}

@router.get("/names/sync/{count}", summary="Get a list of names. Gathering is sync")
async def get_names_from_dummy_api(count: int) -> NameResponse:
    executions = []
    counter = 0
    while counter < count:
        executions.append(get_name_sync())
        counter += 1
    names = await asyncio.gather(*executions)
    return {"message" : names}