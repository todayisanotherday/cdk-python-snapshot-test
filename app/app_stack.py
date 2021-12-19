from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)
from constructs import Construct

class AppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "Vpc",
            cidr="10.0.0.0/16",
            max_azs=2,
        )

        # ec2.Instance(self, "Instance",
        #     vpc=vpc,
        #     instance_type=ec2.InstanceType.of(
        #         instance_class=ec2.InstanceClass.BURSTABLE3,
        #         instance_size=ec2.InstanceSize.MICRO,
        #     ),
        #     machine_image=ec2.AmazonLinuxImage(
        #         edition=ec2.AmazonLinuxEdition.STANDARD,
        #         generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
        #     ),
        #     vpc_subnets=ec2.SubnetType.PRIVATE_ISOLATED,
        # )
