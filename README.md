# Car Prediction Project

## Authors
- Haddany Abdelkhalek

## Dataset
https://drive.google.com/file/d/1_XO6QDHNR86ov69bnIfx5TXM2kIBYyuK/view?usp=sharing

## Overview
This project involves the creation of a car prediction model for a car dealership, aiming to assist salespersons in targeting vehicles that may interest their clients.

## Project Context
The client has provided the following data:
- Catalog of vehicles: "Catalogue.csv"
- Customer file for purchases in the current year: "Clients.csv"
- Information on registrations made this year: "Immatriculations.csv"
- Brief documentation of the data
- Interview with a salesperson

The objective is to propose a solution where:
1. Salespersons can quickly assess the type of vehicle likely to interest clients.
2. Precise documentation on suitable vehicles can be sent to clients selected by the marketing department.

## Project Execution

### 1. Data Preprocessing
- **Catalog Dataset:** Preprocessed for model training using the KMeans algorithm.
- **Cluster Identification:** Used the Elbow method to identify four distinct clusters: 'Family Cars', 'Sport Utility Cars', 'City Cars', 'Luxury Cars'.
- **Client's Dataset and Matriculation:** Merged into a single data frame for the training of the second model.

### 2. Predictive Models
Trained using the following algorithms:
1. Multinomial Logistic Regression
2. Random Forest Classifier
3. XGBoost

### 3. Model Selection
Chose the XGBoost Classifier based on performance.

### 4. StreamLit Interface
- **Client Information Page:** Collects client information.
- **Car Information and Results Page:** Displays results, including the best cluster for the client and proposed cars based on color and occasion status.

### 5. Model Export
Exported the selected model for integration into the StreamLit interface.

## Conclusion
This real-world project aimed to assist a car dealership in targeting vehicles more effectively. The project highlights the importance of a substantial and balanced dataset for achieving optimal accuracy in predictive modeling. The chosen XGBoost Classifier proved to be the most effective for this particular scenario.
