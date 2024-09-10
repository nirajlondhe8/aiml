# Anomaly Detection and Model Comparison in Network Data

**Author**  
Niraj Londhe

#### Executive Summary
This project focuses on detecting anomalies in network data using multiple classification models and grid search to identify optimal hyperparameters. The models compared include Logistic Regression, Random Forest, and Support Vector Machine (SVM). The project also involves evaluating model performance through accuracy metrics and visualization.

#### Rationale
Why should anyone care about this question?  
Anomaly detection in network traffic is critical for identifying network intrusions, detecting system failures, and preventing service disruptions. Efficient anomaly detection helps networking companies maintain service quality, secure communications, and optimize infrastructure performance. This project aims to improve the understanding of different model performances in detecting anomalies in network data.

#### Research Question
What are you trying to answer?  
The goal is to determine which machine learning model and hyperparameter configuration is most effective for detecting anomalies in network data. This project also seeks to evaluate the performance of different models using cross-validation and accuracy scores.

#### Data Sources
What data will you use to answer your question?  
The dataset consists of scaled time-series network data, where non-anomalous data points are identified based on timestamps. Synthetic anomalies are added to the dataset to simulate real-world network issues, such as packet loss, latency spikes, or service disruptions. The data is split into training and test sets for model evaluation.

#### Methodology
What methods are you using to answer the question?  
- **Import Libraries**: Necessary libraries for model building, cross-validation, and grid search (e.g., `scikit-learn`, `tensorflow`) are imported.
- **Data Preparation**: Non-anomalous data points are initialized and collected. The dataset is split into training and test sets.
- **Model Definitions**: Multiple models (Logistic Regression, Random Forest, and SVM) are defined for classification tasks.
- **Hyperparameter Tuning**: Hyperparameters are defined for each model, and grid search is performed to optimize them.
- **Grid Search and Cross-Validation**: Grid search is used with cross-validation to evaluate the best model hyperparameters.
- **Evaluation**: Models are evaluated on the test set using accuracy, classification reports, and ROC curves. For autoencoders, training and validation loss is plotted over epochs.

#### Results
What did your research find?  
The project evaluates the performance of several machine learning models in detecting anomalies in network data. After performing grid search and cross-validation, the best hyperparameters for each model are identified, and the models' performance is assessed on the test set. Key findings include the differences in accuracy and classification metrics among the models.

#### Next Steps
What suggestions do you have for next steps?  
- **Improved Anomaly Simulation**: Refining the method for adding synthetic anomalies to better represent real-world network disruptions such as DDoS attacks, hardware failures, or bandwidth congestion could improve the robustness of the models.
- **Exploring Additional Models**: Future work can involve exploring other models like neural networks or ensemble methods for better anomaly detection in network environments.
- **Real-World Application**: Applying these models to real-world network traffic data and evaluating their performance on unseen data could enhance the understanding of anomaly detection in production network systems.


##### Contact and Further Information
For more information about this project or collaboration opportunities, please feel free to contact me at [your email address].
