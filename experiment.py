import csv
import tkinter as tk
from PIL import Image, ImageTk
import os
import time
import ast

def load_questions_from_csv(file_path):
    """Load questions from a CSV file and convert the choices column to a Python list."""
    questions = []
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert the string representation of a list into an actual list
            choices = ast.literal_eval(row["choices"])
            questions.append({
                "question": row["question"],
                "choices": choices,
                "correct_answer": row["correct_answer"]
            })
    return questions


# Load all chart paths
chart_folder = "Charts_HeatMap_Biased"
#chart_folder = "Charts_ScatterPlot_Biased"
chart_files = [
    os.path.join(chart_folder, f) for f in sorted(os.listdir(chart_folder))
    if f.endswith((".png", ".jpg", ".jpeg"))
]

# Load questions from the CSV file
questions_file = "Question_Answer_HeatMap_Biased.csv"
#questions_file = "Question_Answer_ScatterPlot_Biased.csv"
questions = load_questions_from_csv(questions_file)

# Ensure the questions list matches the number of charts
questions = questions * (len(chart_files) // len(questions)) + questions[:len(chart_files) % len(questions)]

# Initialize variables
current_chart_index = 0
chart_label = None
response_times = []
selected_answers = []
results = []  # List to store whether each answer was correct (True/False)
start_time = None
radio_buttons = []

# Function definitions remain unchanged
def start_experiment():
    global current_chart_index
    welcome_label.pack_forget()
    start_button.pack_forget()
    setup_experiment_layout()
    show_blank_screen_then_load_chart()


def setup_experiment_layout():
    global chart_label, question_label, radio_var, next_button
    chart_label = tk.Label(root, text="", font=("Arial", 16))
    chart_label.pack(pady=20)
    question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=600, anchor="center", justify="center")
    question_label.pack(pady=10)
    radio_var = tk.StringVar()
    next_button = tk.Button(root, text="Next Chart", command=show_blank_screen_then_load_chart, font=("Arial", 12), padx=15, pady=8)
    next_button.pack(pady=15)


def show_blank_screen_then_load_chart():
    global start_time, current_chart_index
    if start_time:
        response_time = time.time() - start_time
        response_times.append(response_time)
        selected_answer = radio_var.get()
        selected_answers.append(selected_answer)
        correct_answer = questions[current_chart_index - 1]["correct_answer"]
        results.append(selected_answer == correct_answer)
    chart_label.config(text="", image="")
    question_label.config(text="")
    for rb in radio_buttons:
        rb.destroy()
    radio_buttons.clear()
    root.after(1000, load_chart, current_chart_index)


def load_chart(index):
    global chart_label, current_chart_index, start_time, question_label, radio_buttons, radio_var
    if index < len(chart_files):
        image = Image.open(chart_files[index])
        image = image.resize((600, 400))
        chart_image = ImageTk.PhotoImage(image)
        chart_label.config(image=chart_image)
        chart_label.image = chart_image
        question_data = questions[index]
        question_label.config(text=question_data["question"])
        radio_var.set(None)
        for choice in question_data["choices"]:
            rb = tk.Radiobutton(root, text=choice, variable=radio_var, value=choice, font=("Arial", 12), anchor="center")
            rb.pack(pady=3)
            radio_buttons.append(rb)
        start_time = time.time()
        current_chart_index += 1
    else:
        thank_you_page()


def thank_you_page():
    chart_label.pack_forget()
    question_label.pack_forget()
    next_button.pack_forget()
    for rb in radio_buttons:
        rb.destroy()
    thank_you_label = tk.Label(root, text="Thank you for your participation!", font=("Arial", 18))
    thank_you_label.pack(pady=40)
    save_results_to_csv()


def save_results_to_csv():
    filename = "experiment_results.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Chart Number", "Response Time", "Correct"])
        for chart_num, (time, correct) in enumerate(zip(response_times, results), start=1):
            writer.writerow([chart_num, time, correct])
    print(f"Results saved to {filename}")


# Create the main window
root = tk.Tk()
root.title("Experiment Setup")
root.geometry("800x700")

welcome_label = tk.Label(root, text="Press start to start the experiment", font=("Arial", 16))
welcome_label.pack(pady=30)
start_button = tk.Button(root, text="Start", command=start_experiment, font=("Arial", 12), padx=15, pady=8)
start_button.pack(pady=15)

# Run the Tkinter event loop
root.mainloop()
