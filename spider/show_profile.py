import codecs
import json
with open('D:/DevelopTool/PyCharm Community Edition 2023.2.5/PycharmProjects/KGQA_HLM/spider/json/data.json', encoding='utf-8')as f:
    data = json.load(f)

def get_profile(name):
    s=''
    for i in data[name]:
        st="<dt class = \"basicInfo-item name\" >"+ str(i)+" \
        <dd class = \"basicInfo-item value\" >"+str(data[name][i])+"</dd >"
        s+=st
    return s

