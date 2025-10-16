# [Customer Feedback Sentiment Analyzer (Streamlit & VADER)](https://github.com/Satyajit546/Customer_sentiment_analyzer_Web_app-python-streamlit-/blob/main/web%20page%20image/sentiment%20Home%20.jpg)

## 1.📝 Project Overview ##

This project implements a live, web-based platform for performing Customer Feedback Sentiment Analysis. Built entirely in Python using the Streamlit framework, the application allows users (like product managers or business analysts) to directly input a Google Sheet URL containing customer reviews and instantly receive a detailed sentiment breakdown.

The core goal was to transform raw, unstructured customer feedback into actionable data points (Positive, Negative, Neutral) to help businesses quickly gauge product satisfaction and prioritize areas for improvement.The platform provides a user-friendly interface for uploading data, performing the sentiment analysis using the VADER lexicon, and visualizing the results.

## 2.✨ Key Features ##

* Live Data Ingestion:  Users can input the URL of a publicly shared Google Sheet (or any CSV file) containing product reviews.

* VADER Sentiment Engine: Utilizes the VADER (Valence Aware Dictionary and sEntiment Reasoner) library, specifically tuned for analyzing sentiments expressed in social media and product reviews.

* Real-Time Analysis: The application processes the data, calculates the compound sentiment score for each review, and classifies it as Positive, Negative, or Neutral.

* Interactive Visualization: Offers clear and interactive data visualizations (Pie Charts and Histograms via Plotly) to summarize the overall sentiment distribution.

* Downloadable Results: The fully analyzed DataFrame, including the new 'Sentiment' column, is saved locally and can be reviewed.

* Intuitive Web Interface: A multi-page Streamlit interface for seamless navigation between Home, Analysis, and Visualization screens.


 ## 3.🛠️ Technology Stack


* Python: The core programming language.

* Streamlit: Used to create the interactive web application interface.

* Pandas: Essential for data manipulation, particularly reading the input data (assumed to be from a Google Sheet URL in CSV format) and processing it.

* VADER (Valence Aware Dictionary and Sentiment Reasoner): The specific lexicon and rule-based sentiment analysis model used to score the reviews.

* Plotly Express: Used for generating interactive data visualizations (Pie Chart and Histogram).

# 4.🚀 How It Works

* Data Input: The user navigates to the "Analysis" page and provides a CSV URL (often from a Google Form linked to a Google Sheet) and the name of the column containing the text reviews.

* Sentiment Scoring: [For every review text (k) in the specified column (cn), the VADER model (SentimentIntensityAnalyzer()) calculates a compound score](https://github.com/Satyajit546/Customer_sentiment_analyzer_Web_app-python-streamlit-/blob/main/web%20page%20image/Sentiment%20Analysis.jpg):

compound > 0.01 ➡️ Positive

compound < -0.01 ➡️ Negative

compound between -0.01 and 0.01 ➡️ Neutral

* Result Integration: A new column, "Sentiment," is added to the DataFrame with the classification.

* Output: The analyzed data is saved to results.csv and made available for visualization on the "Visualization" page, where the sentiment distribution is displayed using Pie Charts and Histograms.


### 5.Application Functionality and Flow
The application is structured into three main sections accessible via a sidebar menu: Home, Analysis, and Visualization.
## [Home](https://github.com/Satyajit546/Customer_sentiment_analyzer_Web_app-python-streamlit-/blob/main/web%20page%20image/sentiment%20Home%20.jpg)

Displays a welcome message and an introductory image.
Serves as the landing page for the application.
Analysis
This is where the sentiment analysis is performed.

* Input: The user must provide the Google Sheet URL (expected to be a public/shareable CSV link) and the column name in the sheet that contains the customer reviews (e.g., "Review," as seen in the image).

## [Process](https://github.com/Satyajit546/Customer_sentiment_analyzer_Web_app-python-streamlit-/blob/main/web%20page%20image/Sentiment%20Analysis.jpg):

The platform reads the data into a Pandas DataFrame.
It iterates through each review in the specified column.
The VADER model calculates the sentiment polarity scores (including the compound score) for each review.
Sentiment Classification Logic.

## [Visualization](https://github.com/Satyajit546/Customer_sentiment_analyzer_Web_app-python-streamlit-/blob/main/web%20page%20image/visualization.jpg)

This section loads the analyzed data from the results.csv file for display.
The user can choose from various visualization options:

* [Table](https://github.com/Satyajit546/Customer_sentiment_analyzer_Web_app-python-streamlit-/blob/main/web%20page%20image/Table.jpg): Displays the full analyzed data in a Streamlit DataFrame, including the original data and the new "Sentiment" column.

* [Pie Chart](https://github.com/Satyajit546/Customer_sentiment_analyzer_Web_app-python-streamlit-/blob/main/web%20page%20image/Vis1.jpg): Shows the percentage distribution of the three sentiment classes (Positive, Negative, Neutral).

* [Histogram](https://github.com/Satyajit546/Customer_sentiment_analyzer_Web_app-python-streamlit-/blob/main/web%20page%20image/Histogram.jpg): Allows the user to select any column from the data (e.g., 'Gender', 'Platform', 'Category') and displays its distribution, with the bars colored based on the "Sentiment" (e.g., showing the sentiment breakdown for each 'Platform').


### 6.Application Use Case and Context

* Source Data: The project is designed to handle product review data, such as that collected from a Google Form response sheet (as suggested by the fg.jpg image). The data includes fields like Timestamp, Name, Gender, Platform (e.g., Flipkart, Amazon, Meesho), Category, and the crucial Review text.

* Objective: To automatically gauge customer satisfaction and feedback at scale by converting raw textual reviews into quantifiable sentiment metrics.

* Beneficiaries: E-commerce analysts, product managers, or market researchers interested in quickly understanding customer perception across different platforms or product categories.
