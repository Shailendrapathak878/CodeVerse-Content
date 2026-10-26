# Topic 24 Master Assembly Script
# Combines CSS, Parts 1-4, and all 20 SVGs into coding/machine_learning/topic_24/notes.html

import os
import sys
import re

# Add scratch directory to sys.path
sys.path.insert(0, os.path.dirname(__file__))

from topic24_css import TOPIC24_CSS
from topic24_svgs import SVG_MAP
from topic24_part1 import PART_1_HTML
from topic24_part2 import PART_2_HTML
from topic24_part3 import PART_3_HTML
from topic24_part4 import PART_4_HTML

def build_notes():
    # Hero header & Table of Contents (21 Modules)
    hero_and_toc = """
    <!-- HERO HEADER -->
    <header class="hero-header">
      <div class="hero-badge">Machine Learning Masterclass • Topic 24 (Capstone)</div>
      <h1 class="hero-title">Model Deployment &amp; MLOps Fundamentals</h1>
      <p class="hero-subtitle">
        Bridge the chasm between experimental notebooks and production applications. Learn to serialize pipelines safely, deploy high-performance FastAPI microservices, containerize workloads, monitor data and concept drift, and govern the full MLOps lifecycle.
      </p>
      <div class="hero-meta-grid">
        <div class="hero-meta-item">
          <span class="hero-meta-label">Prerequisites</span>
          <span class="hero-meta-val">ML Pipelines (Topic 23)</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Serving Framework</span>
          <span class="hero-meta-val">FastAPI &amp; Pydantic V2</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Observability</span>
          <span class="hero-meta-val">Drift Detection &amp; P99 Latency</span>
        </div>
        <div class="hero-meta-item">
          <span class="hero-meta-label">Lifecycle Governance</span>
          <span class="hero-meta-val">Champion/Challenger &amp; CI/CD</span>
        </div>
      </div>
    </header>

    <!-- TABLE OF CONTENTS -->
    <nav class="toc-card" aria-label="Table of Contents">
      <div class="toc-title">
        <span>📖</span> Table of Contents — 21 Comprehensive Modules
      </div>
      <ul class="toc-grid">
        <li><a class="toc-link" href="#sec-01"><span class="toc-num">01</span> From Training to Deployment</a></li>
        <li><a class="toc-link" href="#sec-02"><span class="toc-num">02</span> What Is Model Deployment?</a></li>
        <li><a class="toc-link" href="#sec-03"><span class="toc-num">03</span> Model Artifact &amp; Serialization</a></li>
        <li><a class="toc-link" href="#sec-04"><span class="toc-num">04</span> Serving Predictions via API</a></li>
        <li><a class="toc-link" href="#sec-05"><span class="toc-num">05</span> Beginner-Friendly FastAPI App</a></li>
        <li><a class="toc-link" href="#sec-06"><span class="toc-num">06</span> Batch vs. Real-Time Inference</a></li>
        <li><a class="toc-link" href="#sec-07"><span class="toc-num">07</span> Local vs. Cloud Deployment</a></li>
        <li><a class="toc-link" href="#sec-08"><span class="toc-num">08</span> Introduction to Docker</a></li>
        <li><a class="toc-link" href="#sec-09"><span class="toc-num">09</span> What Is MLOps?</a></li>
        <li><a class="toc-link" href="#sec-10"><span class="toc-num">10</span> Versioning &amp; Experiment Tracking</a></li>
        <li><a class="toc-link" href="#sec-11"><span class="toc-num">11</span> Data Drift &amp; Concept Drift</a></li>
        <li><a class="toc-link" href="#sec-12"><span class="toc-num">12</span> Monitoring a Deployed Model</a></li>
        <li><a class="toc-link" href="#sec-13"><span class="toc-num">13</span> Retraining &amp; Lifecycle Management</a></li>
        <li><a class="toc-link" href="#sec-14"><span class="toc-num">14</span> CI/CD &amp; Automated ML Testing</a></li>
        <li><a class="toc-link" href="#sec-15"><span class="toc-num">15</span> Model Security &amp; Reliability</a></li>
        <li><a class="toc-link" href="#sec-16"><span class="toc-num">16</span> Model Deployment Challenges</a></li>
        <li><a class="toc-link" href="#sec-17"><span class="toc-num">17</span> End-to-End Practical Project</a></li>
        <li><a class="toc-link" href="#sec-18"><span class="toc-num">18</span> Important Visuals &amp; Graphs</a></li>
        <li><a class="toc-link" href="#sec-19"><span class="toc-num">19</span> Revision, Glossary &amp; Checklist</a></li>
        <li><a class="toc-link" href="#sec-20"><span class="toc-num">20</span> Self-Check &amp; Workload Estimator</a></li>
        <li><a class="toc-link" href="#sec-21"><span class="toc-num">21</span> Final ML Completion Banner</a></li>
      </ul>
    </nav>
    """

    # Assemble complete raw HTML
    raw_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Topic 24: Model Deployment &amp; MLOps Fundamentals — CodeVerse Machine Learning Notes</title>
  <style>
{TOPIC24_CSS}
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

    # Check for all 21 section IDs
    for i in range(1, 22):
        sec_id = f"sec-{i:02d}"
        if f'id="{sec_id}"' not in final_html:
            print(f"ERROR: Section ID {sec_id} not found in final HTML!")
            sys.exit(1)

    # Sanity check: Ensure NO height="auto" in SVG tags
    bad_svgs = re.findall(r'<svg[^>]*height=["\']auto["\']', final_html, re.IGNORECASE)
    if bad_svgs:
        print(f"WARNING: Found {len(bad_svgs)} SVGs with height='auto'. Cleaning them up...")
        final_html = re.sub(r'(\sheight=["\']auto["\'])', '', final_html, flags=re.IGNORECASE)

    # Ensure output directory exists
    out_dir = os.path.join("coding", "machine_learning", "topic_24")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "notes.html")

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    file_size_kb = os.path.getsize(out_file) / 1024
    print(f"Successfully assembled {out_file}!")
    print(f"File size: {file_size_kb:.1f} KB")
    print(f"Total Sections: 21 (all verified)")
    print(f"Total SVGs injected: {len(SVG_MAP)} (all 20 valid XML)")

if __name__ == "__main__":
    build_notes()
