# Student Performance Indicator

## Introduction and Overview

### Problem Statement
The project aims to accurately predict student performance in mathematics based on a range of socio-demographic and academic features. The challenge lies in effectively understanding and interpreting the complex interplay of factors that influence academic achievement and applying this understanding to make informed predictions.

### Project Components

1. **Model Training (Jupyter Notebook)**:
   - Initial data exploration and analysis.
   - Testing various machine learning models like Linear Regression, Random Forest Regressor, CatBoost Regressor, AdaBoost Regressor, Lasso Regressor, XG Boost Regressor, K-Nearest Neighbour Regressor and Decision Trees, with Linear Regression as the optimal choice.
   - Evaluation of model performance using metrics like RMSE, MAE, and R2 Score.

2. **Modular Programming**:
   - Data ingestion, transformation, and model training separated into modular scripts.
   - Utilizes dataclasses for configuration management.

3. **Data Transformation**:
   - Preprocesses data by handling missing values and standardizing numerical features.
   - Utilizes pipelines for efficient data transformation.
   - Implements one-hot encoding for categorical features.

4. **Model Trainer**:
   - Trains a Linear Regression model on preprocessed data.
   - Evaluates model performance and saves the trained model.

5. **Predict Pipeline**:
   - Loads the trained model and preprocessing object.
   - Accepts user input through a web interface and predicts math scores.
   - Provides rounded predictions to two decimal places.

6. **Exception Handling and Logging**:
   - Custom exception handling for better error reporting.
   - Logging of events and errors for debugging.

7. **Web Interface (Flask)**:
   - User-friendly web interface for inputting student data.
   - Displays predicted math scores based on user input.
   - Utilizes Bootstrap for a visually appealing design.

## Usage

1. Clone the repository.
2. Install the project's dependencies using `pip install -r requirements.txt`.
3. Run the Flask application using `python app.py`.

## Web Interface

Access the web interface by visiting `http://localhost:5000/` in your browser. Input student data, and the predicted math score will be displayed.

## Learning Outcomes

1. Developed a prediction model using Linear Regression.
2. Analyzed the impact of socio-demographic and academic factors on math performance.
3. Enhanced educational quality by providing data-driven insights for tailored interventions.

## Future Work and Business Implications

1. Future Work:
   - Expand the model's application to examine diversity data in job applications.
   - Adapt the model for categorizing areas needing CSR initiatives.
   - Incorporate additional features for more accurate CSR predictions.

2. Business Implications:
   - Empower proactive CSR initiatives with data-driven insights.
   - Enhance corporate reputation through strategic CSR initiatives.
   - Optimize resource allocation for impactful interventions.

3. Technical Extensions:
   - Apply modular programming to CSR initiative projects.
   - Conduct independent testing of each module.
   - Experiment with various classification algorithms for CSR predictions.

## Author

- Satyam Sharma
- Email: satyam3196@gmail.com

This project was developed as part of an educational initiative to predict student performance and provide insights for educational improvement.
