from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.idea_validator.validator_engine import ValidatorEngine
import traceback

router = APIRouter()


class IdeaRequest(BaseModel):
    idea: str


@router.post("/validate-idea")
async def validate_idea(request: IdeaRequest):
    try:
        engine = ValidatorEngine()
        result = engine.evaluate(request.idea)

        return {
            "final_viability_score": result["final_viability_score"],
            "problem": result["problem"].model_dump(),
            "market": result["market"].model_dump(),
            "competition": result["competition"].model_dump(),
            "differentiation": result["differentiation"].model_dump(),
            "mvp": result["mvp"].model_dump(),
            "monetization": result["monetization"].model_dump(),
            "risk": result["risk"].model_dump(),
        }
    except Exception as e:
        print(f"Error: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))