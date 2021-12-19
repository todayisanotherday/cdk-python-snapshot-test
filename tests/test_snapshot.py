import aws_cdk as cdk
from aws_cdk.assertions import Template
from app.app_stack import AppStack

def test_app_stack_snapshot(snapshot):
    app = cdk.App()

    # Stack作成
    app_stack = AppStack(
        app, "AppStack"
    )

    # StackからTemplateを生成
    template = Template.from_stack(app_stack)

    # 差分が無いことを比較
    assert template.to_json() == snapshot

