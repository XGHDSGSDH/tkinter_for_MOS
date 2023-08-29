class Judgement:
    def __init__(self,*,file_pth):
        self.dic={}
        self.load(self,file_pth=file_pth)

    def add(self,*,key,value):
        if key in self.dic.keys():
            self.dic[key].append(value)
        else:
            self.dic[key]=[value]

    def change(self,*,key,value,idx=-1):
        if key in self.dic.keys():
            self.dic[key][idx]=value
        else:
            self.dic[key]=[value]

    def __len__(self):
        return len(self.dic.keys())
    
    def __getitem__(self,key):
        if key in self.dic.keys():
            return self.dic[key]
        else:
            return None
    
    def save(self,*,file_pth):
        with open(file_pth,'w') as outfile:
            outfile.write(str(self.dic))

    def load(self,*,file_pth):
        import os
        if os.path.is_file(file_pth):
            with open(file_pth) as readfile:
                self.dic=eval(readfile.read())
                return True
        else:
            return False
        
    def evaluate(self,*,keys):
        import math
        arr=[]
        for key in keys:
            if key in self.dic.keys():
                for score in self.dic[key]:
                    arr.append(score)
        mean=math.fsum(arr)/len(arr)
        variance=sum([((x-mean)**2) for x in arr])/(len(arr)-1)
        return (mean,variance)