from pydantic import BaseModel, Field, ValidationError
class TraineeProfile(BaseModel): 
    name: str
    years_experience: int = Field(..., ge=0, description="Years of experience must be a non-negative integer.")
    current_role: str
    target_role: str = "AI Engineer"
    skills: list[str] = [] 
    
good = '{"name": "Ana", "years_experience": 7, "current_role": "BA"}'

print(TraineeProfile.model_validate_json(good))

bad = '{"name": "Ana", "years_experience": -1, "current_role": "BA"}'
# Uncomment this to see how Pydantic raises a ValidationError for invalid data.
# print(TraineeProfile.model_validate_json(bad))  # raises ValidationError
# to catch the error, try this below : 
try:
    print(TraineeProfile.model_validate_json(bad))
except ValidationError as e:
    print("Validation error:", e)   
