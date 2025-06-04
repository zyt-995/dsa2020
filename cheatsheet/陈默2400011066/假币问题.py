n = int(input())
for _ in range(n):
    comp1 = list(map(str, input().split()))
    comp2 = list(map(str, input().split()))
    comp3 = list(map(str, input().split()))

    truecoin = set()
    possible_heavy = set()
    possible_light = set()
    first_uneven = True  # 标记是否为第一次非平衡称量

    # 处理三次称量
    for k in [comp1, comp2, comp3]:
        left, right, status = k[0], k[1], k[2]
        if status == "even":
            # 将两边所有硬币标记为真币
            for c in left + right:
                truecoin.add(c)
        else:
            # 非平衡称量，动态更新候选集合
            if status == "up":
                # 左边重或右边轻（排除真币）
                current_heavy = {c for c in left if c not in truecoin}
                current_light = {c for c in right if c not in truecoin}
            elif status == "down":
                # 左边轻或右边重（排除真币）
                current_heavy = {c for c in right if c not in truecoin}
                current_light = {c for c in left if c not in truecoin}

            if first_uneven:
                # 第一次非平衡称量，初始化候选集合
                possible_heavy = current_heavy
                possible_light = current_light
                first_uneven = False
            else:
                # 后续非平衡称量，取交集以缩小范围
                possible_heavy &= current_heavy
                possible_light &= current_light

    # 最终检查候选
    light_candidates = possible_light - truecoin
    heavy_candidates = possible_heavy - truecoin

    if light_candidates:
        print(f"{light_candidates.pop()} is the counterfeit coin and it is light.")
    elif heavy_candidates:
        print(f"{heavy_candidates.pop()} is the counterfeit coin and it is heavy.")