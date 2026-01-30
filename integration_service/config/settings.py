"""Configuration management for Integration Service."""  
import os  
from dotenv import load_dotenv  
  
load_dotenv()  
  
class Settings:  
    """Integration Service settings"""  
      
    def __init__(self):  
        # Service URLs  
        self.atomspace_url = os.environ['ATOMSPACE_API_URL']
        self.miner_url = os.environ['NEURAL_MINER_URL']
          
        # Timeouts 
        self.atomspace_timeout = int(os.environ['ATOMSPACE_TIMEOUT'])  
        self.miner_timeout = int(os.environ['MINER_TIMEOUT'])  
          
        # CSV caching  
        self.csv_cache_dir = os.environ['CSV_CACHE_DIR']
          
        # Shared volume  
        self.shared_volume_path = os.environ['SHARED_VOLUME_PATH']
  
settings = Settings()