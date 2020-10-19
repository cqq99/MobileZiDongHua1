import  yaml
import os,sys

sys.path.append(os.getcwd())

#class GetData:
   # def anylyze_file( self,file_name):
file_name="search.yml"
filepath="../data/"+file_name
with open( filepath, "r", encoding="utf-8")as f:
    case_data = yaml.load(f,Loader=yaml.FullLoader)
    data_list = list()
    for i in case_data.values():
        data_list.append(i)
    print(case_data)
    print(data_list)
        #return data_list