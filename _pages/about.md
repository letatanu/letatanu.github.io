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

<span class='anchor' id='Publication'></span>
# Publications
<div style="display: flex; gap: 20px; margin-bottom: 25px; align-items: start;">
    
  <div style="flex: 0 0 150px;"> <img src="/assets/img/paper/aerorelief3d.png" 
         alt="Paper Teaser" 
         style="width: 100%; 
                height: 120px; 
                object-fit: contain;  /* <--- CHANGED THIS LINE */
                border: 1px solid #ddd; /* Optional: Adds a border to see the box limits */
                border-radius: 5px; 
                background-color: #f8f9fa;">
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
    </div>
    <!-- <div style="margin-top: 5px; font-size: 0.9em; color: #444;">
      <span class="show_paper_citations" data="1QRx2m4AAAAJ:u-x6o8ySG0sC"></span>
    </div> -->
    
  </div>

</div>
<div style="display: flex; gap: 20px; margin-bottom: 25px; align-items: start;">
  <div style="flex: 0 0 150px;"> <img src="/assets/img/paper/spie.png" 
         alt="Paper Teaser" 
        style="width: 100%; 
                height: 120px; 
                object-fit: contain;  /* <--- CHANGED THIS LINE */
                border: 1px solid #ddd; /* Optional: Adds a border to see the box limits */
                border-radius: 5px; 
                background-color: #f8f9fa;">
  </div>

  <div style="flex: 1;">
    <div style="font-size: 1.1em; font-weight: bold;">
      <a href="https://www.spiedigitallibrary.org/conference-proceedings-of-spie/13461/134610B/3D-semantic-segmentation-network-for-post-disaster-assessment-with-unmanned/10.1117/12.3053919.short">3D semantic segmentation network for post-disaster assessment with unmanned aerial vehicles</a>
    </div>
    <div style="margin-top: 5px;">
      <strong>Nhut Le</strong>, Maryam Rahnemoonfar
    </div>
    <div style="font-style: italic; color: #666;">
      Geospatial Informatics XV, 2025
    </div>
    <!-- <div style="margin-top: 5px; font-size: 0.9em; color: #444;">
      <span class="show_paper_citations" data="1QRx2m4AAAAJ:u-x6o8ySG0sC"></span>
    </div> -->
  </div>

</div>

<div style="display: flex; gap: 20px; margin-bottom: 25px; align-items: start;">
    
  <div style="flex: 0 0 150px;"> <img src="/assets/img/paper/igarss.png" 
         alt="Paper Teaser" 
         style="width: 100%; 
                height: 120px; 
                object-fit: contain;  /* <--- CHANGED THIS LINE */
                border: 1px solid #ddd; /* Optional: Adds a border to see the box limits */
                border-radius: 5px; 
                background-color: #f8f9fa;">
  </div>

  <div style="flex: 1;">
    <div style="font-size: 1.1em; font-weight: bold;">
      <a href="https://arxiv.org/abs/2512.24593">3D Semantic Segmentation for Post-Disaster Assessment
</a>
    </div>
    <div style="margin-top: 5px;">
      <strong>Nhut Le</strong>, Maryam Rahnemoonfar
    </div>
    <div style="font-style: italic; color: #666;">
    the 2025 IEEE International Geoscience and Remote Sensing Symposium (IGARSS 2025)    </div>
    <!-- <div style="margin-top: 5px; font-size: 0.9em; color: #444;">
      <span class="show_paper_citations" data="1QRx2m4AAAAJ:u-x6o8ySG0sC"></span>
    </div> -->
  </div>

</div>

<span class='anchor' id='education'></span>
# Educations
- *2024.08 - present*, &nbsp;PhD in Computer Science, Lehigh University.
- *2018.09 - 2020.08*, &nbsp;Master's in Computer Science, Portland State University.
- *2015.01 - 2018.06*, &nbsp;Bachelor in Computer Science, Portland State University.

<span class='anchor' id='experience'></span>
# Experience
- *2024.08 - present*, &nbsp;<strong>Research Assistant</strong> - Bina Lab, Lehigh University, Bethlehem, PA
  - Research 3D methodologies and machine learning to support disaster-affected areas \\
- *2020.10 - 2023.10*, &nbsp;<strong>Computer Vision Engineer</strong> - Sturfee, Inc., Remote
  - Developed, prototyped, and enhanced methods for 3D reconstruction and precise localization in the 3D prior map using Structure-from-Motion (SfM) and Multi-View Stereo (MVS) techniques, resulting in improving outdoor VPS and enabling indoor VPS
  - Implemented and optimized RGBD integration algorithms to reconstruct 3D point clouds and meshes, such as using TSDF volume integration and optimizing RGBD poses
  - Worked with deep learning networks for 3D semantic segmentation 
  - Proficient in 3D manipulations such as mesh texturing, texture baking, bundle adjustment, and UV unwrapping


<span class='anchor' id='honors-and-awards'></span>
# Honors and Awards
- *2015 - 2018*, &nbsp;International Achievement Scholarship, Portland State University
- *2010, 2011*, &nbsp;The Second place, Dong Thap Olympiad for High School Student Individual Contest in Math, Vietnam
- *2010*, &nbsp;Gold Medal, Mekong Delta Olympic in Math, Vietnam
- *2009*, &nbsp;Silver Medal, Olympic 30/4 in Math, Vietnam
<span class='anchor' id='projects'></span>
# Projects
<div style="display: flex; gap: 20px; margin-bottom: 25px; align-items: start;">
  <div style="flex: 0 0 200px; max-width: 200px;">
    <img src="/assets/img/project/example_5/predicted.gif" 
         alt="Homography Estimation" 
           style="width: 100%; 
                height: 120px; 
                object-fit: contain;  /* <--- CHANGED THIS LINE */
                border: 1px solid #ddd; /* Optional: Adds a border to see the box limits */
                border-radius: 5px; 
                background-color: #f8f9fa;">
  </div>
  <div style="flex: 1;">
    <div style="font-size: 1.1em; font-weight: bold;">
      <a href="https://github.com/letatanu/DeepHomography">Deep Image Homography Estimation</a>
    </div>
    <div style="margin-top: 5px; color: #666; font-size: 0.9em;">
      <strong>Stack:</strong> Python, Pytorch, OpenCV, Numpy, Matplotlib
    </div>
    <div style="margin-top: 10px; font-size: 0.95em; line-height: 1.4; color: #555; text-align: justify;">
      <ul>
        <li>Unofficial implementation of the paper <a href="https://arxiv.org/pdf/1606.03798.pdf">Deep Image Homography Estimation</a>.</li>
        <li>Estimates a 4-point homography parameterization which maps the four corners from one image into the second image.</li>
        <li>Achieved average corner error of 6.003 (train) and 6.034 (validation).</li>
      </ul>
    </div>
  </div>
</div>
<hr style="border-top: 1px dashed #ccc; margin: 20px 0;">

<div style="display: flex; gap: 20px; margin-bottom: 25px; align-items: start;">
  <div style="flex: 0 0 200px; max-width: 200px;">
    <img src="/assets/img/project/DeepF.gif" 
         alt="Deep Essential Matrix" 
          style="width: 100%; 
                height: 120px; 
                object-fit: contain;  /* <--- CHANGED THIS LINE */
                border: 1px solid #ddd; /* Optional: Adds a border to see the box limits */
                border-radius: 5px; 
                background-color: #f8f9fa;">
  </div>
  <div style="flex: 1;">
    <div style="font-size: 1.1em; font-weight: bold;">
      <a href="https://github.com/letatanu/DeepE_noCor_Pytorch">Deep Essential Matrix Estimation without Correspondences</a>
    </div>
    <div style="margin-top: 5px; color: #666; font-size: 0.9em;">
      <strong>Stack:</strong> Python, Pytorch, OpenCV, Numpy, Matplotlib
    </div>
    <div style="margin-top: 10px; font-size: 0.95em; line-height: 1.4; color: #555; text-align: justify;">
      <ul>
        <li>Estimates the essential matrix between two frames obtained by a monocular camera in epipolar geometry.</li>
        <li>Uses a ConvNet to directly estimate the matrix without detecting feature points (correlations) between images.</li>
      </ul>
    </div>
  </div>
</div>
<hr style="border-top: 1px dashed #ccc; margin: 20px 0;">

<div style="display: flex; gap: 20px; margin-bottom: 25px; align-items: start;">
  <div style="flex: 0 0 200px; max-width: 200px;">
    <img src="/assets/img/project/chess.gif" 
         alt="AI Chess" 
         style="width: 100%; 
                height: 120px; 
                object-fit: contain;  /* <--- CHANGED THIS LINE */
                border: 1px solid #ddd; /* Optional: Adds a border to see the box limits */
                border-radius: 5px; 
                background-color: #f8f9fa;">
  </div>
  <div style="flex: 1;">
    <div style="font-size: 1.1em; font-weight: bold;">
      <a href="https://github.com/letatanu/AI_Chess">AI Chess</a>
    </div>
    <div style="margin-top: 5px; color: #666; font-size: 0.9em;">
      <strong>Stack:</strong> Python, Numpy, Reinforcement Learning
    </div>
    <div style="margin-top: 10px; font-size: 0.95em; line-height: 1.4; color: #555; text-align: justify;">
      <ul>
        <li>Trained an agent to play chess against human players using reinforcement learning.</li>
        <li>The agent was trained on playing both sides (black and white) to reduce training time.</li>
        <li>Result: The agent wins 100/100 games against a Random agent.</li>
      </ul>
    </div>
  </div>
</div>
<hr style="border-top: 1px dashed #ccc; margin: 20px 0;">

<div style="display: flex; gap: 20px; margin-bottom: 25px; align-items: start;">
  <div style="flex: 0 0 200px; max-width: 200px;">
    <img src="/assets/img/project/minesweeper.gif" 
         alt="AI Minesweeper" 
           style="width: 100%; 
                height: 120px; 
                object-fit: contain;  /* <--- CHANGED THIS LINE */
                border: 1px solid #ddd; /* Optional: Adds a border to see the box limits */
                border-radius: 5px; 
                background-color: #f8f9fa;">
  </div>
  <div style="flex: 1;">
    <div style="font-size: 1.1em; font-weight: bold;">
      <a href="https://github.com/letatanu/AI_MineSweeper">AI MineSweeper</a>
    </div>
    <div style="margin-top: 5px; color: #666; font-size: 0.9em;">
      <strong>Stack:</strong> Python, Numpy, Reinforcement Learning
    </div>
    <div style="margin-top: 10px; font-size: 0.95em; line-height: 1.4; color: #555; text-align: justify;">
      <ul>
        <li>Reinforcement learning agent that plays Minesweeper.</li>
        <li>State representation in the Q-matrix is designed to allow transfer learning from small grids to larger grids.</li>
        <li>Agent trained on 5x5 grids can successfully play on 9x9 grids.</li>
      </ul>
    </div>
  </div>
</div>
<hr style="border-top: 1px dashed #ccc; margin: 20px 0;">

<div style="display: flex; gap: 20px; margin-bottom: 25px; align-items: start;">
  <div style="flex: 0 0 200px; max-width: 200px; display: flex; align-items: center; justify-content: center; background: #f8f9fa; border: 1px solid #ddd; border-radius: 5px; height: 120px;">
    <span style="color: #999; font-size: 0.9em;">iOS App</span>
  </div>
  <div style="flex: 1;">
    <div style="font-size: 1.1em; font-weight: bold;">
      <a href="https://github.com/letatanu/ColorID">Color ID</a>
    </div>
    <div style="margin-top: 5px; color: #666; font-size: 0.9em;">
      <strong>Stack:</strong> Swift, K-mean Clustering
    </div>
    <div style="margin-top: 10px; font-size: 0.95em; line-height: 1.4; color: #555; text-align: justify;">
      <ul>
        <li>iOS application that identifies the most dominant color in a photo from the gallery or camera.</li>
        <li>Utilizes K-mean machine learning algorithm to cluster colors and calculate the average value of the most popular group.</li>
      </ul>
    </div>
  </div>
</div>
<hr style="border-top: 1px dashed #ccc; margin: 20px 0;">

<div style="display: flex; gap: 20px; margin-bottom: 25px; align-items: start;">
  <div style="flex: 0 0 200px; max-width: 200px;">
    <img src="/assets/img/project/flappyBird.gif" 
         alt="Flappy Bird AI" 
           style="width: 100%; 
                height: 120px; 
                object-fit: contain;  /* <--- CHANGED THIS LINE */
                border: 1px solid #ddd; /* Optional: Adds a border to see the box limits */
                border-radius: 5px; 
                background-color: #f8f9fa;">
  </div>
  <div style="flex: 1;">
    <div style="font-size: 1.1em; font-weight: bold;">
      <a href="https://github.com/letatanu/FlappyBird-AI">Flappy Bird AI</a>
    </div>
    <div style="margin-top: 5px; color: #666; font-size: 0.9em;">
      <strong>Stack:</strong> Python, NEAT (Neuroevolution)
    </div>
    <div style="margin-top: 10px; font-size: 0.95em; line-height: 1.4; color: #555; text-align: justify;">
      <ul>
        <li>Uses Neuroevolution of Augmenting Topologies (NEAT) to train an agent to play Flappy Bird.</li>
        <li>The agent achieves perfect play (no losing) after just four generations of evolution.</li>
      </ul>
    </div>
  </div>
</div>
<hr style="border-top: 1px dashed #ccc; margin: 20px 0;">

<div style="display: flex; gap: 20px; margin-bottom: 25px; align-items: start;">
  <div style="flex: 0 0 200px; max-width: 200px;">
    <img src="/assets/img/project/imager.png" 
         alt="Imager App" 
           style="width: 100%; 
                height: 120px; 
                object-fit: contain;  /* <--- CHANGED THIS LINE */
                border: 1px solid #ddd; /* Optional: Adds a border to see the box limits */
                border-radius: 5px; 
                background-color: #f8f9fa;">
  </div>
  <div style="flex: 1;">
    <div style="font-size: 1.1em; font-weight: bold;">
      <a href="https://github.com/letatanu/Imager">Imager: Image Processing Web App</a>
    </div>
    <div style="margin-top: 5px; color: #666; font-size: 0.9em;">
      <strong>Stack:</strong> ReactJS, Django, OpenCV, Heroku
    </div>
    <div style="margin-top: 10px; font-size: 0.95em; line-height: 1.4; color: #555; text-align: justify;">
      <ul>
        <li>Full-stack web application for image processing (Palette generation and Filters).</li>
        <li><strong>Palette:</strong> Detects the n-most dominant colors in an image.</li>
        <li><strong>Filters:</strong> Applies Gaussian blur, detail enhancement, and grayscale effects.</li>
      </ul>
    </div>
  </div>
</div>


