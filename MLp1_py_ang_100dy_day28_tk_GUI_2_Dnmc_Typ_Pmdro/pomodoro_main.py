import  tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

tiMer = None
check_text = ' '

# ---------------------------- TIMER RESET ------------------------------- # 
def resEt():
    winDow.after_cancel(tiMer)
    can_vas.itemconfig(timer_text, text = "00:00")
    heading.config(text = "Timer")
    check.config(text = '')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
reps = 0
    # To invoke count_down() when button is clicked
def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if (reps > 0) and (reps % 8 == 0):
        count_down(long_break)
        heading.config(text = "LONG Break", fg =  RED)
        reps = 0
    elif (reps > 0) and (reps % 2 == 0):
        count_down(short_break)
        heading.config(text = "SHORT Break", fg =  PINK)
    else:
        count_down(work_time)
        heading.config(text = "WORK time", fg =  GREEN)
    
    print(reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global tiMer
    if count > 0:
        remain_min = math.floor(count/60)
        remain_sec = count % 60
        if remain_sec <= 9:
            # remain_sec = "00" # dynamic type occuring "int" to "string" auto-conversion
            # remain_sec = "0" + str(remain_sec) # dynamic type occuring "int" to "string" auto-conversion
            remain_sec = f"0{remain_sec}"   # dynamic type occuring "int" to "string" auto-conversion
        # can_vas.itemconfig() is like Label.coonfig()
        can_vas.itemconfig(timer_text, text = f"{remain_min}:{remain_sec}")
        tiMer = winDow.after(1000, count_down, count -1 )
    else:
        global check_text
        if reps % 2:
            check_text += '✔'
            check.config(text = check_text)
        start_timer()
    

# ---------------------------- UI SETUP ------------------------------- #

winDow = tkinter.Tk()
winDow.minsize(height = 300, width = 420)
winDow.title("Pomdoro GUI app")

# Back ground color
winDow.config(bg = YELLOW)
winDow.config(padx =100, pady = 50)


#including image
    # PhotoImage is needed to attach image to tkinter
pic_tomato = tkinter.PhotoImage(file= "./tomato.png")
    # crfreating Canvas for image: Its like a artist canvas, it allows layering
can_vas = tkinter.Canvas(width = 220, height = 250, bg = YELLOW, highlightthickness= 0)
            # highlightthickness= 0 to disable canvas border
    # attaching image to canvas. "bg" for background color, "image" to insert image
    # must include x, y position
can_vas.create_image(110, 125, image=pic_tomato)
    # wont show unless use a geometry manager: pack(), place() or grid()
# Grid is relative. To center the position  padding added to window
can_vas.grid(column = 1, row = 1)

# Adding text top of image. Modify the text, use "fill" for color
timer_text = can_vas.create_text(110, 135, text = "00:00", fill = "white", font = (FONT_NAME, 20, "bold"))

# buttons and griding
# fg - foreground color/ text color , bg back-ground color
heading = tkinter.Label(text = "Timer", bg = YELLOW, fg =  GREEN, font = (FONT_NAME, 36, "bold") )
heading.grid(column = 1, row = 0)

# # "bd" or "borderwidth" for border thickness
button_start = tkinter.Button(text = "Start", bg = RED, fg =  "white",  borderwidth = 0, font = (FONT_NAME, 12, "bold") )
    # start_timer will invoke count_down() when button is clicked
button_start.config(command = start_timer)
button_start.grid(column = 0, row = 2)


button_reset = tkinter.Button(text = "Reset", bg = RED, fg =  "white", bd = 0, font = (FONT_NAME, 12, "bold") )
    # resEt() will invoke  when button is clicked
button_reset.config(command = resEt)
button_reset.grid(column = 2, row = 2)

check = tkinter.Label(text = check_text, bg = YELLOW, fg = GREEN ,font = (FONT_NAME, 12))
check.grid(column = 1, row = 3)


winDow.mainloop()


# python pomodoro_main.py