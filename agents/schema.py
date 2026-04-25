from pydantic import BaseModel, Field

class PostOutput(BaseModel):
    bot_id: str
    topic: str
    post_content: str = Field(max_length=280)