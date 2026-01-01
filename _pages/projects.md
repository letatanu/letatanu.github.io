---
layout: default
title: "Projects"
permalink: /projects/
author_profile: true
---
<link rel="stylesheet" href="/assets/css/project-styles.css">
<script src="/assets/js/project-scripts.js" defer></script>

<div class="projects-container">
<body id="page-top">
        <!-- Page Content-->
        <div class="container-fluid p-0">
            <!-- Project-->
            <div class="resume-section-content">
                <h2 class="mb-5">Projects</h2>
                <div class="d-flex flex-column flex-md-row justify-content-between mb-5">
                    <div class="flex-grow-1">
                        <h3 class="mb-0"><a href="https://github.com/letatanu/DeepHomography">Deep Image Homography Estimation</a></h3>
                        <div class="subheading mb-3">Python/Pytorch/OpenCV/Numpy/Matplotlib</div>
                        <ul class="lead">
                            <li>
                                This project is the unofficial implementation of the paper
                                <a href="https://arxiv.org/pdf/1606.03798.pdf">Deep Image Homography Estimation</a>
                            </li>
                            <li>A homography is a mapping from a projective space (image) P to Q</li>
                            <li>From this network, it will estimate a 4-point homography parameterization which maps the four corners from one image into the second image</li>
                            <li>As a result, the average corner error is</li>
                            <ul>
                                <li>6.003 for the train set</li>
                                <li>6.034 for the validation set</li>
                            </ul>
                        </ul>
                        <ul class="list-group list-group-horizontal-sm">
                            <li class="list-group-item">
                                <figure>
                                    <img class="img-fluid img-thumbnail img-responsive rounded mb-2" src="assets/img/project/example_5/origin.png" alt="origin" />
                                    <figcaption><p>Example</p></figcaption>
                                </figure>
                            </li>
                            <li class="list-group-item">
                                <figure>
                                    <img class="img-fluid img-thumbnail img-responsive rounded mb-2" src="assets/img/project/example_5/result.png" alt="result" />
                                    <figcaption><p>Result</p></figcaption>
                                </figure>
                            </li>
                            <li class="list-group-item">
                                <figure>
                                    <img class="img-fluid img-thumbnail img-responsive rounded mb-2" src="assets/img/project/example_5/patch.png" alt="patch" />
                                    <figcaption><p>Patch</p></figcaption>
                                </figure>
                            </li>
                            <li class="list-group-item">
                                <figure>
                                    <img class="img-fluid img-thumbnail img-responsive rounded mb-2" src="assets/img/project/example_5/gt.gif" alt="groundTruth" />
                                    <figcaption><p>Ground Truth</p></figcaption>
                                </figure>
                            </li>
                            <li class="list-group-item">
                                <figure>
                                    <img class="img-fluid img-thumbnail img-responsive rounded mb-2" src="assets/img/project/example_5/predicted.gif" alt="predicted" />
                                    <figcaption><p>Predicted Result</p></figcaption>
                                </figure>
                            </li>
                        </ul>
                        <ul class="list-group list-group-horizontal-sm">
                            <li class="list-group-item">
                                <figure>
                                    <img class="img-fluid img-thumbnail img-responsive rounded mb-2" src="assets/img/project/example_6/origin.png" alt="origin" />
                                    <figcaption><p>Example</p></figcaption>
                                </figure>
                            </li>
                            <li class="list-group-item">
                                <figure>
                                    <img class="img-fluid img-thumbnail img-responsive rounded mb-2" src="assets/img/project/example_6/result.png" alt="result" />
                                    <figcaption><p>Result</p></figcaption>
                                </figure>
                            </li>
                            <li class="list-group-item">
                                <figure>
                                    <img class="img-fluid img-thumbnail img-responsive rounded mb-2" src="assets/img/project/example_6/patch.png" alt="patch" />
                                    <figcaption><p>Patch</p></figcaption>
                                </figure>
                            </li>
                            <li class="list-group-item">
                                <figure>
                                    <img class="img-fluid img-thumbnail img-responsive rounded mb-2" src="assets/img/project/example_6/gt.gif" alt="groundTruth" />
                                    <figcaption><p>Ground Truth</p></figcaption>
                                </figure>
                            </li>
                            <li class="list-group-item">
                                <figure>
                                    <img class="img-fluid img-thumbnail img-responsive rounded mb-2" src="assets/img/project/example_6/predicted.gif" alt="predicted" />
                                    <figcaption><p>Predicted Result</p></figcaption>
                                </figure>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="d-flex flex-column flex-md-row justify-content-between mb-5">
                    <div class="flex-grow-1">
                        <h3 class="mb-0"><a href="https://github.com/letatanu/DeepE_noCor_Pytorch">Deep Essential Matrix Estimation without Correspondences</a></h3>
                        <div class="subheading mb-3">Python/Pytorch/OpenCV/Numpy/Matplotlib</div>
                        <ul class="lead">
                            <li>Estimating the essential matrix between two frames obtained by a monocular camera in the epipolar geometry.</li>
                            <li>The designed ConvNet can directly estimate the essential matrix without detecting feature points (correlations) between the two input images.</li>
                            <li>In the test set, the visualizing results looked incredible</li>
                        </ul>
                        <img class="center img-fluid img-thumbnail img-responsive rounded mb-2" src="assets/img/project/DeepF.gif" alt="demo" />
                    </div>
                </div>
                <div class="d-flex flex-column flex-md-row justify-content-between mb-5">
                    <div class="flex-grow-1">
                        <h3 class="mb-0"><a href="https://github.com/letatanu/AI_Chess">AI Chess</a></h3>
                        <div class="subheading mb-3">Python/Numpy/Reinforcement Learning</div>
                        <ul class="lead">
                            <li>Training an agent that can play chess v.s human players by using reinforcement learning.</li>
                            <li>The agent was trained on both sides of the player, which reduces the training time by half.</li>
                            <li>As a result, the agent wins 100/100 games v.s the Random agent</li>
                        </ul>
                        <img class="center img-fluid img-thumbnail img-responsive rounded mb-2" src="assets/img/project/chess.gif" alt="demo" />
                    </div>
                </div>
                <div class="d-flex flex-column flex-md-row justify-content-between mb-5">
                    <div class="flex-grow-1">
                        <h3 class="mb-0"><a href="https://github.com/letatanu/AI_MineSweeper">AI MineSweeper</a></h3>
                        <div class="subheading mb-3">Python/Numpy/Reinforcement Learning</div>
                        <ul class="lead">
                            <li>Training an agent that can play minesweeper itself by using reinforcement learning.</li>
                            <li>The state in the Q-matrix is re-defined so that the agent trained in small sizes of the grid can play on grids with larger sizes.</li>
                            <li>As a result, the agent trained in random 5x5 grids with three mines can win 16/1000 random games of 9x9 grids with ten mines</li>
                        </ul>
                        <img class="center img-fluid img-thumbnail img-responsive rounded mb-2" src="assets/img/project/minesweeper.gif" alt="demo" />
                    </div>
                </div>
                <div class="d-flex flex-column flex-md-row justify-content-between mb-5">
                    <div class="flex-grow-1">
                        <h3 class="mb-0"><a href="https://github.com/letatanu/ColorID">Color ID</a></h3>
                        <div class="subheading mb-3">Swift/K-mean</div>
                        <ul class="lead">
                            <li>An iOS application gives the name of the most dominant color in the given image, which is obtained from the photo gallery or camera on the iOS devices.</li>
                            <li>It utilizes a machine learning algorithm called k-mean to cluster colors into groups, then takes the average of color values in the most popular group to give the color result.</li>
                            <li>Its extension being developed is to provide the palette of the n-dominant colors from the given image</li>
                        </ul>
                    </div>
                </div>
                <div class="d-flex flex-column flex-md-row justify-content-between mb-5">
                    <div class="flex-grow-1">
                        <h3 class="mb-0"><a href="https://github.com/letatanu/FlappyBird-AI">Flappy Bird AI</a></h3>
                        <div class="subheading mb-3">Python/NEAT</div>
                        <ul class="lead">
                            <li>Using Neuroevolution of augmenting topologies - NEAT to train the agent that can play Flappy Bird itself</li>
                            <li>After four generations, the agent can play the Flappy Bird game well without losing</li>
                        </ul>
                        <img class="h-75 img-fluid img-thumbnail img-responsive rounded" src="assets/img/project/flappyBird.gif" alt="demo" />
                    </div>
                </div>
                <div class="d-flex flex-column flex-md-row justify-content-between mb-5">
                    <div class="flex-grow-1">
                        <h3 class="mb-0"><a href="https://github.com/letatanu/Imager">Imager</a></h3>
                        <div class="subheading mb-3">ReactJS/Django/OpenCV/Heroku/Computer Vision</div>
                        <ul class="lead">
                            <li>The full-stack web application for image processing</li>
                            <li>It has two main functions: generate a palette for and apply filters to the given images</li>
                            <ul>
                                <li>Palette generation detects n-most dominant colors</li>
                                <li>The applying filters are Gaussian, detail enhances, and grayscale</li>
                            </ul>
                        </ul>
                        <ul class="list-group list-group-horizontal-sm">
                            <li class="list-group-item"><img class="img-fluid img-thumbnail img-responsive rounded mb-2" src="assets/img/project/imager.png" alt="Palette" /></li>
                            <li class="list-group-item"><img class="img-fluid img-thumbnail rounded mb-2" src="assets/img/project/filter.png" alt="Filter" /></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <!-- Bootstrap core JS-->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.bundle.min.js"></script>
        <!-- Third party plugin JS-->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.min.js"></script>
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
    </body>
</div>