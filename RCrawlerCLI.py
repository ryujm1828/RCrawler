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
            


def main():
    cra = crawler();
    while(1):
        print("Seclect Number.\n1.Headers 2.Data 3.Cookies 4.Send 5~.Information");
        sel = int(input())
        if(sel == 1):
            print("Enter the number of headers. If you want to reset, enter -1")
            re = int(input())
            if re == -1:
                cra.InitHeaders()
            else:
                for i in range(re):
                    print("Input "+str(i)+"th key.")
                    key = input()
                    print("Input"+key+"'s value.")
                    value = input()
                    cra.InputHeaders(key,value);
        elif(sel == 2):
            print("Enter the number of datas. If you want to reset, enter -1")
            re = int(input())
            if re == -1:
                cra.InitData()
            else:
                for i in range(re):
                    print("Input "+str(i)+"th key.")
                    key = input()
                    print("Input"+key+"'s value.")
                    value = input()
                    cra.InputData(key,value)

        elif(sel == 3):
            print("Enter the number of cookies. If you want to reset, enter -1")
            re = int(input())
            if re == -1:
                cra.InitCookies()
            else:
                for i in range(re):
                    print("Input "+str(i)+"th key.")
                    key = input()
                    print("Input"+key+"'s value.")
                    value = input()
                    cra.InputCookies(key,value)
        elif(sel == 4):
            print("Input the url")
            url = input()
            print("Select 1.POST 2.GET")
            gorp = int(input())
            print("Crawling HTML 0.NO 1.YES")
            html = int(input())
            print("Crawling Cookies 0.NO 1.YES")
            cookie = int(input())

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
            print("Crawling Finished.\n\n")
        else:
            print("https://github.com/ryujm1828/RCrawler\n\n")


if __name__ == '__main__':
    main()
