# Laptop-Price-Prediction
A collection of machine learning models for predicting laptop prices

![Laptop-Price-Prediction](assets/demo.png)

<details>
<summary style="font-size: 20px;">Dependencies</summary>
To install the required Python packages you can use the following command:

```bash
pip install -r requirements.txt
```
</details>

<details>
<summary style="font-size: 20px;">Datasets Reference</summary>
The dataset is about laptops configuration with prices containing 1302 laptops data with 12 columns Company name,type namee, laptop size in (inches), Screen resolution, CPU, RAM, Memory, GP, Operating system, Price in INR. The dataset was collected from Amazon in 2017-18.
</details>

<details>
<summary style="font-size: 20px;">Regressor Model Choices</summary>

- Multiple Linear Regression
- Ridge Regression
- Lasso Regression
- k-Nearest Neighbors (k-NN)
- Decision Tree
- Support Vector Machine (SVM)
- Random Forest
- ExtraTrees
- Adaptive Boost (AdaBoost)
- Gradient
- Extreme Gradient Boost (XGBoost)
- Voting
- Stacking
- Random Forest Regressor Model - Personal Customization
- Voting Regressor Model (Rf+Gradient) - Personal Customization
</details>

<details>
<summary style="font-size: 20px;">Selected Regression Model</summary>

- Random Forest Regressor Model - Personal Customization

```
R2 Score: 88.78 %
Mean Absolute Error: 15.94 %
```
- Voting Regressor Model (Rf+Gradient) - Personal Customization

```
R2 Score: 0.89 ( 89.27 %)
Mean Absolute Error: 0.15 ( 15.37 %)
```
</details>

<details>
<summary style="font-size: 20px;">Price Currency Conversion [Optional]</summary>
This line of code indicates currency conversion of laptop prices from INR to USD (1 Indian Rupee = 0.012 US Dollar). You can customize the currency exchange rate that suits your need.
<br><br>
  
```
st.title(f"\nPrice: {round(predicted_price * 0.012, 2)} USD")
```
</details>

<details>
<summary style="font-size: 20px;">Run <i>app.py</i></summary>
To run the app.py, load the dependecies requirements and use the following command:
<br><br>
  
```
streamlit run app.py
```
✨ Enjoy the demo
</details>

<hr>
<footer>
  Feel free to send issues if you face any problem. </br>
  ✨ Don't forget to star the repo :)
</footer>
