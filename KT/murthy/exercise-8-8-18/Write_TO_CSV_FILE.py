from datetime import datetime
from csv


ct = datetime.now()
cts = ct.strftime("%d-%b-%Y-%H-%M")
fo = open("job_list_" + cts  + ".csv" , "w")
writer=csv.writer(fo)
writer.writerow(["JOBID","ORGNIZATIONS","GB","GF"])
