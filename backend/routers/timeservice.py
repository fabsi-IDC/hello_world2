from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from pydantic_classes import *
from sql_alchemy import *
from database import get_db
from bal_stdlib import *

router = APIRouter()


@router.get("/timeservice/", response_model=None, tags=["TimeService"])
def get_all_timeservice(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    return database.query(TimeService).all()


@router.get("/timeservice/count/", response_model=None, tags=["TimeService"])
def get_count_timeservice(database: Session = Depends(get_db)) -> dict:
    """Get the total count of TimeService entities"""
    count = database.query(TimeService).count()
    return {"count": count}


@router.get("/timeservice/paginated/", response_model=None, tags=["TimeService"])
def get_paginated_timeservice(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of TimeService entities"""
    total = database.query(TimeService).count()
    timeservice_list = database.query(TimeService).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": timeservice_list
    }


@router.get("/timeservice/{timeservice_id}/", response_model=None, tags=["TimeService"])
async def get_timeservice(timeservice_id: int, database: Session = Depends(get_db)) -> TimeService:
    db_timeservice = database.query(TimeService).filter(TimeService.id == timeservice_id).first()
    if db_timeservice is None:
        raise HTTPException(status_code=404, detail="TimeService not found")

    response_data = {
        "timeservice": db_timeservice,
}
    return response_data



@router.post("/timeservice/", response_model=None, tags=["TimeService"])
async def create_timeservice(timeservice_data: TimeServiceCreate, database: Session = Depends(get_db)) -> TimeService:


    db_timeservice = TimeService(
        )

    database.add(db_timeservice)
    database.flush()
    database.refresh(db_timeservice)




    database.commit()
    database.refresh(db_timeservice)
    return db_timeservice


@router.post("/timeservice/bulk/", response_model=None, tags=["TimeService"])
async def bulk_create_timeservice(items: list[TimeServiceCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple TimeService entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item

            db_timeservice = TimeService(
            )
            database.add(db_timeservice)
            database.flush()  # Get ID without committing
            created_items.append(db_timeservice.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} TimeService entities"
    }


@router.delete("/timeservice/bulk/", response_model=None, tags=["TimeService"])
async def bulk_delete_timeservice(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple TimeService entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_timeservice = database.query(TimeService).filter(TimeService.id == item_id).first()
        if db_timeservice:
            database.delete(db_timeservice)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} TimeService entities"
    }

@router.put("/timeservice/{timeservice_id}/", response_model=None, tags=["TimeService"])
async def update_timeservice(timeservice_id: int, timeservice_data: TimeServiceCreate, database: Session = Depends(get_db)) -> TimeService:
    db_timeservice = database.query(TimeService).filter(TimeService.id == timeservice_id).first()
    if db_timeservice is None:
        raise HTTPException(status_code=404, detail="TimeService not found")

    database.commit()
    database.refresh(db_timeservice)

    return db_timeservice


@router.delete("/timeservice/{timeservice_id}/", response_model=None, tags=["TimeService"])
async def delete_timeservice(timeservice_id: int, database: Session = Depends(get_db)):
    db_timeservice = database.query(TimeService).filter(TimeService.id == timeservice_id).first()
    if db_timeservice is None:
        raise HTTPException(status_code=404, detail="TimeService not found")
    # Snapshot the columns before deleting: cascading the association-class
    # links loads relationship collections whose back-references would make
    # the JSON encoder recurse endlessly on the live object.
    deleted_timeservice = {
        attr.key: getattr(db_timeservice, attr.key)
        for attr in db_timeservice.__mapper__.column_attrs
    }
    database.delete(db_timeservice)
    database.commit()
    return deleted_timeservice



