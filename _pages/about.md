---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am a second-year PhD student in Computer Science at Lehigh University, advised by Prof. <a href="https://engineering.lehigh.edu/faculty/maryam-rahnemoonfar">Maryam Rahnemoonfar</a>. My current research  interest lies in deep learning and computer vision, and their application in 3D reconstruction, 3D rendering and 3D semantic segmentation.

Previously, I had been working as a 3D computer vision engineer at <a href="https://sturfee.com/">Sturfee, Inc.</a> for three years. My work focused on 3D reconstruction and 3D localization to improve the performance and accuracy of Visual Positioning System (VPS). I received my M.S. and B.S. in Computer Science at Portland State University.

<a href="https://github.com/letatanu/letatanu.github.io/blob/dc6686ad4505e0555d8f0a599bf8e90523818e54/files/NhutLe_Resume.pdf">Download resume</a>

<span class='anchor' id='news'></span>
# 🔥 News
- *2024.08.12*: &nbsp;First-day at Lehigh University as a PhD student.  

<span class='anchor' id='education'></span>
# Educations
- *2024.08 - present*, &nbsp;PhD in Computer Science, Lehigh University.
- *2018.09 - 2020.08*, &nbsp;Master's in Computer Science, Portland State University.
- *2015.01 - 2018.06*, &nbsp;Bachelor in Computer Science, Portland State University.

<span class='anchor' id='experience'></span>
# Experience
- *2020.10 - 2023.10*, &nbsp;Computer Vision Engineer - Sturfee, Inc., Remote
  - Developed, prototyped, and enhanced methods for 3D reconstruction and precise localization in the 3D prior map using Structure-from-Motion (SfM) and Multi-View Stereo (MVS) techniques, resulting in improving outdoor VPS and enabling indoor VPS
  - Implemented and optimized RGBD integration algorithms to reconstruct 3D point clouds and meshes, such as using TSDF volume integration and optimizing RGBD poses
  - Worked with deep learning networks for 3D semantic segmentation 
  - Proficient in 3D manipulations such as mesh texturing, texture baking, bundle adjustment, and UV unwrapping

<h1 id="projects">Projects</h1> 
<div class="projects-container"></div>

<span class='anchor' id='Publication'></span>
# Publications
<div style="display: flex; gap: 20px; margin-bottom: 25px; align-items: start;">
    
  <div style="flex: 0 0 150px;"> <img src="/assets/img/paper/aerorelief3d.png" 
         alt="Paper Teaser" 
         style="width: 100%; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
  </div>

  <div style="flex: 1;">
    <div style="font-size: 1.1em; font-weight: bold;">
      <a href="https://arxiv.org/pdf/2509.11097">3DAeroRelief: The first 3D Benchmark UAV Dataset for Post-Disaster Assessment</a>
    </div>
    
    <div style="margin-top: 5px;">
      <strong>Nhut Le</strong>, Ehsan Karimi, Maryam Rahnemoonfar
    </div>
    
    <div style="font-style: italic; color: #666;">
    2025
      <!-- Conference on Computer Vision and Pattern Recognition (CVPR), 2024 -->
    </div>
    
    <div style="margin-top: 5px; font-size: 0.9em; color: #444;">
      <span class="show_paper_citations" data="1QRx2m4AAAAJ:u-x6o8ySG0sC"></span>
    </div>
  </div>

</div>

<span class='anchor' id='honors-and-awards'></span>
# Honors and Awards
- *2015 - 2018*, &nbsp;International Achievement Scholarship, Portland State University
- *2010, 2011*, &nbsp;The Second place, Dong Thap Olympiad for High School Student Individual Contest in Math, Vietnam
- *2010*, &nbsp;Gold Medal, Mekong Delta Olympic in Math, Vietnam
- *2009*, &nbsp;Silver Medal, Olympic 30/4 in Math, Vietnam

