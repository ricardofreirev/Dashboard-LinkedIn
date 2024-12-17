# Introduction

**Author:** Ricardo Freire
**Date:** 17.12.2024

This project is part of the homework for Lecture 6 of the course "Python Programming for Business and Life Sciences Analytics". The goal of this project is to practice data visualization techniques used in analytics. More specifically, we aim to explore how Python tools such as Plotly, Matplotlib, and Dash can be used to create complex data dashboards.

# Description
In the lecture materials, a dashboard with LinkedIn data was presented. The project was built on top of an example numbered as **d**, and the tasks of the lecture were to modify and enhance the dashboard. The following modifications were made:

1. A additional **stacked area** chart was added at the bottom of the page. The chart shows the amount of messsages send each month (across the different years) and on wich day of the week the messages were sent. To add an element about the time distribution of the messages sent was interesting for the project as none of the other visualizations covered this aspect.

2. An interactive **sidebar** with links to all of the visualizations included in the page was added at the right corner of the page.

3. On the original version, the date-pickers of the dashboard were visually uncomfortable beacuse they were located in the top-middle of the page. To enhance the styling of the page, a **title banner** with the LinkedIn colors was added instead and the date pickers were placed below.

# Deployment

To deploy the application, Render was chosen. The reason for this choice is that Render stands out as a popular, free option for deploying Dash applications, and it offers simple integration with GitHub repositories.

# Getting started 

To view the dashboard online, simply visit the following **Render link**: 
https://python-programming-for-business.onrender.com/

The dashboard will be live, and you can interact with all the visualizations directly in your web browser without any additional setup.