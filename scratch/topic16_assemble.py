"""Assemble Topic 16 complete notes.html from modular components.
"""
import os
import re
import sys

sys.path.insert(0, os.path.abspath("."))

from scratch.topic16_css import TOPIC16_CSS
from scratch.topic16_svgs import (
    SVG_CLUSTERING_OVERVIEW,
    SVG_CLUSTERING_VS_CLASSIFICATION,
    SVG_EUCLIDEAN_VS_MANHATTAN,
    SVG_SCALING_EFFECT,
    SVG_KMEANS_STEPS_PANEL,
    SVG_KMEANS_CENTROIDS_FINAL,
    SVG_ELBOW_METHOD,
    SVG_SILHOUETTE_ANALYSIS,
    SVG_K_VALUES_GRID,
    SVG_KMEANS_LIMITATIONS,
    SVG_LINKAGE_COMPARISON,
    SVG_DENDROGRAM,
    SVG_DENDROGRAM_CUTS,
    SVG_DBSCAN_CONCEPTS,
    SVG_DBSCAN_CLUSTERS_NOISE,
    SVG_DBSCAN_EPS_COMPARISON,
    SVG_KMEANS_VS_DBSCAN,
    SVG_METRICS_COMPARISON
)
from scratch.topic16_part1 import TOPIC16_PART1
from scratch.topic16_part2 import TOPIC16_PART2
from scratch.topic16_part3 import TOPIC16_PART3
from scratch.topic16_part4 import TOPIC16_PART4

def assemble_notes():
    print("Assembling Topic 16 notes.html...")
    
    body_content = TOPIC16_PART1 + "\n" + TOPIC16_PART2 + "\n" + TOPIC16_PART3 + "\n" + TOPIC16_PART4
    
    svg_map = {
        "__SVG_CLUSTERING_OVERVIEW__": SVG_CLUSTERING_OVERVIEW,
        "__SVG_CLUSTERING_VS_CLASSIFICATION__": SVG_CLUSTERING_VS_CLASSIFICATION,
        "__SVG_EUCLIDEAN_VS_MANHATTAN__": SVG_EUCLIDEAN_VS_MANHATTAN,
        "__SVG_SCALING_EFFECT__": SVG_SCALING_EFFECT,
        "__SVG_KMEANS_STEPS_PANEL__": SVG_KMEANS_STEPS_PANEL,
        "__SVG_KMEANS_CENTROIDS_FINAL__": SVG_KMEANS_CENTROIDS_FINAL,
        "__SVG_ELBOW_METHOD__": SVG_ELBOW_METHOD,
        "__SVG_SILHOUETTE_ANALYSIS__": SVG_SILHOUETTE_ANALYSIS,
        "__SVG_K_VALUES_GRID__": SVG_K_VALUES_GRID,
        "__SVG_KMEANS_LIMITATIONS__": SVG_KMEANS_LIMITATIONS,
        "__SVG_LINKAGE_COMPARISON__": SVG_LINKAGE_COMPARISON,
        "__SVG_DENDROGRAM__": SVG_DENDROGRAM,
        "__SVG_DENDROGRAM_CUTS__": SVG_DENDROGRAM_CUTS,
        "__SVG_DBSCAN_CONCEPTS__": SVG_DBSCAN_CONCEPTS,
        "__SVG_DBSCAN_CLUSTERS_NOISE__": SVG_DBSCAN_CLUSTERS_NOISE,
        "__SVG_DBSCAN_EPS_COMPARISON__": SVG_DBSCAN_EPS_COMPARISON,
        "__SVG_KMEANS_VS_DBSCAN__": SVG_KMEANS_VS_DBSCAN,
        "__SVG_METRICS_COMPARISON__": SVG_METRICS_COMPARISON,
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
  <title>Topic 16: Clustering &mdash; CodeVerse Machine Learning</title>
  <style>
{TOPIC16_CSS}
  </style>
</head>
<body>
{body_content}
</body>
</html>
"""
    
    out_dir = os.path.join("coding", "machine_learning", "topic_16")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "notes.html")
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    file_size_kb = os.path.getsize(out_path) / 1024
    print(f"SUCCESS: Assembled Topic 16 notes at '{out_path}' ({file_size_kb:.2f} KB)")

if __name__ == "__main__":
    assemble_notes()
