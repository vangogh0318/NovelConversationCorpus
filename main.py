import re
import os
import jieba


def cutWord(str_data):
    seg_list=jieba.cut(str_data,cut_all=False)
    str_out="/".join(seg_list)+"/"
    return str_out
def findContent(str_raw):
    str_pat = re.compile(r'“(.*?)”')
    data = (str_pat.findall(str_raw))
    return data

def novelProcess(str_novel):
    str_out=""
    str_pat = re.compile(r'“(.*?)”')
    finditer=re.finditer(str_pat,str_novel)
    lastend=0
    for it in finditer:
        it_span=it.span()
        if it_span[0]-lastend>60:
            str_out+="E\n"
        lastend=it_span[1]
        str_out+="M "+cutWord(it.group())+"\n"
    return str_out



def writedata(str_data,str_filename):
    f=open("output/"+str_filename[0:3]+".txt","a",encoding='ansi')
    f.write(str_data)
    f.close()

#ff=open("Data/001.盘龙.txt","r",encoding="ansi")
#print(novelProcess(ff.read()))
#ff.close()
def main():
    for novelFile in os.listdir("Data/"):
        try:
            print(novelFile)
            f=open("Data/"+novelFile,'r',encoding="ansi")
            writedata(novelProcess(f.read()),novelFile)
            f.close()
        except Exception as err:
            try:
                print("Error begin:"+novelFile+"  "+str(err))
                f = open("Data/" + novelFile, 'r', encoding="utf-16")
                writedata(novelProcess(f.read()), novelFile)
                f.close()
            except Exception as err2:
                print("Error do not know:"+novelFile+"  "+str(err2))

#111.纳妾记.txt
def test():
    file_name="110.无极魔道.txt"
    ff=open("Data/"+file_name,"r",encoding="utf-16")
    writedata(findContent(ff.read()), file_name)
    ff.close()


def touchFile():
    f=open("min.txt","r",encoding="utf-8")
    for i in range(100):
        print(f.readline())

def combine():
    fw=open("out.txt","w",encoding="utf-8")
    for novelfile in os.listdir("output/"):
        print(novelfile)
        f=open("output/"+novelfile,"r",encoding="ansi")
        fw.write(f.read())
        f.close()
    fw.close()


#cutWord()
combine()
#touchFile()
#main()
#test()
