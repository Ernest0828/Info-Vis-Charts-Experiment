import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the datasets
scatterplot_biased_file_path = './Dataset/Scatterplot-Biased_Dataset_for_10_Schools.csv'
heatmap_biased_file_path = './Dataset/Heatmap-Biased_Dataset_for_10_Schools.csv'

scatterplot_data = pd.read_csv(scatterplot_biased_file_path)
heatmap_data = pd.read_csv(heatmap_biased_file_path)

# Ensure the Month column is ordered for both datasets
month_order = [
    "January", "February", "March", "April", "May", 
    "June", "July", "August", "September", "October", 
    "November", "December"
]
scatterplot_data['Month'] = pd.Categorical(scatterplot_data['Month'], categories=month_order, ordered=True)
heatmap_data['Month'] = pd.Categorical(heatmap_data['Month'], categories=month_order, ordered=True)

# Create output folder if it doesn't exist
os.makedirs("Charts_HeatMap_Biased", exist_ok=True)

def create_scatterplots(data, output_folder="Charts_HeatMap_Biased"):
    # Question 1: Total absences for School 1 and School 5
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Month"], data["School_1"], label="School 1", color="blue", s=100, edgecolors="black")
    plt.scatter(data["Month"], data["School_5"], label="School 5", color="orange", s=100, edgecolors="black")
    # plt.title("Scatterplot: Total Absence Rates for School 1 and School 5", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Absences", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(alpha=0.5)
    plt.savefig(os.path.join(output_folder, "01_scatterplot_q1_school1_vs_school5.png"))
    plt.close()

    # Question 2: Absences for School 3 and School 8
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Month"], data["School_3"], label="School 3", color="green", s=100, edgecolors="black")
    plt.scatter(data["Month"], data["School_8"], label="School 8", color="purple", s=100, edgecolors="black")
    # plt.title("Scatterplot: Absences for School 3 and School 8", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Absences", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(alpha=0.5)
    plt.savefig(os.path.join(output_folder, "02_scatterplot_q2_school3_vs_school8.png"))
    plt.close()

    # Question 3: Month with highest total absences
    total_per_month = data.iloc[:, 1:].sum(axis=1)
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Month"], total_per_month, label="Total Absences", color="cyan", s=100, edgecolors="black")
    # plt.title("Scatterplot: Total Absences Across All Schools by Month", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Total Absences", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(alpha=0.5)
    plt.savefig(os.path.join(output_folder, "03_scatterplot_q3_school1-10_sum.png"))
    plt.close()

    # Question 4: Monthly absences for School 7 and School 9
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Month"], data["School_7"], label="School 7", color="red", s=100, edgecolors="black")
    plt.scatter(data["Month"], data["School_9"], label="School 9", color="blue", s=100, edgecolors="black")
    # plt.title("Scatterplot: Monthly Absences for School 7 and School 9", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Absences", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(alpha=0.5)
    plt.savefig(os.path.join(output_folder, "04_scatterplot_q4_school7_vs_school9.png"))
    plt.close()

    # Question 5: Monthly absences for School 6
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Month"], data["School_6"], label="School 6", color="purple", s=100, edgecolors="black")
    # plt.title("Scatterplot: Monthly Absences for School 6", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Absences", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(alpha=0.5)
    plt.savefig(os.path.join(output_folder, "05_scatterplot_q5_school6.png"))
    plt.close()

    # Question 6: Monthly absences for School 1 and School 2
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Month"], data["School_1"], label="School 1", color="blue", s=100, edgecolors="black")
    plt.scatter(data["Month"], data["School_2"], label="School 2", color="orange", s=100, edgecolors="black")
    # plt.title("Scatterplot: Monthly Absences for School 1 and School 2", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Absences", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(alpha=0.5)
    plt.savefig(os.path.join(output_folder, "06_scatterplot_q6_school1_vs_school2.png"))
    plt.close()

    # Question 7: Monthly absences for School 3
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Month"], data["School_3"], label="School 3", color="green", s=100, edgecolors="black")
    # plt.title("Scatterplot: Monthly Absences for School 3", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Absences", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(alpha=0.5)
    plt.savefig(os.path.join(output_folder, "07_scatterplot_q7_school3.png"))
    plt.close()

    # Question 8: Monthly absences for School 6 and School 8
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Month"], data["School_6"], label="School 6", color="green", s=100, edgecolors="black")
    plt.scatter(data["Month"], data["School_8"], label="School 8", color="blue", s=100, edgecolors="black")
    # plt.title("Scatterplot: Monthly Absences for School 6 and School 8", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Absences", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(alpha=0.5)
    plt.savefig(os.path.join(output_folder, "08_scatterplot_q8_school6_vs_school8.png"))
    plt.close()

    # Question 9: Monthly absences for School 5 and School 9
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Month"], data["School_5"], label="School 5", color="red", s=100, edgecolors="black")
    plt.scatter(data["Month"], data["School_9"], label="School 9", color="purple", s=100, edgecolors="black")
    # plt.title("Scatterplot: Monthly Absences for School 5 and School 9", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Absences", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(alpha=0.5)
    plt.savefig(os.path.join(output_folder, "09_scatterplot_q9_school5_vs_school9.png"))
    plt.close()

    # Question 10: Monthly absences for School 4 and School 10
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Month"], data["School_4"], label="School 4", color="orange", s=100, edgecolors="black")
    plt.scatter(data["Month"], data["School_10"], label="School 10", color="green", s=100, edgecolors="black")
    # plt.title("Scatterplot: Monthly Absences for School 4 and School 10", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Absences", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(alpha=0.5)
    plt.savefig(os.path.join(output_folder, "10_scatterplot_q10_school4_vs_school10.png"))
    plt.close()


def create_heatmaps(data, output_folder="Charts_HeatMap_Biased"):
    # Question 1: Total absences for School 1 and School 5
    monthly_absences = data[["Month", "School_1", "School_5"]].set_index("Month")
    sns.heatmap(
        monthly_absences.T, annot=False, fmt="d", cmap="coolwarm", cbar=True, 
        linewidths=0.5, cbar_kws={'label': 'Absences'}
    )
    # plt.title("Heatmap: Monthly Absences for School 1 and School 5", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Schools", fontsize=12)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.savefig(os.path.join(output_folder, "11_heatmap_q1_school1_vs_school5.png"))
    plt.close()

    # Question 2: Absences for School 3 and School 8
    monthly_absences = data[["Month", "School_3", "School_8"]].set_index("Month")
    sns.heatmap(
        monthly_absences.T, annot=False, fmt="d", cmap="coolwarm", cbar=True, 
        linewidths=0.5, cbar_kws={'label': 'Absences'}
    )
    # plt.title("Heatmap: Monthly Absences for School 3 and School 8", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Schools", fontsize=12)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.savefig(os.path.join(output_folder, "12_heatmap_q2_school3_vs_school8.png"))
    plt.close()

    # Question 3: Total absences for all schools by month
    total_per_month = data.set_index("Month").iloc[:, 1:].sum(axis=1).to_frame().T
    sns.heatmap(
        total_per_month, annot=False, fmt="d", cmap="coolwarm", cbar=True, 
        linewidths=0.5, cbar_kws={'label': 'Total Absences'}
    )
    # plt.title("Heatmap: Total Absences Across All Schools by Month", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Total Absences All School")
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.savefig(os.path.join(output_folder, "13_heatmap_q3_all_schools.png"))
    plt.close()

    # Question 4: Lowest absences in a single month for School 7 and School 9
    monthly_absences = data[["Month", "School_7", "School_9"]].set_index("Month")
    sns.heatmap(
        monthly_absences.T, annot=False, fmt="d", cmap="coolwarm", cbar=True, 
        linewidths=0.5, cbar_kws={'label': 'Absences'}
    )
    # plt.title("Heatmap: Monthly Absences for School 7 and School 9", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Schools", fontsize=12)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.savefig(os.path.join(output_folder, "14_heatmap_q4_school7_vs_school9.png"))
    plt.close()

    # Question 5: Monthly absences for School 6
    school_6_data = data[["Month", "School_6"]].set_index("Month").T
    sns.heatmap(
        school_6_data, annot=False, fmt="d", cmap="coolwarm", cbar=True, 
        linewidths=0.5, cbar_kws={'label': 'Absences'}
    )
    # plt.title("Heatmap: Monthly Absences for School 6", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("School 6", fontsize=12)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.savefig(os.path.join(output_folder, "15_heatmap_q5_school6.png"))
    plt.close()

    # Question 6: Monthly absences for School 1 and School 2
    monthly_absences = data[["Month", "School_1", "School_2"]].set_index("Month")
    sns.heatmap(
        monthly_absences.T, annot=False, fmt="d", cmap="coolwarm", cbar=True, 
        linewidths=0.5, cbar_kws={'label': 'Absences'}
    )
    # plt.title("Heatmap: Monthly Absences for School 1 and School 2", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Schools", fontsize=12)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.savefig(os.path.join(output_folder, "16_heatmap_q6_school1_vs_school2.png"))
    plt.close()

    # Question 7: Monthly absences for School 3
    school_3_data = data[["Month", "School_3"]].set_index("Month").T
    sns.heatmap(
        school_3_data, annot=False, fmt="d", cmap="coolwarm", cbar=True, 
        linewidths=0.5, cbar_kws={'label': 'Absences'}
    )
    # plt.title("Heatmap: Monthly Absences for School 3", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("School 3", fontsize=12)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.savefig(os.path.join(output_folder, "17_heatmap_q7_school3.png"))
    plt.close()

    # Question 8: Monthly absences for School 6 and School 8
    monthly_absences = data[["Month", "School_6", "School_8"]].set_index("Month")
    sns.heatmap(
        monthly_absences.T, annot=False, fmt="d", cmap="coolwarm", cbar=True, 
        linewidths=0.5, cbar_kws={'label': 'Absences'}
    )
    # plt.title("Heatmap: Monthly Absences for School 6 and School 8", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Schools", fontsize=12)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.savefig(os.path.join(output_folder, "18_heatmap_q8_school6_vs_school8.png"))
    plt.close()

    # Question 9: Monthly absences for School 5 and School 9
    monthly_absences = data[["Month", "School_5", "School_9"]].set_index("Month")
    sns.heatmap(
        monthly_absences.T, annot=False, fmt="d", cmap="coolwarm", cbar=True, 
        linewidths=0.5, cbar_kws={'label': 'Absences'}
    )
    # plt.title("Heatmap: Monthly Absences for School 5 and School 9", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Schools", fontsize=12)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.savefig(os.path.join(output_folder, "19_heatmap_q9_school5_vs_school9.png"))
    plt.close()

    # Question 10: Monthly absences for School 4 and School 10
    monthly_absences = data[["Month", "School_4", "School_10"]].set_index("Month")
    sns.heatmap(
        monthly_absences.T, annot=False, fmt="d", cmap="coolwarm", cbar=True, 
        linewidths=0.5, cbar_kws={'label': 'Absences'}
    )
    # plt.title("Heatmap: Monthly Absences for School 4 and School 10", fontsize=14)
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Schools", fontsize=12)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.savefig(os.path.join(output_folder, "20_heatmap_q10_school4_vs_school10.png"))
    plt.close()


# Generate the graphs
print("Generating scatterplots...")
create_scatterplots(heatmap_data)

print("Generating heatmaps...")
create_heatmaps(heatmap_data)
