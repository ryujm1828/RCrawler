#pip install requests
import webbrowser
import requests as rq;
from tkinter import *;
from tkinter import ttk
from tkinter.messagebox import *

class crawler:
    def __init__(self):
        self.data = {}
        self.url = ""
        self.cookie = {}
        self.header = {}
    
    def InitData(self):
        self.data = {}

    def InitCookies(self):
        self.cookie = {}

    def InitHeaders(self):
        self.header = {}

    def InputURL(self,u):
        self.url = u

    def InputData(self,key,value):
        self.data[key] = value

    def InputCookies(self,key,value):
        self.cookie[key] = value

    def InputHeaders(self,key,value):
        self.header[key] = value

    def GetReq(self):
        try:
            self.res = rq.get(self.url, data = self.data, cookies = self.cookie, headers = self.header)
        except:
            showerror("Error","Error Occurred")


    def PostReq(self):
        try:
            self.res = rq.post(self.url, data = self.data, cookies = self.cookie, headers = self.header)
        except:
            showerror("Error","Error Occurred")

    def HtmlWrite(self,filename):
        try:
            html = self.res.content;
            f = open(filename + ".txt",'w', encoding="UTF-8")
            f.write("HTML Code)\n"+html.decode('UTF-8'))
            f.close
        except:
            print("error")
            

    def CookiesWrite(self,filename):
        try:
            f = open(filename + ".txt",'w')
            f.write("Cookies)\n")
            cookie = self.res.cookies
            for i in list(cookie):
                f.write(str(i))
                f.write("\n")
            f.close
        except:
            print("error")
            


cra = crawler()
cra.data = {}
cra.url = ""
cra.cookie = {}
cra.header = {}

#Create GUI
win = Tk()
win.title("RCrawler")
win.geometry("500x500")
win.resizable(0,0)

#Create 4 tabs
tabc = ttk.Notebook(win)

tab1 = ttk.Frame(tabc)
tab2 = ttk.Frame(tabc)
tab3 = ttk.Frame(tabc)
tab4 = ttk.Frame(tabc)
tab5 = ttk.Frame(tabc)

tabc.add(tab1,text="Headers")
tabc.add(tab2,text="Data")
tabc.add(tab3,text="Cookies")
tabc.add(tab4,text="Send")
tabc.add(tab5,text="Information")

tabc.pack(expand=1, fill='both')

#Header Tab


header_key = Entry(tab1)
header_val = Entry(tab1)

header_key.insert(0,"Key")
header_val.insert(0,"Value")

header_key.pack()
header_val.pack()

header_ins_btn = Button(tab1,text="Insert")
header_ins_btn.config(command =lambda: [cra.InputHeaders(header_key.get(),header_val.get()),header_list.insert(0,header_key.get()+":"+header_val.get()),header_val.delete(0,100),header_key.delete(0,100)])
header_ins_btn.pack()

header_list = Listbox(tab1,height =20, selectmode="extended")
header_list.yview()
header_list.pack()


header_init_btn = Button(tab1,text="Init")
header_init_btn.config(command =lambda:[cra.InitHeaders(),header_list.delete(0, header_list.size()-1)])
header_init_btn.pack()


#Data Tab

data_key = Entry(tab2)
data_val = Entry(tab2)

data_key.insert(0,"Key")
data_val.insert(0,"Value")

data_key.pack()
data_val.pack()

data_ins_btn = Button(tab2,text="Insert")
data_ins_btn.config(command =lambda: [cra.InputData(data_key.get(),data_val.get()),data_list.insert(0,data_key.get()+":"+data_val.get()),data_key.delete(0,100),data_val.delete(0,100)])
data_ins_btn.pack()

data_list = Listbox(tab2,height =20, selectmode="extended")
data_list.yview()
data_list.pack()


data_init_btn = Button(tab2,text="Init")
data_init_btn.config(command =lambda:[cra.InitData(),data_list.delete(0, data_list.size()-1)])
data_init_btn.pack()

#Cookie Tab

cookie_key = Entry(tab3)
cookie_val = Entry(tab3)

cookie_key.insert(0,"Key")
cookie_val.insert(0,"Value")

cookie_key.pack()
cookie_val.pack()

cookie_ins_btn = Button(tab3,text="Insert")
cookie_ins_btn.config(command =lambda: [cra.InputCookies(cookie_key.get(),cookie_val.get()),cookie_list.insert(0,cookie_key.get()+":"+cookie_val.get()),cookie_key.delete(0,100),cookie_val.delete(0,100)])
cookie_ins_btn.pack()

cookie_list = Listbox(tab3,height =20, selectmode="extended")
cookie_list.yview()
cookie_list.pack()


cookie_init_btn = Button(tab3,text="Init")
cookie_init_btn.config(command =lambda:[cra.InitCookies(),cookie_list.delete(0, cookie_list.size()-1)])
cookie_init_btn.pack()

#Send Tab

send_url = Entry(tab4)
send_url.insert(0,"Url")

send_url.pack()

gorp = IntVar()
html = IntVar()
cookie = IntVar()

send_post = Radiobutton(tab4,text="Post",variable=gorp,value="1")
send_get = Radiobutton(tab4,text="Get",variable=gorp,value="2")

send_post.pack()
send_get.pack()

send_html=Checkbutton(tab4,text="Html",variable=html)
send_cookie=Checkbutton(tab4,text="Cookies",variable=cookie)
send_html.pack()
send_cookie.pack()

send_btn = Button(tab4,text="Send")
send_btn.config(command =lambda:[send(cra,send_url.get(),gorp.get(),html.get(),cookie.get())])
send_btn.pack()


def send(cra,url,gorp,html,cookie):
    cra.url = url;
    if(gorp == 1):     #Post 
        cra.PostReq()
        if(html == 1):
            cra.HtmlWrite("HtmlPost")
        if(cookie == 1):
            cra.CookiesWrite("CookiesPost")
    elif(gorp == 2):    #Get
        cra.GetReq()
        if(html == 1):
            cra.HtmlWrite("HtmlPost")
        if(cookie == 1):
            cra.CookiesWrite("CookiesPost")

#Information Tab
inf_git = Label(tab5,text="Github:https://github.com/ryujm1828/WebCrawler",font = ("","13"))
inf_git.pack()
inf_btn = Button(tab5,text="Go to Github")
inf_btn.config(command =lambda:[webbrowser.open('https://github.com/ryujm1828/WebCrawler')])
inf_btn.pack()


win.mainloop()
