def count_structures(pre, post):
    # 检查是否有重复字符
    if len(pre) != len(post):
        return 0
    if len(pre) == 0:
        return 1
    if pre[0] != post[-1]:
        return 0
    n = len(pre)
    if n == 1:
        return 1

    ans = 0

    # 常规分割方式：左子树非空
    left_root_pre = pre[1] if len(pre) > 1 else None
    if left_root_pre in post:
        left_root_post_idx = post.index(left_root_pre)
        left_post = post[:left_root_post_idx + 1]
        left_len = len(left_post)
        left_pre = pre[1:1 + left_len]
        right_pre = pre[1 + left_len:]
        right_post = post[left_root_post_idx + 1:-1]

        # 递归计算左右数目
        left_count = count_structures(left_pre, left_post)
        if left_count == 0:
            pass
        else:
            right_count = count_structures(right_pre, right_post)
            ans += left_count * right_count

    # 分割方式二：左子树为空，右子树非空
    if n >= 1:
        right_pre = pre[1:]
        right_post = post[:-1]
        if len(right_pre) == len(right_post) and len(right_pre) > 0:
            if right_pre[0] == right_post[-1]:
                right_count = count_structures(right_pre, right_post)
                ans += right_count

    return ans


def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        pre, post = line.split()
        # 检查前序和后序是否有重复字符
        if len(set(pre)) != len(pre) or len(set(post)) != len(post):
            print(0)
            continue
        # 检查长度是否相等
        if len(pre) != len(post):
            print(0)
            continue
        # 检查根是否相同
        if pre[0] != post[-1]:
            print(0)
            continue
        total = count_structures(pre, post)
        print(total)


if __name__ == "__main__":
    main()