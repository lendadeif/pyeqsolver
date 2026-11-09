import json
class JSONExporter:
    def __init__(self,output_path):
        self.output_path=output_path
#########  -0.0
    def save(self,solutions:dict,metadata):
        solutions={k:round(v,4) for k,v in solutions.items()}
        result={
            "status":"SUCCESS",
            "system_info":metadata,
            "solution":solutions
        }
        with open(self.output_path,"w") as f:
            json.dump(result,f,indent=4)

    def save_error(self,exc):
        result={
            "status":"ERROR",
            "error_type":type(exc).__name__,
            "message":str(exc)
        }
        with open(self.output_path,"w") as f:
            json.dump(result,f,indent=4)