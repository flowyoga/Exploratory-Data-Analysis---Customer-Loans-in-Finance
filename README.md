# Exploratory-Data-Analysis -- Customer-Loans-in-Finance
<!-- 
## Table of Contents  -->

## A description of the project

This project is part of AICore's Data Analytics course. It involves sourcing data from an AWS RDS database, cleaning and transforming the data, visualizing it, and performing analysis.

## Installation instructions

git clone https://github.com/flowyoga/Exploratory-Data-Analysis---Customer-Loans-in-Finance

## File structure of the project

* db_utils.py - This file contains utilities for connecting to and downloading data from an RDS database. It also includes functions for loading data from a local file and saving a dataframe to a local file.
* df_data_transform.py - This file contains functions for log transformation, boxcox_transformation, yeojohnson transformation and outlier handling. 
* df_info.py - This file contains loading basic inforamtion such as info, describe, shape, null value checks on a dataframe.
* df_transform.py - This file contains functions for data type conversion, drop columns or rows, remove strings in a column and imputing median/mean. 
* df_visualisation.py - This file contains functions for plotting histograms, boxplots, and heatmaps. 
* Milestone3EDA.ipynb - This notebook contains Exploratory Data Analysis (EDA) tasks.
* Milestone4.ipynb  - This notebook contains tasks for Milestone 4. 
