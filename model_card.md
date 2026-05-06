# Model Card: Mood Machine

This model card describes the Mood Machine project, which includes two approaches to sentiment classification:

1. A rule based model implemented in `mood_analyzer.py`
2. A machine learning model implemented in `ml_experiments.py` using scikit-learn

---

## 1. Model Overview

**Model type:**  
Both models were implemented and compared: a rule based classifier and a simple machine learning classifier.

**Intended purpose:**  
The system classifies short text messages into four categories: positive, negative, neutral, or mixed.

**How it works (brief):**  
The rule based model uses predefined lists of positive and negative words and applies scoring logic with simple rules such as negation handling and mixed sentiment detection.  

The ML model converts text into numerical vectors using a bag-of-words representation and learns patterns from labeled examples using a Naive Bayes classifier.

---

## 2. Data

**Dataset description:**  
The dataset consists of short text posts stored in `SAMPLE_POSTS`, each paired with a label in `TRUE_LABELS`. Additional posts were added to include slang, emojis, sarcasm, and mixed emotions.

**Labeling process:**  
Labels were manually assigned based on interpretation of each sentence. Some examples were ambiguous, especially those with mixed emotions or sarcasm, which made labeling subjective.

**Important characteristics of the dataset:**

- Includes slang such as "lowkey" and "highkey"
- Contains emojis such as 😂 and 💀
- Includes sarcasm and indirect expressions
- Some posts contain mixed emotions
- Contains short and ambiguous phrases

**Possible issues with the dataset:**

- Small dataset size
- Subjective labeling
- Lack of balanced examples across all categories
- Limited vocabulary coverage

---

## 3. How the Rule Based Model Works

**Your scoring rules:**

- Positive words increase score
- Negative words decrease score
- Negation words ("not", "no", "never") invert meaning
- If both positive and negative signals appear, the label becomes "mixed"
- Score thresholds determine final label

**Strengths of this approach:**

- Transparent and easy to understand
- Predictable behavior
- Works well for clear, simple sentences

**Weaknesses of this approach:**

- Cannot detect sarcasm reliably
- Struggles with slang and informal language
- Limited by predefined vocabulary
- Difficult to scale for complex language

---

## 4. How the ML Model Works

**Features used:**  
Bag-of-words representation using CountVectorizer.

**Training data:**  
The model is trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  
The model achieved 100% accuracy on the dataset, but this was misleading because it was evaluated on the same data it was trained on.

**Strengths and weaknesses:**

Strengths:
- Learns patterns automatically from data
- Can capture relationships not explicitly coded

Weaknesses:
- Overfits easily on small datasets
- Depends heavily on training data quality
- Does not generalize well to unseen inputs
- Difficult to interpret compared to rule-based logic

---

## 5. Evaluation

**How you evaluated the model:**  
Both models were evaluated using the labeled dataset.

- Rule based model accuracy improved from ~0.50 to ~0.75 after refining rules and word lists
- ML model achieved 1.00 accuracy on the dataset but failed on new inputs

**Examples of correct predictions:**

- "I love this class so much" → positive  
- "Today was a terrible day" → negative  
- "This is fine" → neutral  

**Examples of incorrect predictions:**

- "I absolutely love getting stuck in traffic" → interpreted incorrectly due to sarcasm  
- "Lowkey stressed but I think I got this" → misclassified due to mixed tone  
- "happy" → incorrectly classified by ML model despite being clearly positive  

---

## 6. Limitations

- Small dataset size limits learning ability  
- Model does not generalize well to new inputs  
- Rule-based system lacks flexibility  
- ML model overfits training data  
- Cannot reliably detect sarcasm or cultural context  
- Performance heavily depends on dataset quality  

---

## 7. Ethical Considerations

- Misclassification of emotional content could lead to incorrect conclusions  
- Different language styles or communities may be unfairly interpreted  
- Privacy concerns when analyzing personal text data  
- Risk of overconfidence in model predictions  

---

## 8. Ideas for Improvement

- Expand dataset with more diverse examples  
- Improve preprocessing for emojis and slang  
- Use TF-IDF instead of simple counts  
- Add a validation/test split instead of training-only evaluation  
- Improve mixed sentiment detection  
- Explore more advanced models such as neural networks  

---

## 9. Key Insight

The ML model achieved 100% accuracy on the dataset but failed on new inputs, showing that it memorized the training data rather than learning generalizable patterns.

This demonstrates that high accuracy does not necessarily indicate a strong or reliable model.