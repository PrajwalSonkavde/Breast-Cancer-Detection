# Breast-Cancer-Detection
Here a user interface is created through which people can give the details and in the back-end model will check and say whether there is possibility of getting breast cancer


![Screenshot 2023-03-22 170029](https://user-images.githubusercontent.com/99462259/226891330-8795b67d-d54b-45ac-952f-af9b611d0923.png)
![Screenshot 2023-03-22 170120](https://user-images.githubusercontent.com/99462259/226891486-37dab7bf-ef80-4413-92c3-828a206a7c65.png)
![Screenshot 2023-03-22 165847](https://user-images.githubusercontent.com/99462259/226891030-bd7643db-0cc6-430a-80ba-5d0172bd1a1b.png)


code is Written in such a way which represents a Flask web application for breast cancer detection. It uses a trained Random Forest model to predict whether a person has breast cancer based on various input features. Here is a description that you can use for the GitHub repository:
Breast Cancer Detection Web Application<br>

This is a Flask-based web application that allows users to determine the likelihood of having breast cancer using machine learning. The application uses a trained Random Forest model to predict the presence of breast cancer based on user input.<br>
Functionality:<br><br>

    -> User-friendly interface for inputting relevant information
    -> Trained Random Forest model for accurate predictions
    -> Interactive visualization of cancer death rates in different US states

How it works:<br><br>

    -> Users input their personal information, including name, age, race, marital status, tumor stage, grade, and other relevant factors.
    -> The application processes the input data and passes it through the trained Random Forest model.
    -> The model predicts whether the user is likely to have breast cancer or not.
    -> The result is displayed on the screen, indicating the probability of having breast cancer.
    -> Additionally, the application provides a graph that shows the death rates due to cancer in different US states.

Dataset:<br><br>

The breast cancer dataset used for training the model was obtained from the 2017 November update of the SEER Program of the NCI (National Cancer Institute). It includes information about female patients with infiltrating duct and lobular carcinoma breast cancer diagnosed between 2006 and 2010. The dataset contains 4024 patients, excluding those with unknown tumor size, examined regional lymph nodes, positive regional lymph nodes, and those with less than 1 month of survival.

How to Use:<br><br>

    -> Clone the repository to your local machine.
    -> Make sure you have Python and Flask installed.
    -> Run the main file app.py to start the Flask server.
    -> Access the application through your web browser at http://localhost:5000.
    -> Fill in the required information and click the "Submit" button.
    -> The application will display the prediction result on the screen.
