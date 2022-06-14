# TODO: analytics related controllers here
from datetime import datetime

from fastapi import APIRouter, Depends, Query

from adapters.contract import DateTimeEnv
from adapters.db import DBFacade
from adapters.token import TokenAdapter
from models.schema import User

router = APIRouter(
    prefix="/analytics",
    tags=["analytics"],
    responses={404: {"description": "Not found"}},
)


@router.get("/likes_by_day")
def likes_by_day(
    date_from: str = Query(default=None, max_length=50),
    date_to: str = Query(default=None, max_length=50),
    current_user: User = Depends(TokenAdapter.get_current_user),
):
    time_format = DateTimeEnv.get_date_format()
    date_from_obj = datetime.strptime(date_from, time_format)
    date_to_obj = datetime.strptime(date_to, time_format)
    # TODO: extract common time-related and likes-by-dat functionality
    posts = DBFacade().get_likes_by_user_date(
        date_from_obj, date_to_obj, current_user.id
    )
    likes_by_day = {}
    for post in posts:
        date = post.time_created
        date = date.strftime(time_format)
        likes_by_day[date] = likes_by_day.get(date, 0) + 1
    return likes_by_day


@router.get("/likes_by_day_general")
def likes_by_day(date_from: str, date_to: str):
    time_format = DateTimeEnv.get_date_format()
    date_from_obj = datetime.strptime(date_from, time_format)
    date_to_obj = datetime.strptime(date_to, time_format)

    posts = DBFacade().get_likes_by_user_date(
        date_from_obj, date_to_obj
    )
    likes_by_day = {}
    for post in posts:
        date = post.time_created
        date = date.strftime(time_format)
        likes_by_day[date] = likes_by_day.get(date, 0) + 1
    return likes_by_day
