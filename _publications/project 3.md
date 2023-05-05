---
title: "Disease Classification using Machine Learning"
collection: publications
permalink: /publication/project1
excerpt: 'Mukul Ganwal, <b>Balaji Praneeth Boga</b>, Aneesh Sinha.<br /><b>CMU-</b> 24787 Machine Learning and Artificial Intelligence for Engineers [2022]'

---

[[report]](https://drive.google.com/file/d/1qMTXv_fu_c8M2EPm1wNiyFBQXkHnjVqf/view?usp=share_link)


Introduction
======

Disease classification is a crucial task in healthcare that helps identify the type of disease a patient is suffering from based on their symptoms, medical history, and diagnostic test results. Traditional disease classification methods can be subjective and prone to human error, making it challenging for healthcare professionals to keep up with the latest developments in disease classification. This project aimed to provide an accurate prediction of a medical condition based on a set of symptoms using machine learning techniques.


Process
======

The project used a dataset of 1024 patients with 133 symptoms and 42 diseases as labels to evaluate various machine learning models such as Random Forest, Support Vector Machine, K-Means, Gaussian Naive Bayes and Logistic Regression. The methodology involved benchmarking the dataset on different models such as Decision Tree Classifier, Random Forest Classifier, Support Vector Classifier, and Logistic Regression. The accuracy of each model was used to compare their performance. Feature engineering and optimal hyperparameter tuning were used to improve the accuracy of the best-performing model.


Results
======

The results showed that Random Forest Classifier was the best performing model with an accuracy of 99%, followed by Support Vector Machine with 98%, Decision Tree Classifier with 95%, and Logistic Regression with 68%. Feature engineering and optimal hyperparameter tuning helped to remove redundant features and improve the accuracy of the Random Forest Classifier. The optimal number of trees and depth obtained from hyperparameter tuning were 24 and 14 respectively. The accuracy of the Random Forest Classifier decreased to 99% after feature engineering, but the number of features put into use decreased to 99 from 133, making the model more efficient to work on larger data.


Conclusion
======

This project provides an effective approach for accurate disease diagnosis based on symptoms using machine learning techniques. The results highlight the importance of understanding the dataset, evaluating it against various models, and using feature engineering and hyperparameter tuning to improve the accuracy of the model. The use of Random Forest Classifier as the best model with an accuracy of 99% for this dataset provides a promising solution for healthcare settings
