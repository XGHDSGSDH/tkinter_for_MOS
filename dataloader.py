class Dataloader:
    def __init__(self,*,dir):
        self.list=[]
        if dir:
            import os
            self.list = os.listdir(dir)
            self.dir=dir
    
    def mess_up(self):
        import random
        self.list = random.shuffle(self.list)
        return self.list
    
    def save(self,*,file_pth):
        with open(file_pth,'w') as outfile:
            outfile.write(self.list)

    def load(self,*,file_pth):
        import os
        if os.path.isfile(file_pth):
            with open(file_pth) as readfile:
                self.list=eval(readfile)
            return True
        else:
            return False
        
    def __len__(self):
        return len(self.list)

    def __getitem__(self,idx):
        return self.list[idx]