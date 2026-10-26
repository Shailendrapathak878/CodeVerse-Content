"""Assemble Topic 17 complete notes.html from modular components.
"""
import os
import re
import sys

sys.path.insert(0, os.path.abspath("."))

from scratch.topic17_css import TOPIC17_CSS
from scratch.topic17_svgs import (
    SVG_DIMENSIONALITY_OVERVIEW,
    SVG_SELECTION_VS_EXTRACTION,
    SVG_CURSE_OF_DIMENSIONALITY,
    SVG_PCA_INTUITION_AXES,
    SVG_PROJECTION_2D_TO_1D,
    SVG_PCA_PIPELINE_FLOW,
    SVG_EXPLAINED_VARIANCE_SCREE,
    SVG_CUMULATIVE_VARIANCE_CURVE,
    SVG_PCA_2D_SCATTER,
    SVG_PCA_3D_ISOMETRIC,
    SVG_MODEL_PERFORMANCE_COMPARISON,
    SVG_TSNE_VISUALIZATION,
    SVG_UMAP_CONCEPTS,
    SVG_PCA_VS_LDA,
    SVG_METHODS_COMPARISON_GRID,
    SVG_DECISION_FLOWCHART
)
from scratch.topic17_part1 import TOPIC17_PART1
from scratch.topic17_part2 import TOPIC17_PART2
from scratch.topic17_part3 import TOPIC17_PART3
from scratch.topic17_part4 import TOPIC17_PART4

def assemble_notes():
    print("Assembling Topic 17 notes.html...")
    
    body_content = TOPIC17_PART1 + "\n" + TOPIC17_PART2 + "\n" + TOPIC17_PART3 + "\n" + TOPIC17_PART4
    
    svg_map = {
        "__SVG_DIMENSIONALITY_OVERVIEW__": SVG_DIMENSIONALITY_OVERVIEW,
        "__SVG_SELECTION_VS_EXTRACTION__": SVG_SELECTION_VS_EXTRACTION,
        "__SVG_CURSE_OF_DIMENSIONALITY__": SVG_CURSE_OF_DIMENSIONALITY,
        "__SVG_PCA_INTUITION_AXES__": SVG_PCA_INTUITION_AXES,
        "__SVG_PROJECTION_2D_TO_1D__": SVG_PROJECTION_2D_TO_1D,
        "__SVG_PCA_PIPELINE_FLOW__": SVG_PCA_PIPELINE_FLOW,
        "__SVG_EXPLAINED_VARIANCE_SCREE__": SVG_EXPLAINED_VARIANCE_SCREE,
        "__SVG_CUMULATIVE_VARIANCE_CURVE__": SVG_CUMULATIVE_VARIANCE_CURVE,
        "__SVG_PCA_2D_SCATTER__": SVG_PCA_2D_SCATTER,
        "__SVG_PCA_3D_ISOMETRIC__": SVG_PCA_3D_ISOMETRIC,
        "__SVG_MODEL_PERFORMANCE_COMPARISON__": SVG_MODEL_PERFORMANCE_COMPARISON,
        "__SVG_TSNE_VISUALIZATION__": SVG_TSNE_VISUALIZATION,
        "__SVG_UMAP_CONCEPTS__": SVG_UMAP_CONCEPTS,
        "__SVG_PCA_VS_LDA__": SVG_PCA_VS_LDA,
        "__SVG_METHODS_COMPARISON_GRID__": SVG_METHODS_COMPARISON_GRID,
        "__SVG_DECISION_FLOWCHART__": SVG_DECISION_FLOWCHART,
    }
    
    for placeholder, svg in svg_map.items():
        assert placeholder in body_content, f"Missing placeholder in body: {placeholder}"
        body_content = body_content.replace(placeholder, svg)
        print(f"Substituted: {placeholder}")
        
    remaining = re.findall(r'__SVG_[A-Z0-9_]+__', body_content)
    assert len(remaining) == 0, f"Unresolved SVG placeholders found: {remaining}"
    
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Topic 17: Dimensionality Reduction &mdash; CodeVerse Machine Learning</title>
  <style>
{TOPIC17_CSS}
  </style>
</head>
<body>
{body_content}
</body>
</html>
"""
    
    out_dir = os.path.join("coding", "machine_learning", "topic_17")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "notes.html")
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    file_size_kb = os.path.getsize(out_path) / 1024
    print(f"SUCCESS: Assembled Topic 17 notes at '{out_path}' ({file_size_kb:.2f} KB)")

if __name__ == "__main__":
    assemble_notes()
