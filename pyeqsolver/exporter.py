import json
class JSONEporter:
    def __init__(self,output_path):
        self.output_path=output_path
#########  -0.0
    def save(self,solutions:dict,metadata):
        solutions={k:round(v,4) for k,v in solutions.items()}
        with open(self.output_path,"w") as f:
            json.dump(solutions,f)

    def save_error(self,exc):
        ...