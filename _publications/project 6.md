---
title: "Variability in Performance of SOTA models in Object Detection towards Synthetic Dataset"
collection: publications
permalink: /publication/project6
excerpt: 'Niranjan Kumawat, Mangalam Sahai, <b>Balaji Praneeth Boga</b>, Alexander Lyons.<br /><b>CMU-</b> 16824 Visual Learning and Recognition [2023]'

---

[[report]](https://drive.google.com/file/d/1Q297GuqGtTjWjuGzbk4fqn0LgDlw_WD4/view?usp=drive_link)


Introduction
======

Detecting objects in cluttered indoor environments is a crucial functionality for service robots. The best performing object detection approaches in Computer Vision leverage State-Of-The-Art (SOTA) models to simultaneously detect and categorize objects of interest in these scenes. We intend to conduct a comparative study to assess the performance of these models on images cluttered with similar unwanted objects. Our goal is to differentiate between reallife objects and objects painted on posters. To carry out this study, we aimed to create a synthetic dataset of indoor scenes augmented with various objects on posters and subsequently analyze the performance of five SOTA models on this dataset. We found that performance did vary across the five models when using this dataset, showing there is a need for datasets to train and test the robustness of SOTA models when dealing with objects in posters.

Process
======

* <h2>Greedy Poster Placement</h2>
<figure>
  <img src="/images/Greedy poster placement.png" style="width:600px;height:300px;">
</figure>

* <h2>Greedy Poster Placement Result</h2>
<figure>
  <img src="/images/Greedy placement.png" style="width:600px;height:300px;">
</figure>

* <h2>Warping the Poster on the Wall </h2>
<figure>
  <img src="/images/Poster impose.png" style="width:600px;height:300px;">
</figure>

* <h2>Robustness Score</h2>
<figure>
  <img src="/images/Robustness Score.png" style="width:600px;height:300px;">
</figure>

* <h2>Robustness Score Results</h2>
<figure>
  <img src="/images/Results_VLR.png" style="width:600px;height:300px;">
  <img src="/images/Robustness figures.png" style="width:600px;height:300px;">
  <img src="/images/Exp3 RS.png" style="width:600px;height:300px;">
</figure>


Results
======

The results of Experiment 1 have shown that YOLO was the best performing model since it had a median robustness score across the results obtained from different thresholds of approximately 0.98, and a minimum score of 0.875. The second best performing model was SSD300, which yielded a median robustness score of approximately 0.97, but with a higher minimum score of approximately 0.925. Therefore, YOLO had a better best score, but SSD300 had a better worst score. 

The results of Experiment 2 have shown that SSD300 was the best performing model, as it had a median robustness score of approximately 0.98, and a minimum score
of 0.875. The second best performing model was YOLO, which yielded a median robustness score of approximately 0.9, but with a lower minimum score of approximately 0.7. Therefore, SSD300 had a better best score, but YOLO had a better worst score.

Discussion
======

The primary goal of our comparative study is to lay the groundwork for fine-tuning different SOTA models to disregard poster images when classifying real objects in an image. In the baseline study we showed which specific hyperparameters for each model produced the best top three F1 scores for each setting. Using these hyper-parameters, we ran the models against three different sets of poster tests. The general trend across all the experiments was that SSD300 and YOLO performed the best, then FCOS and RetinaNet performed worse, and Faster R-CNN performed the worst. From our empirical results, we have shown that SSD300 and YOLO are the most robust towards images containing posters.

The comparisons yielded from these experiments are not meant to be used for effectively comparing the models, but rather showing that different models do in fact exhibit different behavior when interacting with posters in images. Therefore, future work involves completing a full evaluation of which models are best at avoiding detecting objects in posters by using a larger dataset.

Other future work would be to experiment with a larger variety of data. For example, using more than one image for each class of poster objects. Another example would be adding posters to more images besides indoor scenes, such as road-scenes, which would allow for one to test object detection models used in self-driving vehicles. 
