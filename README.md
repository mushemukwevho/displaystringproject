## Truckoo: DisplayStringProject(FastAPI)

## Run from container

Navigate to root folder.

run `$ docker build -t displaystringproject .`

then `$ docker run -p 8000:8000 displaystringproject`

## Debug/Run locally

Navigate to root folder.

run `$ pip install poetry`, after that

run `$ poetry install`,

run `$ cd app`

then `$ uvicorn main:app --reload`

## Tests

Navigate to root folder.

run `$ pytest`

Note: Tests will be put in separate tests directory later

## Endpoints


| Method | Url |
| ------ | ----------- |
| POST   | `/context_display_strings/` for method `get_displaystring_for_context(uid, locale, offer)`|
| POST   | `/resolve_display_strings/` for method `resolve_displaystrings(dictionary, locale, context)` |
