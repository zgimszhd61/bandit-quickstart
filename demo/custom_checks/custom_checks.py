import bandit
from bandit.core import test_properties

@test_properties.accepts_baseline
def check_user_input_to_os_system(context):
    # 检查是否是os.system调用
    if context.call_function_name_qual == 'os.system':
        # 获取调用参数
        arg = context.get_call_arg_at_position(0)
        if arg:
            # 检查参数是否来自用户输入
            if 'request' in arg:
                return bandit.Issue(
                    severity=bandit.HIGH,
                    confidence=bandit.HIGH,
                    text="os.system is called with user-controlled input, potential security issue."
                )
    return None

