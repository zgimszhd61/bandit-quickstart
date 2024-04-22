# bandit-quickstart

为了使用 Bandit 编写自定义的静态代码分析规则并扫描一个样本，你需要了解如何扩展 Bandit 的基础功能。以下是一个详细的步骤说明，包括如何定义一个新的检查规则、将其集成到 Bandit 中，并使用这个新规则扫描一个 Python 示例文件。

### 步骤 1: 安装 Bandit

如果你还没有安装 Bandit，可以通过 pip 安装：

```bash
pip install bandit
```

### 步骤 2: 创建自定义规则

创建一个新的 Python 文件（比如叫做 `custom_checks.py`），在这个文件中定义你的自定义规则。这里我们创建一个简单的规则来检测是否在代码中直接使用了 `eval` 函数，因为这通常被认为是不安全的。

```python
import bandit
from bandit.core import test_properties

@test_properties.accepts_baseline
def check_for_eval(context):
    # 检测代码中是否使用了 eval
    if context.call_function_name_qual == 'eval':
        return bandit.Issue(
            severity=bandit.HIGH,
            confidence=bandit.HIGH,
            text="使用 eval 可能导致代码执行安全风险",
            lineno=context.get_lineno(),
        )

# 在测试集中注册这个检查
def register_checks(registry):
    registry.register_check(check_for_eval, checks='call')
```

### 步骤 3: 创建一个示例 Python 文件

创建一个示例 Python 文件 `example.py`，其中包含可能的安全问题。

```python
# 示例代码，其中包含使用 eval 的情况
def demo():
    eval("print('hello, world')")

if __name__ == "__main__":
    demo()
```

### 步骤 4: 运行 Bandit 并使用自定义规则

为了使用你的自定义规则扫描 `example.py` 文件，你需要在运行 Bandit 时指定自定义规则文件。可以通过以下命令来做：

```bash
bandit -r example.py -s custom_checks
```

这里 `-r` 代表递归扫描指定目录下的文件，`-s custom_checks` 指定了包含自定义检查规则的 Python 模块。

### 结果输出

执行上述命令后，Bandit 将分析 `example.py` 文件，并报告关于 `eval` 使用的信息。如果一切设置正确，你会看到关于使用 `eval` 的安全警告。

通过这个流程，你可以根据具体的需求定制自己的静态代码分析规则，使得 Bandit 能够针对特定的编码问题进行检查。这对于定制化的安全审计尤其有用。
