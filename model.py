import json
class CleanJson():
    def __init__(self,path):
        self.path = path
    
    def read_json(self,path):
        try:
            with open(path,"r") as f:
                data = json.load(f)
                return data
            
        except Exception as e:
            print(f"{e},we cant open file")
            
    def cleanItem(self,data):
        return " ".join(data.strip().split())
        
    def clean_file(self,data):
        
        if isinstance(data,str):
            data = self.cleanItem(data=data)
            return data
        elif isinstance(data,list):
            data = [self.clean_file(item) for item in data]
            return data    
        elif isinstance(data,dict):
            cleand = {}
            for key,vlaue in data.items():
                cleand[key] = self.clean_file(vlaue)
            return cleand
    def write_file(self,path,out_path):
        try:
            data = self.read_json(path)
            clean_data = self.clean_file(data)
            with open(out_path,"w") as f:
                json.dump(clean_data,f,indent=4) 
                return "every thing is ok now"
        except Exception as e:
            return f"{e}:we canr acsses file sorry"
        