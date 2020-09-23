# UsedCarPricePrediction

**Dataset link**: https://www.kaggle.com/avikasliwal/used-cars-price-prediction <br/>
The data was taken from kaggle.
Various data cleaning and preprocessing steps were performed and visualizations were made. Further, the prediction models used were XGBoost, Random Forest, Decision Tree and Lasso Regression. Finally, the most suitable model with least found mean absolute error was selected and the model was deployed using Django with a minimally aesthetic user interface made using HTML, CSS and bootstrap.

XGBoost performed best among the others. The model was stored in a pickle file and used in Django API.

In DjangoAPI project, model was created with respect to the required fields in the dataset.

Serializers were used to make data interpretable to the machine by converting complex data such as querysets and model instances into native Python data types.

To accept details of car from user, forms were created.

Now, views were created with functions that would work in the background to fetch the posted details, preprocess it and use the ML model to predict and display the prices.

**User Interface:**<br/>
<img src="https://github.com/awamay/car_price_predictor/blob/master/photo_2020-09-24_01-57-32.jpg" width="700" title="screenshot og UI"> <br/>
**Sample output**:<br/>
<img src="https://github.com/awamay/car_price_predictor/blob/master/photo_2020-09-24_01-57-50.jpg" width="700" title="screenshot og UI">
