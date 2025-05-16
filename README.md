# Info-Vis-Charts-Experiment

This project involves the design of a laboratory experiment to compare Heatmaps vs Scatterplots for showing how pupil absences vary across a school year. 

## Experiment Design
- This experiemnt was made with Python and the Tkinter library to allow for an interactive design. It will display charts with a question for users to answer relating to the visualisation provided.
- It will start with displaying 10 questions visualised with a **Scatterplot** first, followed with 10 questions visualised with **Heatmaps**. The 10 questions are the same, just visualised differently.
- After one question is answered, the screen will be blanked for 1 second before showing the next chart.
- Two variables are recorded here: **Response Time** (time taken for the user to answer each question) and **Error Rate** (whether the users' answer was True or False).
- To determine the effectiveness fo the charts: **T-tests**, **Average Response Times** and **Average Error Rates** were computed.
- Afetr assessing the results, it was shown that **Heatmaps** were more effective in visualising pupil absence data.

## Usage
- Run the _GenerateCharts.py_ file first to generate heatmap and scatterplot visualisations of school absences from the dataset.
- Run the _experiment.py_ file to start the experiment. It will start with 10 **Scatterplots** followed with 10 **Heatmaps**.

## Example Question
![image](https://github.com/user-attachments/assets/6055c69e-22ea-4a2b-843c-bce2e2d179cc)
