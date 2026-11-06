from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from pydantic_classes import *
from sql_alchemy import *
from database import get_db
from bal_stdlib import *

router = APIRouter()

############################################
#   TimeService Method Endpoints
############################################





@router.post("/timeservice/{timeservice_id}/methods/getCurrentTime/", response_model=None, tags=["TimeService Methods"])
async def execute_timeservice_getCurrentTime(
    timeservice_id: int,  # the TimeService that getCurrentTime runs on
    params: dict = Body(default=None, embed=True),
    database: Session = Depends(get_db)
):
    """Execute the getCurrentTime method on a TimeService instance.

    TimeService.getCurrentTime() is declared with no parameters, and the button sends none.
    An empty request body must succeed - default any value the spec leaves open, never demand it.
    """
    # TimeService.getCurrentTime: load the instance
    _timeservice_object = database.query(TimeService).filter(TimeService.id == timeservice_id).first()
    if _timeservice_object is None:
        raise HTTPException(status_code=404, detail="TimeService not found")
    # TimeService.getCurrentTime
    raise HTTPException(
        status_code=501,
        detail="Method 'getCurrentTime' of TimeService is modeled but has no implementation - 501, never a fake success",
    )

