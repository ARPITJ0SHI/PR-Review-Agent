from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.github_service import github_service
from app.agents.graph import app_graph

router = APIRouter()

class ReviewRequest(BaseModel):
    repo_name: str
    pr_number: int

class ReviewResponse(BaseModel):
    review: str

@router.post("/review", response_model=ReviewResponse)
async def review_pr(request: ReviewRequest):
    try:

        diff_text = github_service.get_pr_diff(request.repo_name, request.pr_number)
        

        

        initial_state = {"diff": diff_text, "reviews": []}
        result = await app_graph.ainvoke(initial_state)
        
        final_review = result['reviews'][-1]
        
        return ReviewResponse(review=final_review)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
