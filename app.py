#!/usr/bin/env python3

import aws_cdk as cdk
from app.app_stack import AppStack

app = cdk.App()
AppStack(app, "AppStack")

app.synth()
