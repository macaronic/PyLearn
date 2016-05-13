import tkinter


class Calc():
    def __init__(self):

        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, tkinter.END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "minus":
            self.total -= self.current
        if self.op == "times":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current )
        if self.op_pending:
            self.do_sum()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        self.current = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)



sum1 = Calc()
root = tkinter.Tk()
calc = tkinter.Frame(root)
calc.grid()

root.title("Sopf calc MA FAKA")
text_box = tkinter.Entry(calc, justify=tkinter.RIGHT)
text_box.grid(row=0, column=0, columnspan=3, pady=5)
text_box.insert(0, "0")

numbers = "789456123"
i = 0
bttn = []
for j in range(1, 4 ):
    for k in range( 3 ):
        bttn.append( tkinter.Button( calc, text=numbers[i] ) )
        bttn[i].grid( row=j, column=k, pady=5 )
        bttn[i]["command"] = lambda x=numbers[i]: sum1.num_press( x )
        i += 1

bttn_0 = tkinter.Button( calc, text="0" )
bttn_0["command"] = lambda: sum1.num_press( 0 )
bttn_0.grid( row=4, column=1, pady=5 )

bttn_div = tkinter.Button( calc, text=chr( 247 ) )
bttn_div["command"] = lambda: sum1.operation( "divide" )
bttn_div.grid( row=1, column=3, pady=5 )

bttn_mult = tkinter.Button( calc, text="x" )
bttn_mult["command"] = lambda: sum1.operation( "times" )
bttn_mult.grid( row=2, column=3, pady=5 )

point = tkinter.Button( calc, text="." )
point["command"] = lambda: sum1.num_press( "." )
point.grid( row=4, column=0, pady=5 )

add = tkinter.Button( calc, text="+" )
add["command"] = lambda: sum1.operation( "add" )
add.grid( row=4, column=3, pady=5 )

neg = tkinter.Button( calc, text="+/-" )
neg["command"] = sum1.sign
neg.grid( row=5, column=0, pady=5 )

##clear["command"] = sum1.calcel
#clear.grid( row=5, column=1, pady=5 )

all_clear = tkinter.Button( calc, text="LAIN" )
all_clear["command"] = sum1.all_cancel
all_clear.grid( row=5, column=2, pady=5 )

equals = tkinter.Button( calc, text="=" )
equals["command"] = sum1.calc_total
equals.grid( row=5, column=3, pady=5 )

root.mainloop( )
