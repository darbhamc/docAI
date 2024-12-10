from sklearn.metrics import precision_score, recall_score, f1_score
import numpy as np

def compute_entity_metrics(predicted_entities, actual_entities):
    """
    Compute precision, recall, and F1-score for entity extraction.

    :param predicted_entities: List of predicted entities from Document AI API
    :param actual_entities: List of actual entities (ground truth)
    :return: Precision, Recall, F1-Score
    """
    # Convert to set for unique entities
    predicted_set = set(predicted_entities)
    actual_set = set(actual_entities)

    # True positives (correctly predicted entities)
    true_positives = len(predicted_set & actual_set)

    # False positives (predicted but not actual)
    false_positives = len(predicted_set - actual_set)

    # False negatives (actual but not predicted)
    false_negatives = len(actual_set - predicted_set)

    # Precision = TP / (TP + FP)
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0

    # Recall = TP / (TP + FN)
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0

    # F1-Score = 2 * (Precision * Recall) / (Precision + Recall)
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return precision, recall, f1


def evaluate_entity_extraction(predicted_entities, actual_entities):
    """
    Evaluate the entity extraction capabilities of Google Document AI API.

    :param predicted_entities: List of predicted entities from Document AI API
    :param actual_entities: List of actual entities (ground truth)
    :return: Evaluation metrics for entity extraction
    """
    precision, recall, f1 = compute_entity_metrics(predicted_entities, actual_entities)

    print("Evaluation Metrics for Entity Extraction:")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")


def evaluate_token_level_accuracy(predicted_text, actual_text):
    """
    Compute the token-level accuracy by comparing predicted text with actual text.

    :param predicted_text: The text recognized by the Document AI API
    :param actual_text: The ground truth text
    :return: Token-level accuracy
    """
    predicted_tokens = predicted_text.split()
    actual_tokens = actual_text.split()

    correct_tokens = sum([1 for p, a in zip(predicted_tokens, actual_tokens) if p == a])
    total_tokens = len(actual_tokens)

    token_accuracy = correct_tokens / total_tokens if total_tokens > 0 else 0

    print(f"Token-Level Accuracy: {token_accuracy:.4f}")


# Example: Integrating these metrics with your Document AI processing flow

# Define the ground truth and predicted entities (this should come from your test set or API response)
# Actual entities are the entities in the document (could come from manually labeled data).
# Predicted entities are the entities recognized by the Document AI API.

# Sample data (replace with actual values from Document AI output)
predicted_entities = ["invoice_number", "total_amount", "date"]
actual_entities = ["invoice_number", "total_amount", "date", "purchase_order"]

# Example of actual and predicted text
predicted_text = "Invoice Number: 1234, Total Amount: $100, Date: 2023-11-15"
actual_text = "Invoice Number: 1234, Total Amount: $100, Date: 2023-11-15"

# Compute entity-level metrics
evaluate_entity_extraction(predicted_entities, actual_entities)

# Compute token-level accuracy
evaluate_token_level_accuracy(predicted_text, actual_text)
