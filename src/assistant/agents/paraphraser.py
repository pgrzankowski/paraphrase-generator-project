from pydantic_ai import Agent, RunContext
from pydantic import BaseModel, Field
from dataclasses import dataclass
from dotenv import load_dotenv
import os
from ..prompts.prompts import PARAPHRASER_PROMPT


load_dotenv()
MODEL = os.getenv("MODEL")


@dataclass
class ParaphraserDeps:
    to_paraphrase: str

class ParaphraserResult(BaseModel):
    paraphrased: str = Field(description="Paraphrased text.")
    comment: str = Field(description="Comment about paraphrased text to the user.")

paraphraser = Agent(model=MODEL,
                    deps_type=ParaphraserDeps)

@paraphraser.system_prompt
def system_prompt(ctx: RunContext[ParaphraserDeps]) -> str:
    to_paraphrase = ctx.deps.to_paraphrase
    return PARAPHRASER_PROMPT.format(to_paraphrase=to_paraphrase)
