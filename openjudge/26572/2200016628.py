import sys

class Node:
    def __init__(self, value, left=None, right=None, is_op=False, precedence=0):
        self.value = value
        self.left = left
        self.right = right
        self.is_op = is_op # 是否是操作符节点
        self.precedence = precedence # 操作符的优先级 (0 for num, 1 for +, 2 for *)


def get_precedence(op_char): #获取优先级
    if op_char == '+':
        return 1
    elif op_char == '*':
        return 2
    return 0

# 将输入字符串转换为一个 Token 列表
# 注意原表达式中两个数字连接在一起是一个二位数，不能拆开
def tokenize(expression_str):
    tokens = []
    i = 0
    while i < len(expression_str):
        char = expression_str[i]
        if char.isdigit():
            num_str = ""
            while i < len(expression_str) and expression_str[i].isdigit():
                num_str += expression_str[i]
                i += 1
            tokens.append(num_str)
            continue
        elif char in ('+', '*', '(', ')'):
            tokens.append(char)
        i += 1
    return tokens

tokens = []
current_token_index = 0 #跟踪当前正在解析的 Token

def peek_token():#查看下一个即将被处理的 token，但不移动 current_token_index
    if current_token_index < len(tokens):
        return tokens[current_token_index]
    return None

def consume_token():#获取当前 token 并将 current_token_index 向前移动一位。
    global current_token_index
    if current_token_index < len(tokens):
        token = tokens[current_token_index]
        current_token_index += 1
        return token
    raise ValueError("Unexpected end of expression")


def parse_factor():#最底层，只处理数字和括号
    token = peek_token() #查看下一个 token
    if token == '(':
        consume_token()  # 消费左括号 '('
        node = parse_expression()  # 递归解析括号内的整个表达式
        # 期望括号内表达式解析完成后是右括号 ')'
        if peek_token() != ')': # 异常处理：如果期望是 ')' 但不是，表示括号不匹配
            raise ValueError("Mismatched parentheses: expected ')'")
        consume_token()  # 消费右括号 ')'
        return node # 返回括号内表达式的 AST 节点
    elif token.isdigit():# 检查 token 是否存在且是数字
        consume_token()  # 消费数字 token
        return Node(int(token), is_op=False, precedence=0) # 创建一个数字节点
    else:
        raise ValueError(f"Unexpected token in parse_factor: {token}")


def parse_term():#处理乘法
    left_node = parse_factor()
    while peek_token() == '*':
        op = consume_token()  # Consume '*'
        right_node = parse_factor()
        left_node = Node(op, left=left_node, right=right_node, is_op=True, precedence=get_precedence(op))
    return left_node


def parse_expression():#处理加法
    left_node = parse_term()
    while peek_token() == '+':
        op = consume_token()  # Consume '+'
        right_node = parse_term()
        left_node = Node(op, left=left_node, right=right_node, is_op=True, precedence=get_precedence(op))
    return left_node


def parse_full_expression(expression_str):#解析整个表达式字符串并返回 AST 根节点。
    global tokens, current_token_index
    tokens = tokenize(expression_str)
    current_token_index = 0
    ast_root = parse_expression()
    if current_token_index != len(tokens):
        raise ValueError("Extra tokens at end of expression")
    return ast_root

# 遍历抽象语法树 (AST) 并将其转换回字符串表达式
#从根开始输出时，只有当：当前运算优先级 < 父节点的优先级（比如 + 嵌套在 * 里），或者当前运算优先级 == 父节点，但你是右孩子（因为左结合），才加括号。
def print_ast_simplified(node, parent_op_precedence=-1, is_right_child=False):#通过判断当前操作符优先级和父节点优先级的比较，是否是右孩子，来决定是否加括号。
    if not node.is_op:
        return str(node.value)  # 数字节点直接打印值

    current_op_precedence = node.precedence# 获取当前操作符节点的优先级。

    # 判断是否需要为当前节点对应的子表达式添加括号
    should_wrap = False

    # 规则1：当前操作符的优先级严格低于父操作符的优先级
    # 例如：A * (B + C) 中，(B + C) 的优先级 (1) < A * 的优先级 (2)，需要括号
    if current_op_precedence < parent_op_precedence:
        should_wrap = True
    # 规则2：当前操作符的优先级等于父操作符的优先级，并且当前节点是右孩子
    # 例如：1 + (2 + 3) 中，(2 + 3) 是右孩子，其优先级 (1) == 1 + 的优先级 (1)，需要括号以保留运算顺序。
    elif current_op_precedence == parent_op_precedence and is_right_child:
        should_wrap = True

    # 递归打印左右子节点
    # 左子节点永远不是其父节点的右孩子 (is_right_child=False)
    left_str = print_ast_simplified(node.left, current_op_precedence, False)
    # 右子节点永远是其父节点的右孩子 (is_right_child=True)
    right_str = print_ast_simplified(node.right, current_op_precedence, True)

    result = left_str + str(node.value) + right_str

    if should_wrap:
        return "(" + result + ")"
    else:
        return result

def main():
    for line in sys.stdin:
        expression = line.strip()
        ast_root = parse_full_expression(expression)
        # 根节点没有父节点，所以 parent_op_precedence 设为 -1 (最低)
        # 根节点也不是右孩子 (is_right_child=False)
        simplified_expression = print_ast_simplified(ast_root, -1, False)
        sys.stdout.write(simplified_expression + "\n")

if __name__ == "__main__":
    main()