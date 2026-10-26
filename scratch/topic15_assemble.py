"""
Topic 15: Ensemble Learning - Assembler Script
Combines CSS, 17 XML-valid SVGs, and 4 Content Parts into the complete notes.html.
Strict Light Mode Only.
"""

import os
import sys
sys.path.insert(0, ".")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import re
from scratch.topic15_css import TOPIC_15_CSS
from scratch.topic15_svgs import (
    SVG_ENSEMBLE_PIPELINE,
    SVG_SINGLE_VS_ENSEMBLE,
    SVG_VOTING_COMPARISON,
    SVG_BOOTSTRAP_SAMPLING,
    SVG_BAGGING_DECISION_BOUNDARY,
    SVG_RANDOM_FOREST_ARCHITECTURE,
    SVG_RF_DECISION_BOUNDARIES,
    SVG_RF_TREES_CURVE,
    SVG_ADABOOST_SEQUENTIAL,
    SVG_GRADIENT_BOOSTING_ADDITIVE,
    SVG_BOOSTING_STAGES_CURVE,
    SVG_BAGGING_VS_BOOSTING,
    SVG_STACKING_ARCHITECTURE,
    SVG_CLASSIFICATION_BENCHMARK,
    SVG_REGRESSION_ACTUAL_PRED,
    SVG_FEATURE_IMPORTANCE,
    SVG_TRAIN_VS_VAL_OVERFIT
)
from scratch.topic15_part1 import TOPIC_15_PART1
from scratch.topic15_part2 import TOPIC_15_PART2
from scratch.topic15_part3 import TOPIC_15_PART3
from scratch.topic15_part4 import TOPIC_15_PART4

SVG_MAP = {
    "__SVG_ENSEMBLE_PIPELINE__": SVG_ENSEMBLE_PIPELINE,
    "__SVG_SINGLE_VS_ENSEMBLE__": SVG_SINGLE_VS_ENSEMBLE,
    "__SVG_VOTING_COMPARISON__": SVG_VOTING_COMPARISON,
    "__SVG_BOOTSTRAP_SAMPLING__": SVG_BOOTSTRAP_SAMPLING,
    "__SVG_BAGGING_DECISION_BOUNDARY__": SVG_BAGGING_DECISION_BOUNDARY,
    "__SVG_RANDOM_FOREST_ARCHITECTURE__": SVG_RANDOM_FOREST_ARCHITECTURE,
    "__SVG_RF_DECISION_BOUNDARIES__": SVG_RF_DECISION_BOUNDARIES,
    "__SVG_RF_TREES_CURVE__": SVG_RF_TREES_CURVE,
    "__SVG_ADABOOST_SEQUENTIAL__": SVG_ADABOOST_SEQUENTIAL,
    "__SVG_GRADIENT_BOOSTING_ADDITIVE__": SVG_GRADIENT_BOOSTING_ADDITIVE,
    "__SVG_BOOSTING_STAGES_CURVE__": SVG_BOOSTING_STAGES_CURVE,
    "__SVG_BAGGING_VS_BOOSTING__": SVG_BAGGING_VS_BOOSTING,
    "__SVG_STACKING_ARCHITECTURE__": SVG_STACKING_ARCHITECTURE,
    "__SVG_CLASSIFICATION_BENCHMARK__": SVG_CLASSIFICATION_BENCHMARK,
    "__SVG_REGRESSION_ACTUAL_PRED__": SVG_REGRESSION_ACTUAL_PRED,
    "__SVG_FEATURE_IMPORTANCE__": SVG_FEATURE_IMPORTANCE,
    "__SVG_TRAIN_VS_VAL_OVERFIT__": SVG_TRAIN_VS_VAL_OVERFIT,
}

HTML_HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Topic 15: Ensemble Learning &bull; CodeVerse Machine Learning</title>
  <style>
""" + TOPIC_15_CSS + """
  </style>
</head>
<body>
  <div class="container">
"""

HTML_FOOTER = """
  </div>
</body>
</html>
"""

def assemble_notes():
    print("Assembling Topic 15 notes.html...")
    raw_content = TOPIC_15_PART1 + TOPIC_15_PART2 + TOPIC_15_PART3 + TOPIC_15_PART4
    
    # Replace all SVG placeholders
    for placeholder, svg_code in SVG_MAP.items():
        if placeholder in raw_content:
            raw_content = raw_content.replace(placeholder, svg_code)
            print(f"Replaced placeholder {placeholder}")
        else:
            print(f"WARNING: Placeholder {placeholder} not found in content!")

    # Check for any remaining placeholders
    remaining = re.findall(r'__SVG_[A-Z0-9_]+__', raw_content)
    if remaining:
        print(f"ERROR: Remaining unreplaced placeholders: {remaining}")
    else:
        print("All 17 SVG placeholders successfully replaced.")

    full_html = HTML_HEADER + raw_content + HTML_FOOTER
    
    target_dir = os.path.join("coding", "machine_learning", "topic_15")
    os.makedirs(target_dir, exist_ok=True)
    target_file = os.path.join(target_dir, "notes.html")

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"Topic 15 notes.html successfully written to {target_file}")
    print(f"Total HTML file size: {len(full_html)} characters, {len(full_html.encode('utf-8'))} bytes.")

if __name__ == "__main__":
    assemble_notes()
