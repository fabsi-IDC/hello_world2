from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from pydantic_classes import *
from sql_alchemy import *
from database import get_db
from bal_stdlib import *

router = APIRouter()


@router.get("/helloworld/", response_model=None, tags=["HelloWorld"])
def get_all_helloworld(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    return database.query(HelloWorld).all()


@router.get("/helloworld/count/", response_model=None, tags=["HelloWorld"])
def get_count_helloworld(database: Session = Depends(get_db)) -> dict:
    """Get the total count of HelloWorld entities"""
    count = database.query(HelloWorld).count()
    return {"count": count}


@router.get("/helloworld/paginated/", response_model=None, tags=["HelloWorld"])
def get_paginated_helloworld(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of HelloWorld entities"""
    total = database.query(HelloWorld).count()
    helloworld_list = database.query(HelloWorld).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": helloworld_list
    }
@router.get("/helloworld/search/", response_model=None, tags=["HelloWorld"])
def search_helloworld(
    id: int = None,
    Name: str = None,
    database: Session = Depends(get_db)
) -> list:
    """Search HelloWorld entities by attributes"""
    query = database.query(HelloWorld)

    if id is not None:
        query = query.filter(HelloWorld.id == id)
    if Name is not None:
        query = query.filter(HelloWorld.Name.ilike(f"%{Name}%"))

    results = query.all()
    return results


@router.get("/helloworld/{helloworld_id}/", response_model=None, tags=["HelloWorld"])
async def get_helloworld(helloworld_id: int, database: Session = Depends(get_db)) -> HelloWorld:
    db_helloworld = database.query(HelloWorld).filter(HelloWorld.id == helloworld_id).first()
    if db_helloworld is None:
        raise HTTPException(status_code=404, detail="HelloWorld not found")

    response_data = {
        "helloworld": db_helloworld,
}
    return response_data



@router.post("/helloworld/", response_model=None, tags=["HelloWorld"])
async def create_helloworld(helloworld_data: HelloWorldCreate, database: Session = Depends(get_db)) -> HelloWorld:


    db_helloworld = HelloWorld(
        Name=helloworld_data.Name        )

    database.add(db_helloworld)
    database.flush()
    database.refresh(db_helloworld)




    database.commit()
    database.refresh(db_helloworld)
    return db_helloworld


@router.post("/helloworld/bulk/", response_model=None, tags=["HelloWorld"])
async def bulk_create_helloworld(items: list[HelloWorldCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple HelloWorld entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item

            db_helloworld = HelloWorld(
                Name=item_data.Name            )
            database.add(db_helloworld)
            database.flush()  # Get ID without committing
            created_items.append(db_helloworld.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} HelloWorld entities"
    }


@router.delete("/helloworld/bulk/", response_model=None, tags=["HelloWorld"])
async def bulk_delete_helloworld(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple HelloWorld entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_helloworld = database.query(HelloWorld).filter(HelloWorld.id == item_id).first()
        if db_helloworld:
            database.delete(db_helloworld)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} HelloWorld entities"
    }

@router.put("/helloworld/{helloworld_id}/", response_model=None, tags=["HelloWorld"])
async def update_helloworld(helloworld_id: int, helloworld_data: HelloWorldCreate, database: Session = Depends(get_db)) -> HelloWorld:
    db_helloworld = database.query(HelloWorld).filter(HelloWorld.id == helloworld_id).first()
    if db_helloworld is None:
        raise HTTPException(status_code=404, detail="HelloWorld not found")

    setattr(db_helloworld, 'Name', helloworld_data.Name)
    database.commit()
    database.refresh(db_helloworld)

    return db_helloworld


@router.delete("/helloworld/{helloworld_id}/", response_model=None, tags=["HelloWorld"])
async def delete_helloworld(helloworld_id: int, database: Session = Depends(get_db)):
    db_helloworld = database.query(HelloWorld).filter(HelloWorld.id == helloworld_id).first()
    if db_helloworld is None:
        raise HTTPException(status_code=404, detail="HelloWorld not found")
    # Snapshot the columns before deleting: cascading the association-class
    # links loads relationship collections whose back-references would make
    # the JSON encoder recurse endlessly on the live object.
    deleted_helloworld = {
        attr.key: getattr(db_helloworld, attr.key)
        for attr in db_helloworld.__mapper__.column_attrs
    }
    database.delete(db_helloworld)
    database.commit()
    return deleted_helloworld



