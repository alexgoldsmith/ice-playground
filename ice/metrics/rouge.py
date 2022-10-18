from anyio.to_thread import run_sync
from pydantic import BaseModel
from rouge_metric import PyRouge

from ice.metrics.base import Metric
from ice.metrics.base import Sample


class _RougeScore(BaseModel):
    r: float
    p: float
    f: float

    def __str__(self):
        return f"recall: {self.r:.2f}, precision: {self.p:.2f}, f1: {self.f:.2f}"


class RougeResult(BaseModel):
    rouge_1: _RougeScore
    rouge_2: _RougeScore
    rouge_3: _RougeScore
    rouge_l: _RougeScore

    class Config:
        alias_generator = lambda n: n.replace("_", "-")  # noqa: E731

    def __str__(self):
        return "\n\n".join(
            [
                f"* Rouge L: {self.rouge_l}",
                f"* Rouge 1: {self.rouge_1}",
                f"* Rouge 2: {self.rouge_2}",
                f"* Rouge 3: {self.rouge_3}",
            ]
        )


class Rouge(Metric):
    name = "Rouge"

    def __init__(
        self, n: tuple[int, ...] = (1, 2, 3), rouge_l: bool = True, rouge_w: bool = True
    ):
        self.rouge = PyRouge(rouge_n=n, rouge_l=rouge_l, rouge_w=rouge_w)

    async def compute(self, sample: list[Sample]) -> list[RougeResult]:
        async def _compute_single(sample: Sample) -> RougeResult:
            hyp = sample.left
            ref = [sample.right for _ in sample.left]

            result_dict = await run_sync(
                lambda: self.rouge.evaluate(hyp, ref), cancellable=True
            )
            return RougeResult.parse_obj(result_dict)

        return [await (_compute_single(s)) for s in sample]
