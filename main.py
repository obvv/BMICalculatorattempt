import tkinter

window = tkinter.Tk()
window.title("BMİ CALCULATİON")
window.minsize(width=350, height=250)


def height_entry():
    h_height = my_entry1.get()

    if h_height.isdigit():
        h_height= int(h_height)/100
    else:
        print("Please enter integer")

    w_weight = my_entry2.get()
    if w_weight.isdigit():
        w_weight = int(w_weight)

    else:
        print("Please enter integer")

    x = h_height*h_height
    total_bmi = w_weight/x
    my_label4 = tkinter.Label(text=round(total_bmi,2), font=('Arial', 10,))
    my_label4.pack()

    if total_bmi <= 18.5:
        my_label3 = tkinter.Label(text="You are weak", font=('Arial', 10,))
        my_label3.pack()
    elif 18.5<total_bmi <=25:
        my_label3 = tkinter.Label(text="You are weakness", font=('Arial', 10, ))
        my_label3.pack()
    elif 25<total_bmi <=30:
        my_label3 = tkinter.Label(text="You are 1.degree obese ", font=('Arial', 10,))
        my_label3.pack()
    elif 30<total_bmi <=35:
        my_label3 = tkinter.Label(text="You are 2.degree Obese", font=('Arial', 10, ))
        my_label3.pack()
    else:
        my_label3 = tkinter.Label(text="You are 3.degree obese", font=('Arial', 10,))
        my_label3.pack()

my_label1 = tkinter.Label(text="Enter your height(cm)",font=('Arial', 10, ))
my_label1.pack()

my_entry1 = tkinter.Entry(width=20)
my_entry1.pack()

my_label2 = tkinter.Label(text="Enter your weight(kg)",font=('Arial', 10,))
my_label2.pack()

my_entry2 = tkinter.Entry(width=20)
my_entry2.pack()

button = tkinter.Button(text="enter",command=height_entry,)
button.pack()


window.mainloop()