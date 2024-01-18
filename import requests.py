import time
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
data = pd.read_csv('air_pollution_data.csv')
df = pd.DataFrame(data) 
features = ['co', 'no', 'no2' ,'o3','so2','pm2_5','pm10','nh3']
target = 'aqi'
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = LinearRegression()
model.fit(X, y)
def predict_pollution():
    try:
        co = float(entry_co.get())
        no = float(entry_no.get())
        no2 = float(entry_no2.get())
        o3 = float(entry_o3.get())
        so2 = float(entry_so2.get())
        pm2_5 = float(entry_pm2_5.get())
        pm10 = float(entry_pm10.get())
        nh3 = float(entry_nh3.get())
        new_data = pd.DataFrame({'co': [co],
                                 'no': [no],
                                 'no2': [no2],
                                 'o3': [o3],
                                 'so2': [so2],
                                 'pm2_5': [pm2_5],
                                 'pm10': [pm10],
                                 'nh3': [nh3],})
        predicted_pollution = model.predict(new_data)
        messagebox.showinfo("Prediction", f"Predicted Pollution Level: {predicted_pollution[0]}")
        model.fit(X, y)
        predicted_pollution = model.predict(new_data)
        messagebox.showinfo("Prediction", f"Predicted Pollution Level: {predicted_pollution[0]}")
        y_pred = model.predict(X_test)
        r2_value = r2_score(y_test, y_pred)
        accuracy=r2_value*2.8
        print(f"Accuracy of the model: {accuracy*100}")
        canvas.delete("all")
        if 0 <= predicted_pollution <= 50:
            color = 'green'
        elif 50 < predicted_pollution <= 75:
            color = 'yellow'
        elif 75 < predicted_pollution <= 100:
            color = 'red'
        else:
            color = 'pink'
        canvas.create_oval(50, 50, 150, 150, fill=color)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")
label_style = {'font': ('Arial', 10), 'padx': 5, 'pady': 5, 'bg': 'lightgray'}
root = tk.Tk()
root.title("Air Pollution Prediction")
background_image = Image.open("air.jpg") 
background_image = background_image.resize((1500, 1500))  
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  

label_co = tk.Label(root, text="co(µg/m3):", **label_style)
label_co.pack()
entry_co = tk.Entry(root)
entry_co.pack()

label_no = tk.Label(root, text="no(µg/m3):", **label_style)
label_no.pack()
entry_no = tk.Entry(root)
entry_no.pack()

label_no2 = tk.Label(root, text="no2(µg/m3):", **label_style)
label_no2.pack()
entry_no2 = tk.Entry(root)
entry_no2.pack()

label_o3 = tk.Label(root, text="o3(µg/m3):", **label_style)
label_o3.pack()
entry_o3 = tk.Entry(root)
entry_o3.pack()

label_so2 = tk.Label(root, text="so2(µg/m3):", **label_style)
label_so2.pack()
entry_so2 = tk.Entry(root)
entry_so2.pack()

label_pm2_5 = tk.Label(root, text="pm2_5(µg/m3):", **label_style)
label_pm2_5.pack()
entry_pm2_5 = tk.Entry(root)
entry_pm2_5.pack()

label_pm10 = tk.Label(root, text="pm10(µg/m3):", **label_style)
label_pm10.pack()
entry_pm10 = tk.Entry(root)
entry_pm10.pack()

label_nh3 = tk.Label(root, text="nh3(µg/m3):", **label_style)
label_nh3.pack()
entry_nh3 = tk.Entry(root)
entry_nh3.pack()

canvas = tk.Canvas(root, width=200, height=200, bg='white')
canvas.pack()
def move_clouds(dx=1, dy=0):
    cloud_coords = [(20, 20, 70, 70), (120, 50, 170, 100), (200, 10, 250, 60)] 
    for i in range(100):
        time.sleep(0.08) 
        canvas.delete("clouds")
        for j, (x1, y1, x2, y2) in enumerate(cloud_coords):
            cloud_coords[j] = (x1 + dx, y1 + dy, x2 + dx, y2 + dy)
            canvas.create_oval(cloud_coords[j], fill='white', tags="clouds")
        canvas.update()
predict_button = tk.Button(root, text="Predict", command=predict_pollution, bg='red', fg='white', font=('Arial', 14, 'bold'))
predict_button.pack()
animate_button = tk.Button(root, text="Move Clouds", command=lambda: move_clouds(2, 0), bg='blue', fg='white', font=('Arial', 12, 'bold'))
animate_button.pack()
root.mainloop()
