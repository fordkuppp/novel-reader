from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from novel_reader.db import get_db
from typing import Any

bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/")
def home():
    # This is sample data for showing template
    popular: list[dict[str, str]] = []
    latest: list = []
    for _ in range(18):
        popular.append(
            {
                "name": "Novel Name",
                "image": "/static/cover-default.png",
                "get_absolute_url": "/novel-slug/",
                "alt": "alt",
                "latest_chap": "chapter X",
            }
        )

    for _ in range(30):
        latest.append(
            {
                "name": "Best Novel",
                "image": "/static/cover-default.png",
                "get_absolute_url": "/novel/novel-slug/",
                "alt": "alt",
                "chapters": [
                    {
                        "name": "chapter XX",
                        "get_absolute_url": "/chapter/slug/",
                        "get_date": "2 hours ago",
                    },
                    {
                        "name": "chapter XX",
                        "get_absolute_url": "/chapter/slug/",
                        "get_date": "2 hours ago",
                    },
                ],
            }
        )
    return render_template("starter/home.html", popular="POPULAR NOVELS", latest=latest)


@bp.route("/latest/")
def latest():
    data: list[dict] = []
    for _ in range(40):
        data.append(
            {
                "name": "Best Novel",
                "image": "/static/cover-default.png",
                "get_absolute_url": "/novel/novel-slug/",
                "alt": "alt",
                "hits": 30,
                "description": "This is novel description that is very very and very super duper long.",
                "genres": [{
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "name": "Martial Arts",
                    "slug": "martial-arts"
                }],
                "latest_chap": "chapter XX"
            }
        )

    return render_template("starter/list.html", endpoint="LATEST NOVELS", result=data)


@bp.route("/popular/")
def popular():
    data: list[dict] = []
    for _ in range(40):
        data.append(
            {
                "name": "Best Novel",
                "image": "/static/cover-default.png",
                "get_absolute_url": "/novel/novel-slug/",
                "alt": "alt",
                "hits": 30,
                "description": "This is novel description that is very very and very super duper long.",
                "genres": [{
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "name": "Martial Arts",
                    "slug": "martial-arts"
                }],
                "latest_chap": "chapter XX"
            }
        )

    return render_template("starter/list.html", endpoint="POPULAR NOVELS", result=data)


@bp.route("/status/on_going/")
def on_going():
    data: list[dict] = []
    for _ in range(40):
        data.append(
            {
                "name": "Best Novel",
                "image": "/static/cover-default.png",
                "get_absolute_url": "/novel/novel-slug/",
                "alt": "alt",
                "hits": 30,
                "description": "This is novel description that is very very and very super duper long.",
                "genres": [{
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "name": "Martial Arts",
                    "slug": "martial-arts"
                }],
                "latest_chap": "chapter XX"
            }
        )

    return render_template("starter/list.html", endpoint="ON-GOING NOVELS", result=data)


@bp.route("/status/complete/")
def completed():
    data: list[dict] = []
    for _ in range(40):
        data.append(
            {
                "name": "Best Novel",
                "image": "/static/cover-default.png",
                "get_absolute_url": "/novel/novel-slug/",
                "alt": "alt",
                "hits": 30,
                "description": "This is novel description that is very very and very super duper long.",
                "genres": [{
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "name": "Martial Arts",
                    "slug": "martial-arts"
                }],
                "latest_chap": "chapter XX"
            }
        )

    return render_template("starter/list.html", endpoint="COMPLETED NOVELS", result=data)


@bp.route("/status/hiatus/")
def hiatus():
    data: list[dict] = []
    for _ in range(40):
        data.append(
            {
                "name": "Best Novel",
                "image": "/static/cover-default.png",
                "get_absolute_url": "/novel/novel-slug/",
                "alt": "alt",
                "hits": 30,
                "description": "This is novel description that is very very and very super duper long.",
                "genres": [{
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "name": "Martial Arts",
                    "slug": "martial-arts"
                }],
                "latest_chap": "chapter XX"
            }
        )

    return render_template("starter/list.html", endpoint="HIATUS NOVELS", result=data)


@bp.route("/search/")
def search():
    data: list[dict] = []
    for _ in range(40):
        data.append(
            {
                "name": "Best Novel",
                "image": "/static/cover-default.png",
                "get_absolute_url": "/novel/novel-slug/",
                "alt": "alt",
                "hits": 30,
                "description": "This is novel description that is very very and very super duper long.",
                "genres": [{
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "name": "Martial Arts",
                    "slug": "martial-arts"
                }],
                "latest_chap": "chapter XX"
            }
        )

    return render_template("starter/list.html", endpoint="COMPLETED NOVELS", result=data)


@bp.route("/status/hiatus/")
def hiatus():
    data: list[dict] = []
    for _ in range(40):
        data.append(
            {
                "name": "Best Novel",
                "image": "/static/cover-default.png",
                "get_absolute_url": "/novel/novel-slug/",
                "alt": "alt",
                "hits": 30,
                "description": "This is novel description that is very very and very super duper long.",
                "genres": [{
                    "name": "Action",
                    "slug": "action"
                },
                {
                    "name": "Martial Arts",
                    "slug": "martial-arts"
                }],
                "latest_chap": "chapter XX"
            }
        )

    return render_template("starter/list.html", endpoint="SEARCH: KEYWORD", result=data)
