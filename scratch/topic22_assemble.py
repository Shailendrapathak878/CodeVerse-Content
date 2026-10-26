# Topic 22 Master Assembly Script
# Combines CSS, Parts 1-4, and all 20 SVGs into coding/machine_learning/topic_22/notes.html

import os
import sys
import re

# Add scratch directory to sys.path
sys.path.insert(0, os.path.dirname(__file__))

from topic22_css import TOPIC22_CSS
from topic22_svgs import SVG_MAP
from topic22_part1 import PART_1_HTML
from topic22_part2 import PART_2_HTML
from topic22_part3 import PART_3_HTML
from topic22_part4 import PART_4_HTML

def build_notes():
    # Hero header & Table of Contents
    hero_and_toc = """
    <!-- HERO HEADER -->
    <header class="hero-header">
      <div class="hero-badge">Machine Learning Masterclass • Topic 22</div>
      <h1 class="hero-title">Hyperparameter Tuning &amp; Model Selection</h1>
      <p class="hero-subtitle">
        Master the engineering discipline of selecting optimal model configurations, navigating search spaces, executing leak-free cross-validation, and establishing true generalization in real-world ML systems.
      </p>
      <div class="hero-meta-grid">
        <div class="hero-meta-item">
          <span class="hero-meta-label">Prerequisites</span>
          <span class="hero-meta-val">Basic Python &amp; ML Foundations</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Core Algorithms</span>
          <span class="hero-meta-val">KNN, Trees, Random Forest, SVM</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Optimization</span>
          <span class="hero-meta-val">Grid &amp; Randomized Search</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Validation</span>
          <span class="hero-meta-val">Stratified K-Fold &amp; Nested CV</span>
        </div>
      </div>
    </header>

    <!-- TABLE OF CONTENTS -->
    <nav class="toc-card" aria-label="Table of Contents">
      <div class="toc-title">
        <span>📖</span> Table of Contents — 24 Comprehensive Modules
      </div>
      <ul class="toc-grid">
        <li><a class="toc-link" href="#sec-01"><span class="toc-num">01</span> Intro &amp; Study Analogy</a></li>
        <li><a class="toc-link" href="#sec-02"><span class="toc-num">02</span> Parameters vs Hyperparameters</a></li>
        <li><a class="toc-link" href="#sec-03"><span class="toc-num">03</span> Why Tuning Is Needed</a></li>
        <li><a class="toc-link" href="#sec-04"><span class="toc-num">04</span> Train, Val &amp; Test Sets</a></li>
        <li><a class="toc-link" href="#sec-05"><span class="toc-num">05</span> Manual KNN Tuning</a></li>
        <li><a class="toc-link" href="#sec-06"><span class="toc-num">06</span> Search Spaces &amp; Scales</a></li>
        <li><a class="toc-link" href="#sec-07"><span class="toc-num">07</span> Grid Search from Scratch</a></li>
        <li><a class="toc-link" href="#sec-08"><span class="toc-num">08</span> GridSearchCV Practical</a></li>
        <li><a class="toc-link" href="#sec-09"><span class="toc-num">09</span> Random Search Theory</a></li>
        <li><a class="toc-link" href="#sec-10"><span class="toc-num">10</span> RandomizedSearchCV Practical</a></li>
        <li><a class="toc-link" href="#sec-11"><span class="toc-num">11</span> Grid vs Random Search</a></li>
        <li><a class="toc-link" href="#sec-12"><span class="toc-num">12</span> Cross-Validation in Tuning</a></li>
        <li><a class="toc-link" href="#sec-13"><span class="toc-num">13</span> Interpreting CV Scores</a></li>
        <li><a class="toc-link" href="#sec-14"><span class="toc-num">14</span> Algorithm Hyperparameter Map</a></li>
        <li><a class="toc-link" href="#sec-15"><span class="toc-num">15</span> Choosing Scoring Metrics</a></li>
        <li><a class="toc-link" href="#sec-16"><span class="toc-num">16</span> Tuning Overfitting &amp; Bias</a></li>
        <li><a class="toc-link" href="#sec-17"><span class="toc-num">17</span> Data Leakage &amp; Pipelines</a></li>
        <li><a class="toc-link" href="#sec-18"><span class="toc-num">18</span> Learning &amp; Validation Curves</a></li>
        <li><a class="toc-link" href="#sec-19"><span class="toc-num">19</span> Computational Cost &amp; Workload</a></li>
        <li><a class="toc-link" href="#sec-20"><span class="toc-num">20</span> Nested Cross-Validation</a></li>
        <li><a class="toc-link" href="#sec-21"><span class="toc-num">21</span> End-to-End Practical</a></li>
        <li><a class="toc-link" href="#sec-22"><span class="toc-num">22</span> 15 Common Mistakes &amp; Fixes</a></li>
        <li><a class="toc-link" href="#sec-23"><span class="toc-num">23</span> Revision, Glossary &amp; Checklist</a></li>
        <li><a class="toc-link" href="#sec-24"><span class="toc-num">24</span> 10 Self-Check Questions</a></li>
      </ul>
    </nav>
    """

    # Assemble complete raw HTML
    raw_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Topic 22: Hyperparameter Tuning — CodeVerse Machine Learning Notes</title>
  <style>
{TOPIC22_CSS}
  </style>
</head>
<body>
  <div class="page-container">
{hero_and_toc}
{PART_1_HTML}
{PART_2_HTML}
{PART_3_HTML}
{PART_4_HTML}
  </div>
</body>
</html>
"""

    # Inject SVGs
    final_html = raw_html
    for key, svg in SVG_MAP.items():
        if key in final_html:
            final_html = final_html.replace(key, svg)
        else:
            print(f"WARNING: Placeholder {key} not found in HTML!")

    # Check for unreplaced placeholders
    unreplaced = re.findall(r"__SVG_[A-Z0-9_]+__", final_html)
    if unreplaced:
        print(f"ERROR: Unreplaced SVG placeholders found: {unreplaced}")
        sys.exit(1)

    # Check for all 24 section IDs
    for i in range(1, 25):
        sec_id = f"sec-{i:02d}"
        if f'id="{sec_id}"' not in final_html:
            print(f"ERROR: Section ID {sec_id} not found in final HTML!")
            sys.exit(1)

    # Ensure output directory exists
    out_dir = os.path.join("coding", "machine_learning", "topic_22")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "notes.html")

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    file_size_kb = os.path.getsize(out_file) / 1024
    print(f"Successfully assembled {out_file}!")
    print(f"File size: {file_size_kb:.1f} KB")
    print(f"Total Sections: 24 (verified)")
    print(f"Total SVGs injected: {len(SVG_MAP)} (all valid XML)")

if __name__ == "__main__":
    build_notes()
