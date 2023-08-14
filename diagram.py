from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53


with Diagram("Diagram", show= True, direction="BT"):
    EC2("Instance") >> ELB("App_Load_Balancer") >> Route53("Route53")
