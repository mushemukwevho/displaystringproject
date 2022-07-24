from typing import Union
from fastapi import FastAPI, HTTPException
from models import contextDisplayString, resolveDisplayString
from services import DisplayStringService
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['GET','POST'],
    )


@app.post("/context_display_strings/")
async def get_display_strings(context_displaystring_item: contextDisplayString):
    """Return displayString for context.

    Args:
        context_displaystring_item (contextDisplayString): 

    Returns:
        Str: displayString
    """
    item_dict = context_displaystring_item.dict()
    if not item_dict:
        raise HTTPException(status_code=400, detail="Bad request, no data")
    return DisplayStringService.\
        get_displaystring_for_context(displaystring_holder=item_dict['displaystring_holder'],
                                      locale=item_dict['locale'],
                                      context=item_dict['context'])
        
@app.post("/resolve_display_strings/")
async def resolve_display_strings(resolve_displaystring_item: resolveDisplayString):
    """Return resolved dictionary with dispaystrings.

    Args:
        resolve_displaystring_item (resolveDisplayString): 

    Returns:
        dict: "documents"
    """
    item_dict = resolve_displaystring_item.dict()
    if not item_dict:
        raise HTTPException(status_code=400, detail="Bad request, no data")
    return DisplayStringService.\
        resolve_displaystrings(dictionary=item_dict['dictionary'],
                                      locale=item_dict['locale'],
                                      context=item_dict['context'])
