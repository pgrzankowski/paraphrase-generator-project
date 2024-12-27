from .agents.paraphraser import paraphraser
from .agents.paraphraser import ParaphraserDeps, ParaphraserResult

class Assistant():
    def __init__(self):
        self._agent = paraphraser

    def get_response(self, to_paraphrase: str, prompt: str) -> ParaphraserResult:
        deps = ParaphraserDeps(to_paraphrase=to_paraphrase)
        response = self._agent.run_sync(user_prompt=prompt,
                                        deps=deps)
        # print("To paraphrase:\n", deps.to_paraphrase)
        # print("Paraphrased:\n", response.paraphrased)
        # print("Comment:\n", response.comment)
        return response.data
