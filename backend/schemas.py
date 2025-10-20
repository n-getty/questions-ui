from enum import Enum
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class SystemStatus(str, Enum):
    disabled = "disabled"
    ready = "ready"
    starting = "starting"

class StatusSchema(BaseModel):
    authoring: SystemStatus

class History(BaseModel):
    question_id: int
    review_id: Optional[int]
    question: str
    action: str
    modified: datetime
class CreateAuthorSchema(BaseModel):
    name: str
    affilliation: str
    position: str = ""
    orcid: Optional[str] = None
    class Config:
        from_attributes = True
class SkipSchema(BaseModel):
    author: CreateAuthorSchema|int
    question_id: int
    class Config:
        from_attributes = True
class ReviewerSchema(BaseModel):
    author: CreateAuthorSchema|int
    domains: list[str]
    class Config:
        from_attributes = True
class CreateReviewSchema(BaseModel):
    author: CreateAuthorSchema|int
    question_id: int
    questionrelevent: int
    questionfromarticle: int
    questionindependence: int
    questionchallenging: int
    answerrelevent: int
    answercomplete: int
    answerfromarticle: int
    answerunique: int
    answeruncontroverial: int
    arithmaticfree: int
    skillcorrect: int
    domaincorrect: int
    comments: str
    accept: bool
    class Config:
        from_attributes = True
class ReviewSchema(BaseModel):
    id: int
    author: CreateAuthorSchema|int
    question_id: int
    questionrelevent: int
    questionfromarticle: int
    questionindependence: int
    questionchallenging: int
    answerrelevent: int
    answercomplete: int
    answerfromarticle: int
    answerunique: int
    answeruncontroverial: int
    arithmaticfree: int
    skillcorrect: int
    domaincorrect: int
    comments: str
    accept: bool
    class Config:
        from_attributes = True
class AuthorSchema(BaseModel):
    id: int
    name: str
    affilliation: str = ""
    position: str = ""
    orcid: Optional[str] = None
    class Config:
        from_attributes = True
class CreateQuestionSchema(BaseModel):
    question: str
    correct_answer: str
    distractors: list[str]
    skills: list[str]
    domains: list[str]
    difficulty: str
    doi: str
    author: CreateAuthorSchema|int
    support: str = ""
    comments: str = ""
    class Config:
        from_attributes = True
class QuestionSchema(BaseModel):
    id: Optional[int] = None
    question: str
    correct_answer: str
    distractors: list[str]
    skills: list[str]
    domains: list[str]
    difficulty: str
    doi: str
    author: int|CreateAuthorSchema
    support: str = ""
    comments: str = ""
    class Config:
        from_attributes = True
class QuestionEvalSchema(BaseModel):
    model: str
    score: float
    correct: bool
    corectlogprobs: str
    incorrectlogprobs: str
    class Config:
        from_attributes = True
class ContributionsSchema(BaseModel):
    num_questions : int
    num_validated : int
    num_reviews : int
    class Config:
        from_attributes = True

class AiExperienceLevelSchema(BaseModel):
    id: int
    description: str
    class Config:
        from_attributes = True


class AuthorExperienceSchema(BaseModel):
    author_id: AuthorSchema|int
    ai_experience_level: AiExperienceLevelSchema|int
    class Config:
        from_attributes = True

class CreateAiSkillSchema(BaseModel):
    name: str
    description: str
    level: int|str
    class Config:
        from_attributes = True

class CreateJustifiedAiSkill(BaseModel):
    score: CreateAiSkillSchema
    justification: str
    class Config:
        from_attributes = True

class AiSkillSchema(BaseModel):
    id: int
    name: str
    description: str
    skill_category: int
    level: int
    class Config:
        from_attributes = True

class AiSkillCategorySchema(BaseModel):
    id: int
    name: str
    description: str
    class Config:
        from_attributes = True

class CreateFinalEvaluationSchema(BaseModel):
    experiment_id: int
    overall: Optional[CreateJustifiedAiSkill]
    novelty: Optional[CreateJustifiedAiSkill]
    productivity: Optional[CreateJustifiedAiSkill]
    teamwork: Optional[CreateJustifiedAiSkill]
    completeness: Optional[CreateJustifiedAiSkill]
    productivity_improvement: Optional[str]
    event_improvement: str
    daily_use: str
    main_strength: str
    main_weakness: str
    class Config:
        from_attributes = True

class FinalEvaluationSchema(BaseModel):
    id: int
    overall: AiSkillSchema|int
    novelty: AiSkillSchema|int
    productivity: AiSkillSchema|int
    teamwork: AiSkillSchema|int
    completeness: AiSkillSchema|int
    overall_justification: str
    novelty_justification: str
    productivity_justification: str
    teamwork_justification: str
    completeness_justification: str
    productivity_improvement: str
    event_improvement: str
    class Config:
        from_attributes = True

class CreateExperimentLogSchema(BaseModel):
    author_id: AuthorSchema|int
    class Config:
        from_attributes = True

class ExperimentLogSchema(BaseModel):
    id: int
    author_id: AuthorSchema|int
    preliminary_evaluation_id: int
    final_evaluation_id: FinalEvaluationSchema|int
    class Config:
        from_attributes = True

class CreateExperimentTurnSchema(BaseModel):
    experiment_id: int
    previous_turn: Optional[int]
    goal: str
    prompt: str
    output: str
    other_task: str
    other_task_assessment: str
    files_url: str

    analysis: CreateJustifiedAiSkill
    conclusions: CreateJustifiedAiSkill
    hypothesis: CreateJustifiedAiSkill
    planning: CreateJustifiedAiSkill
    review: CreateJustifiedAiSkill
    understanding: CreateJustifiedAiSkill

    class Config:
        from_attributes = True

class ExperimentTurnSchema(BaseModel):
    id: int
    experiment_id: ExperimentLogSchema|int
    previous_turn: int
    turn: str
    goal: str
    prompt: str
    discussion: str
    class Config:
        from_attributes = True

class CreatePreliminaryEvaluationSchema(BaseModel):
    experiment_id: int
    title: str
    description: str
    model: str
    goal: str
    difficulty_explaination: str
    realism: str
    comments: str
    experience: CreateAiSkillSchema
    reasoning_experience: CreateAiSkillSchema
    difficulty: CreateAiSkillSchema
    class Config:
        from_attributes = True

class PreliminaryEvaluationSchema(BaseModel):
    id: int
    title: str
    description: str
    difficulty: AiSkillSchema|int
    class Config:
        from_attributes = True

class ExperimentTurnEvaluationSchema(BaseModel):
    turn_id: ExperimentTurnSchema|int
    skill_id: AiSkillSchema|int
    skill_level: str 
    class Config:
        from_attributes = True

class ExperimentFile(BaseModel):
    turn_id: int
    contents: list[int]
    filename: str


class LoginSchema(BaseModel):
    password: str
class TokenSchema(BaseModel):
    token: str

class ReviewRemainingItem(BaseModel):
    key: str
    count: int
class ReviewRemaining(BaseModel):
    values: list[ReviewRemainingItem]

class DomainResponse(BaseModel):
    name: str
    id: int

class Suggestion(BaseModel):
    suggestion: str

class SuggestionRequest(BaseModel):
    prompt: str
    system_prompt: str
