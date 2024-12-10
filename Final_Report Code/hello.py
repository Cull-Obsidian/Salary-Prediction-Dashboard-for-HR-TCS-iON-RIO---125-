# Importing necessary Library
import pandas as pd
import streamlit as st
import pickle
import altair as alt



# heading
st.markdown("<h1 style = 'text-align:center;'>Salary Prediction Model</h1>", unsafe_allow_html=True)
st.write("---")

# form to input informatioon
with st.form("Form 2", clear_on_submit=False):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last Name")
    experience = col1.number_input("Enter The Experience",min_value=0, max_value=50)
    age = col2.number_input("Enter Your Age", min_value = 18, max_value = 100)
    department = col1.radio("Choose the Department", options=("Admin", "Finance", "HR", "IT", "Marketing"))
    st.write("---")
    btn = st.form_submit_button("Submit")

    if btn:
        if f_name and l_name and department and experience and age:
            st.success("Submitted Succesfully!")
        else:
            st.warning("Please Fill all fields")


    # 'IT':3, 'Finance':1, 'HR':2, 'Admin':0, 'Marketing:4'

# integrating model with streamlit
# loading pickle model
with open('salary_model.pkl', 'rb') as file:
    clf = pickle.load(file)


def info_display(fname, lname, deptartment, experience, age):

    # Converting Data Types
    exp = int(experience)
    age = int(age)
    dept = {
        "Admin":0,
        "Finance":1,
        "HR":2,
        "IT":3,
        "Marketing":4
    }

    # making predictions
    prediction = clf.predict([[dept[deptartment], age, exp]])

    # converting the array to float and limiting the values after decimals
    prediction = float(prediction[0])
    formatted_number = f"{prediction:.2f}"

    # Displaying Prediction
    st.write(f"<h3 style = 'text-align:center;'>According to the Given Data, <span style = 'color:orange;'>{fname +' '+ lname}</span> will have a salary of:</h3>", unsafe_allow_html=True)
    st.markdown(f"<h2 style = 'text-align:center; color:Green;'>{'₹'+formatted_number}</h2>", unsafe_allow_html=True)


if btn:
    if f_name and l_name and department and experience > 0 and age >= 18:
        info_display(f_name, l_name, department, experience, age)
    else:
        pass


# separator
st.write("---")

# Making Graphs
gcol1, gcol2 = st.columns(2)

dataset = pd.read_csv(r'datasets/cleaned_data.csv')


# Line chart Experience vs Salary
with gcol1:
#     chart = alt.Chart(dataset).mark_line(point=True).encode(
#         x="experience:Q",  # Quantitative (numeric) data
#         y="salary:Q",
#         color="department:N",  # Categorical data for hue
#         tooltip=["experience", "salary", "department"]  # Tooltip for interaction
#     ).properties(
#         title="Salary vs Experience by Department"
#     )
#     # displaying chart
#     st.altair_chart(chart, use_container_width=True)

     st.image(r"media\exp_vs_salary.png")



# 2. Line Chart Age vs Salary
with gcol2:
    department_count = dataset["department"].value_counts().reset_index()
    department_count.columns = ["department", "count"]

    bar_chart = alt.Chart(department_count).mark_bar().encode(
        x=alt.X("department:N", title="Department"),  # Categorical data for x-axis
        y=alt.Y("count:Q", title="Number of Employees"),  # Quantitative data for y-axis
        color="department:N",  # Different color for each department
        tooltip=["department", "count"]  # Tooltip for interactivity
    ).properties(
        title="Number of Employees in Each Department",
        width=600,
        height=400
    )

    # Display the bar chart in Streamlit
    st.altair_chart(bar_chart, use_container_width=True)


# Adding a footer
footer = """
<style>
footer {
    visibility: hidden;
}
.custom-footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #0E1117;
    border-top: solid 1px white;
    color: white;
    text-align: center;
    padding: 10px 0;
    font-size: 14px;
}
.custom-footer a {
    color: #ff914d;
    text-decoration: none;
}
.custom-footer a:hover {
    text-decoration: underline;
}
</style>
<div class="custom-footer">
    Developed by Lakhan Kumar | <a href="https://github.com/Cull-Obsidian"> Github Profile </a> | © 2024 All Rights Reserved
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
