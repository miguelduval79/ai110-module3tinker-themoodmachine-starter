# mood_analyzer.py

from typing import List, Optional
from dataset import POSITIVE_WORDS, NEGATIVE_WORDS


class MoodAnalyzer:
    """
    A simple rule-based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:

        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------
    # Preprocessing
    # ---------------------------

    def preprocess(self, text: str) -> List[str]:
        cleaned = text.strip().lower()
        tokens = cleaned.split()
        return tokens

    # ---------------------------
    # Scoring logic
    # ---------------------------

    def score_text(self, text: str) -> int:
        tokens = self.preprocess(text)
        score = 0

        for i, token in enumerate(tokens):
            prev = tokens[i - 1] if i > 0 else ""

            # positive words
            if token in self.positive_words:
                if prev in {"not", "no", "never"}:
                    score -= 1
                else:
                    score += 1

            # negative words
            elif token in self.negative_words:
                if prev in {"not", "no", "never"}:
                    score += 1
                else:
                    score -= 1

        return score

    # ---------------------------
    # Label prediction
    # ---------------------------

    def predict_label(self, text: str) -> str:
        tokens = self.preprocess(text)

        has_positive = False
        has_negative = False

        for i, token in enumerate(tokens):
            prev = tokens[i - 1] if i > 0 else ""

            if token in self.positive_words:
                if prev in {"not", "no", "never"}:
                    has_negative = True
                else:
                    has_positive = True

            elif token in self.negative_words:
                if prev in {"not", "no", "never"}:
                    has_positive = True
                else:
                    has_negative = True

        # 🔥 NEW: detect mixed sentiment
        if has_positive and has_negative:
            return "mixed"

        score = self.score_text(text)

        if score > 0:
            return "positive"
        elif score < 0:
            return "negative"
        else:
            return "neutral"

    # ---------------------------
    # Explanation (optional)
    # ---------------------------

    def explain(self, text: str) -> str:
        tokens = self.preprocess(text)

        positive_hits = []
        negative_hits = []
        score = 0

        for i, token in enumerate(tokens):
            prev = tokens[i - 1] if i > 0 else ""

            if token in self.positive_words:
                positive_hits.append(token)
                score += 1

            if token in self.negative_words:
                negative_hits.append(token)
                score -= 1

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or []}, "
            f"negative: {negative_hits or []})"
        )