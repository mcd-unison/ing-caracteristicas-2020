import pandas as pd
from pandas_profiling import ProfileReport 

insurance = pd.read_csv("insurance.cvs")

profile = ProfileReport(
    insurance, 
    explorative=True,
    title='Pandas Profiling Report', 
    html={'style':{'full_width':True}}
) 
profile.to_file("insurance-pandas-profiler.html")