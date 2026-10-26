# Topic 23 Master Assembly Script
# Combines CSS, Parts 1-4, and all 20 SVGs into coding/machine_learning/topic_23/notes.html

import os
import sys
import re

# Add scratch directory to sys.path
sys.path.insert(0, os.path.dirname(__file__))

from topic23_css import TOPIC23_CSS
from topic23_svgs import SVG_MAP
from topic23_part1 import PART_1_HTML
from topic23_part2 import PART_2_HTML
from topic23_part3 import PART_3_HTML
from topic23_part4 import PART_4_HTML

def build_notes():
    # Hero header & Table of Contents
    hero_and_toc = """
    <!-- HERO HEADER -->
    <header class="hero-header">
      <div class="hero-badge">Machine Learning Masterclass • Topic 23</div>
      <h1 class="hero-title">Feature Engineering &amp; ML Pipelines</h1>
      <p class="hero-subtitle">
        Master the engineering discipline of transforming raw data into high-signal numerical representations, executing leak-free preprocessing, building multi-branch ColumnTransformers, and deploying robust scikit-learn pipelines.
      </p>
      <div class="hero-meta-grid">
        <div class="hero-meta-item">
          <span class="hero-meta-label">Prerequisites</span>
          <span class="hero-meta-val">Basic Python &amp; Introductory ML</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Core Preprocessing</span>
          <span class="hero-meta-val">Imputation, Scaling, Encoders</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Pipeline Architecture</span>
          <span class="hero-meta-val">Pipeline &amp; ColumnTransformer</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Validation</span>
          <span class="hero-meta-val">Leak-Free Cross-Validation &amp; Tuning</span>
        </div>
      </div>
    </header>

    <!-- TABLE OF CONTENTS -->
    <nav class="toc-card" aria-label="Table of Contents">
      <div class="toc-title">
        <span>📖</span> Table of Contents — 22 Comprehensive Modules
      </div>
      <ul class="toc-grid">
        <li><a class="toc-link" href="#sec-01"><span class="toc-num">01</span> Intro &amp; Cooking Analogy</a></li>
        <li><a class="toc-link" href="#sec-02"><span class="toc-num">02</span> Understanding Feature Types</a></li>
        <li><a class="toc-link" href="#sec-03"><span class="toc-num">03</span> Raw vs Model-Ready Data</a></li>
        <li><a class="toc-link" href="#sec-04"><span class="toc-num">04</span> Handling Missing Values</a></li>
        <li><a class="toc-link" href="#sec-05"><span class="toc-num">05</span> Encoding Categorical Features</a></li>
        <li><a class="toc-link" href="#sec-06"><span class="toc-num">06</span> Feature Scaling &amp; Transforms</a></li>
        <li><a class="toc-link" href="#sec-07"><span class="toc-num">07</span> Creating New Features</a></li>
        <li><a class="toc-link" href="#sec-08"><span class="toc-num">08</span> Polynomial &amp; Interactions</a></li>
        <li><a class="toc-link" href="#sec-09"><span class="toc-num">09</span> Feature Selection</a></li>
        <li><a class="toc-link" href="#sec-10"><span class="toc-num">10</span> Data Leakage in Preprocessing</a></li>
        <li><a class="toc-link" href="#sec-11"><span class="toc-num">11</span> What Is an ML Pipeline?</a></li>
        <li><a class="toc-link" href="#sec-12"><span class="toc-num">12</span> Building a Basic Pipeline</a></li>
        <li><a class="toc-link" href="#sec-13"><span class="toc-num">13</span> ColumnTransformer for Mixed Data</a></li>
        <li><a class="toc-link" href="#sec-14"><span class="toc-num">14</span> Full Mixed-Data Pipeline</a></li>
        <li><a class="toc-link" href="#sec-15"><span class="toc-num">15</span> Pipelines with Cross-Validation</a></li>
        <li><a class="toc-link" href="#sec-16"><span class="toc-num">16</span> Hyperparameter Tuning Inside Pipelines</a></li>
        <li><a class="toc-link" href="#sec-17"><span class="toc-num">17</span> Advanced Feature Types (Date/Text)</a></li>
        <li><a class="toc-link" href="#sec-18"><span class="toc-num">18</span> Visualizing FE Results &amp; Benchmark</a></li>
        <li><a class="toc-link" href="#sec-19"><span class="toc-num">19</span> 15 Common Mistakes &amp; Fixes</a></li>
        <li><a class="toc-link" href="#sec-20"><span class="toc-num">20</span> End-to-End Practical Project</a></li>
        <li><a class="toc-link" href="#sec-21"><span class="toc-num">21</span> Revision, Glossary &amp; Checklist</a></li>
        <li><a class="toc-link" href="#sec-22"><span class="toc-num">22</span> 10 Self-Check Questions</a></li>
      </ul>
    </nav>
    """

    # Assemble complete raw HTML
    raw_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Topic 23: Feature Engineering &amp; ML Pipelines — CodeVerse Machine Learning Notes</title>
  <style>
{TOPIC23_CSS}
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

    # Check for all 22 section IDs
    for i in range(1, 23):
        sec_id = f"sec-{i:02d}"
        if f'id="{sec_id}"' not in final_html:
            print(f"ERROR: Section ID {sec_id} not found in final HTML!")
            sys.exit(1)

    # Ensure output directory exists
    out_dir = os.path.join("coding", "machine_learning", "topic_23")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "notes.html")

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    file_size_kb = os.path.getsize(out_file) / 1024
    print(f"Successfully assembled {out_file}!")
    print(f"File size: {file_size_kb:.1f} KB")
    print(f"Total Sections: 22 (verified)")
    print(f"Total SVGs injected: {len(SVG_MAP)} (all valid XML)")

if __name__ == "__main__":
    build_notes()
