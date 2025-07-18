# Intelligent Diagnosis System for Autoimmune Diseases

This project presents an AI-based system for the early detection and diagnosis of autoimmune diseases using machine learning algorithms. The aim is to assist medical professionals in improving diagnostic accuracy and response time by analyzing various clinical and biological markers.

The primary objective of this project is to automate the detection of autoimmune diseases using supervised machine learning techniques. By leveraging clinical and biological data, the system aims to enhance diagnostic decision-making through data-driven insights. In addition, it provides a user-friendly interface that allows healthcare professionals to easily upload patient data and obtain accurate diagnostic predictions, thereby streamlining and supporting the medical evaluation process.

## Dataset
The dataset was collected from Kaggle under the name Complete_Updated_Autoimmune_Disorder_Dataset2.csv, containing anonymized patient records with clinical, demographic, and biomarker features.

## Model Performance
We evaluated several supervised machine learning models, including Random Forest, SVC, XGBoost, LGBM, MLP, and CatBoost, across five different feature selection strategies: All Features, Lasso-CV, RFE-CV, Tree Importance, and Common Features. The results demonstrate consistently high performance across models, with accuracy values exceeding 98% in nearly every configuration.

| Feature Set         | Model         | Accuracy | F1 (Weighted) | ROC-AUC (OvR) |
| ------------------- | ------------- | -------- | ------------- | ------------- |
| **All Features**    | Random Forest | 0.9881   | 0.9880        | 0.9991        |
|                     | SVC           | 0.9855   | 0.9854        | 0.9970        |
|                     | XGBoost       | 0.9866   | 0.9865        | 0.9995        |
|                     | LGBM          | 0.9830   | 0.9829        | 0.9984        |
|                     | MLP           | 0.9837   | 0.9836        | 0.9970        |
|                     | CatBoost      | 0.9852   | 0.9851        | 0.9995        |
| **Lasso-CV**        | Random Forest | 0.9906   | 0.9905        | 0.9991        |
|                     | SVC           | 0.9855   | 0.9854        | 0.9966        |
|                     | XGBoost       | 0.9870   | 0.9869        | 0.9996        |
|                     | LGBM          | 0.9852   | 0.9851        | 0.9994        |
|                     | MLP           | 0.9862   | 0.9861        | 0.9986        |
|                     | CatBoost      | 0.9866   | 0.9865        | 0.9993        |
| **RFE-CV**          | Random Forest | 0.9902   | 0.9902        | 0.9993        |
|                     | SVC           | 0.9873   | 0.9872        | 0.9984        |
|                     | XGBoost       | 0.9888   | 0.9887        | 0.9996        |
|                     | LGBM          | 0.9870   | 0.9869        | 0.9993        |
|                     | MLP           | 0.9855   | 0.9854        | 0.9981        |
|                     | CatBoost      | 0.9866   | 0.9865        | 0.9989        |
| **Tree Importance** | Random Forest | 0.9912   | 0.9880        | 0.9993        |
|                     | SVC           | 0.9866   | 0.9865        | 0.9986        |
|                     | XGBoost       | 0.9884   | 0.9883        | 0.9996        |
|                     | LGBM          | 0.9881   | 0.9880        | 0.9995        |
|                     | MLP           | 0.9848   | 0.9847        | 0.9961        |
|                     | CatBoost      | 0.9859   | 0.9858        | 0.9988        |
| **Common Features** | Random Forest | 0.9899   | 0.9898        | 0.9995        |
|                     | SVC           | 0.9873   | 0.9872        | 0.9984        |
|                     | XGBoost       | 0.9873   | 0.9871        | 0.9996        |
|                     | LGBM          | 0.9888   | 0.9887        | 0.9995        |
|                     | MLP           | 0.9866   | 0.9865        | 0.9977        |
|                     | CatBoost      | 0.9841   | 0.9840        | 0.9989        |


Among these models, Random Forest, SVC and XGBoost delivered the most reliable and robust results, with accuracies reaching up to 99.12% and ROC-AUC scores as high as 0.9996. Feature selection techniques such as Lasso-CV and Tree Importance not only enhanced performance but also helped simplify the models. These findings indicate the potential of our AI-based system to offer a high-performing, interpretable, and efficient solution for supporting the diagnosis of autoimmune diseases.

## Team Members
Wahiba Bousyf 
Hajar Alouani

## Supervised by
Pr. Faouzia Benabbou and Dr. Zineb Ellaky   
Faculty of Sciences Ben M’Sik, Hassan II University, Casablanca

## License
This project is for academic use only. Contact us for any reproduction or reuse permissions.

## Contact
Feel free to reach out via [email](mailto:hajar_alouani@outlook.fr) or on [LinkedIn: Hajar Alouani](www.linkedin.com/in/hajaralouani) / [Wahiba Bousyf](https://www.linkedin.com/in/wahiba-bousyf).

