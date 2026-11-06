from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from pydantic_classes import *
from sql_alchemy import *
from database import get_db
from bal_stdlib import *

router = APIRouter()

############################################
#   HelloWorld Method Endpoints
############################################





@router.post("/helloworld/{helloworld_id}/methods/showCurrentTime/", response_model=None, tags=["HelloWorld Methods"])
async def execute_helloworld_showCurrentTime(
    helloworld_id: int,  # the HelloWorld that showCurrentTime runs on
    params: dict = Body(default=None, embed=True),
    database: Session = Depends(get_db)
):
    """Execute the showCurrentTime method on a HelloWorld instance.

    HelloWorld.showCurrentTime() is declared with no parameters, and the button sends none.
    An empty request body must succeed - default any value the spec leaves open, never demand it.
    """
    # HelloWorld.showCurrentTime: load the instance
    _helloworld_object = database.query(HelloWorld).filter(HelloWorld.id == helloworld_id).first()
    if _helloworld_object is None:
        raise HTTPException(status_code=404, detail="HelloWorld not found")
    # HelloWorld.showCurrentTime
    raise HTTPException(
        status_code=501,
        detail="Method 'showCurrentTime' of HelloWorld is modeled but has no implementation - 501, never a fake success",
    )






@router.post("/helloworld/{helloworld_id}/methods/showHelloWorld/", response_model=None, tags=["HelloWorld Methods"])
async def execute_helloworld_showHelloWorld(
    helloworld_id: int,  # the HelloWorld that showHelloWorld runs on
    params: dict = Body(default=None, embed=True),
    database: Session = Depends(get_db)
):
    """Execute the showHelloWorld method on a HelloWorld instance.

    HelloWorld.showHelloWorld() is declared with no parameters, and the button sends none.
    An empty request body must succeed - default any value the spec leaves open, never demand it.
    """
    # HelloWorld.showHelloWorld: load the instance
    _helloworld_object = database.query(HelloWorld).filter(HelloWorld.id == helloworld_id).first()
    if _helloworld_object is None:
        raise HTTPException(status_code=404, detail="HelloWorld not found")
    # HelloWorld.showHelloWorld
    raise HTTPException(
        status_code=501,
        detail="Method 'showHelloWorld' of HelloWorld is modeled but has no implementation - 501, never a fake success",
    )

