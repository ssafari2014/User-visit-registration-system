from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models import PageVisit
from utils.database import get_db
from app.schemas.visit import PageVisitCreate, PageVisitResponse
from app.services.visit import create_page_visit
from app.routers.user import get_profile
from fastapi_cache.decorator import cache
from app.services.visit import get_visit_count
router = APIRouter(prefix="/visit", tags=["visit"])
@router.post("/", response_model=PageVisitResponse)
def track_page_visit(data: PageVisitCreate, db: Session = Depends(get_db)):
    return create_page_visit(db, data)



@router.get("/", response_model=PageVisitResponse)
@cache(expire=60)
async def get_page_visits(page_name:str, db: Session = Depends(get_db)):
    """مشاهده بازدیدها"""
    print("QUERY executed")
    return get_visit_count(db, page_name)
    # visits = db.query(PageVisit).filter(PageVisit.id == users_profile.id).all()
    # print("QUERY executed")
    # return visits
