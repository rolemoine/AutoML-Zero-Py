from dataclasses import dataclass
from typing import Any


@dataclass
class TaskBuffer:
    consummed_: bool
    train_features_: Any
    valid_features_: Any
    eval_type_: Any
    train_labels_: Any
    valid_labels_: Any
