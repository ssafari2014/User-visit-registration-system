from sqlalchemy.orm import Session
from app.models.visit import PageVisit
from app.schemas.visit import PageVisitCreate, PageVisitResponse
from datetime import datetime

def create_page_visit(db: Session, visit_data: PageVisitCreate):
    page_visit = PageVisit(
        page=visit_data.page,
        user_agent=visit_data.user_agent,
        timestamp=datetime.utcnow()
    )
    db.add(page_visit)
    db.commit()
    db.refresh(page_visit)
    return page_visit

def get_visit_count(db: Session, page_name:str):
    visit_count = db.query(PageVisit).filter(PageVisit.page == page_name).count()
    return f"{page_name} : {visit_count}"

