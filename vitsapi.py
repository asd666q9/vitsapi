# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 10:51:39 2023

@author: Administrator
"""

import httpx

import json
import time
import base64


qq="370837546"
pwd=""    #在群691432604 内输入#SOV 验证码 获取你qq的验证码
params = {"account": qq, "code": pwd}


headers = {
   'uId': qq,
   'token': pwd,
   'Content-Type': 'application/json'
}


name_list=[
    [0,3,122,"宵宫","原神","zh"],
    [1,3,123,"托马","原神","zh"],
    [2,3,124,"优菈","原神","zh"],
    [3,3,125,"雷电将军","原神","zh"],
    [4,3,126,"早柚","原神","zh"],
    [5,3,127,"珊瑚宫心海","原神","zh"],
    [6,3,128,"五郎","原神","zh"],
    [7,3,129,"九条裟罗","原神","zh"],
    [8,3,130,"荒泷一斗","原神","zh"],
    [9,3,131,"埃洛伊","原神","zh"],
    [10,3,133,"八重神子","原神","zh"],
    [11,3,134,"神里绫人","原神","zh"],
    [12,3,135,"夜兰","原神","zh"],
    [13,3,136,"久岐忍","原神","zh"],
    [14,3,142,"纳西妲","原神","zh"],
    [15,3,195,"希儿","崩坏三","zh"],
    [16,3,197,"黑希儿","崩坏三","zh"],
    [17,3,316,"多莉","原神","ja"],
    [18,3,324,"胡桃","原神","ja"],
    [19,3,329,"可莉","原神","ja"],
    [20,3,330,"心海","原神","ja"],
    [21,3,552,"派蒙","原神","zh"],
    [22,3,339,"派蒙","原神","ja"],
    [23,4,10,"天童爱丽丝","碧蓝档案","ja"],
    [24,5,10,"一之濑明日奈","碧蓝档案","ja"],
    [25,6,10,"白洲梓","碧蓝档案","ja"],
    [26,7,10,"空崎日奈","碧蓝档案","ja"],
    [27,8,10,"小鸟游星野","碧蓝档案","ja"],
    [28,9,10,"银镜伊织","碧蓝档案","ja"],
    [29,10,10,"久田泉奈","碧蓝档案","ja"],
    [30,11,10,"角楯花凛","碧蓝档案","ja"],
    [31,12,10,"圣园未花","碧蓝档案","ja"],
    [32,13,10,"霞泽美游","碧蓝档案","ja"],
    [33,14,10,"砂狼白子","碧蓝档案","ja"],
    [34,3,0,"特别周","赛马娘","ja"],
    [35,3,1,"无声铃鹿","赛马娘","ja"],
    [36,3,2,"东海帝皇","赛马娘","ja"],
    [37,3,3,"丸善斯基","赛马娘","ja"],
    [38,3,4,"富士奇迹","赛马娘","ja"],
    [39,3,5,"小栗帽","赛马娘","ja"],
    [40,3,6,"黄金船","赛马娘","ja"],
    [41,3,7,"伏特加","赛马娘","ja"],
    [42,3,8,"大和赤骥","赛马娘","ja"],
    [43,3,9,"大树快车","赛马娘","ja"],
    [44,3,10,"草上飞","赛马娘","ja"],
    [45,3,12,"目白麦昆","赛马娘","ja"],
    [46,3,15,"成田白仁","赛马娘","ja"],
    [47,3,16,"鲁道夫象征","赛马娘","ja"],
    [48,3,19,"星云天空","赛马娘","ja"],
    [49,3,22,"琵琶晨光","赛马娘","ja"],
    [50,3,29,"米浴","赛马娘","ja"],
    [51,3,87,"神里绫华","原神","zh"],
    [52,3,91,"荧","原神","zh"],
    [53,3,97,"温迪","原神","zh"],
    [54,3,113,"迪奥娜","原神","zh"],
    [55,3,115,"刻晴","原神","zh"],
    [56,3,119,"胡桃","原神","zh"],
    [57,15,0,"可可萝","公主连结","ja"],
    [58,16,10,"凯露","公主连结","ja"],
    [59,17,10,"佩可莉姆","公主连结","ja"],
    [60,18,0,"高咲侑","虹咲","ja"],
    [61,18,1,"上原步梦","虹咲","ja"],
    [62,18,2,"中须霞","虹咲","ja"],
    [63,18,3,"樱坂雫","虹咲","ja"],
    [64,18,4,"朝香果林","虹咲","ja"],
    [65,18,5,"宫下爱","虹咲","ja"],
    [66,18,6,"优木雪菜","虹咲","ja"],
    [67,18,7,"天王寺璃奈","虹咲","ja"],
    [68,18,8,"三船栞子","虹咲","ja"],
    [69,18,9,"艾玛·维尔德","虹咲","ja"],
    [70,18,10,"钟岚珠","虹咲","ja"],
    [71,18,11,"米娅·泰勒","虹咲","ja"],
    [72,18,12,"近江彼方","虹咲","ja"],
    [73,19,0,"小埋","干物妹","ja"],
    [74,20,0,"秋蒂","B站主播","zh"],
    [75,21,0,"海老名","干物妹","ja"],
    [76,23,0,"小埋","干物妹","zh"],
    [77,22,0,"土间大平","干物妹","ja"],
    [78,22,1,"土间大平","干物妹","zh"],
    [79,24,10,"伊蕾娜","魔女之旅","ja"],
    [80,25,0,"双尾彗星","B站主播","zh"],
    [81,26,0,"心羽萝妮","日本主播","ja"],
    [82,27,0,"布良梓","柚子社","ja"],
    [83,27,1,"绫地宁宁","柚子社","ja"],
    [84,27,2,"朝武芳乃","柚子社","ja"],
    [85,27,3,"在原七海","柚子社","ja"],
    [86,27,10,"菲呂菈","花落冬阳","gd"],
    [87,28,0,"安兹(骨王)","overload","ja"],
    ]

   
    
class model:

    def __init__(self,modelId:int,roleId:str):
        self.data={
            "modelId": 0,
            "roleId": "",
            "text": "[ZH]你好[ZH]"
        }
        self.modelId=modelId
        self.roleId=roleId
        self.data["modelId"]=modelId
        self.data["roleId"]=roleId
        
        
    def get_base64_by_text(self,text:str,lan:str):
        
        if lan.lower()=="zh":
            self.data["text"]=f"[ZH]{text}[ZH]"
        elif lan.lower()=="ja":
            self.data["text"]=f"[JA]{text}[JA]"
        elif lan.lower()=="gd":
            self.data["text"]=f"[GD]{text}[GD]"
        else:
            return False
        
        url="http://soundai.natapp1.cc/vits/genByText"
        
        
    
        
        print(self.data)
        print(headers)
        conn=httpx.post(url,headers=headers,data=json.dumps(self.data))
        return json.loads(conn.text)["data"]
        
    def get_voice_by_base64(self,base):
        url = f"http://soundai.natapp1.cc/vits/getBase64ById?uuid={base}"
        response = httpx.get(url,headers=headers)
        return  json.loads(response.text)
        
        
    def get_voice_by_text(self,text:str,lan:str):
        
        base=self.get_base64_by_text(text,lan)
        
        status=False
        
        for i in range(100):
            print("tring get result")
            time.sleep(0.5)
            content=self.get_voice_by_base64(base)
            if content["code"]==0:
                status=True
                break
    
        return content["data"]
    
        
        
    
def login():
    url="http://soundai.natapp1.cc/sys/loginByC"
    
    
    conn = httpx.post(url, data=params)
    print(conn.text)



def get_model():
    
    
    url="http://soundai.natapp1.cc/vits/getAllMod/"
    
    conn = httpx.get(url,headers=headers)
    return json.loads(conn.text)





def print_name_list(response):

    for c in response["data"]:
        index=response["data"].index(c)
        modelId=c["code"].split("-")[0]
        roleId=c["code"].split("-")[1]
        title=c["title"]
        
        
        if "中文" in title:
            lan="zh"
        elif "日语"in title:
            lan="ja"
        elif "粤语"in title:
            lan="gd"
        
        name=c["title"].split("->")[0]
        
        anime=title.split("[")[1].split("]")[0]
        
        print(f"[{index},{modelId},{roleId},\"{name}\",\"{anime}\",\"{lan}\"],")
        
    
    
def get_model_by_name(name):
    
    for i in name_list:
        if i[3]==name:
            return model(i[1],str(i[2]))
        
    return False   

def get_model_by_index(index):
    

    i=name_list[index]
    return model(i[1],str(i[2]))
        

    

if __name__=="__main__":
    #login()


    m=get_model_by_name("纳西妲")

    mp3_base64=m.get_voice_by_text("旅行者，快滚去学习！", "zh")

    decoded_mp3 = base64.b64decode(mp3_base64)


    with open("output.mp3","wb") as f:
        f.write(decoded_mp3)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
