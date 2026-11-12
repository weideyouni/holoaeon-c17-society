# -*- coding: utf-8 -*-
"""C17 Gate —— 社会仓（制度收敛·主相金/副相火）
================================================================================
  · 第一性原理问题：个体如何与制度文化互动
  · 神龟（保存基线族）：保存参与历史与制度认知
  · 神马（推演路径族）：推演公共表达与协作路径
  · N19 派生声明：本仓=N19 holoaeon（github.com/weideyouni/holoaeon，唯一归零
    锚·唯一全局观测者）机制在本领域的正交投影。机制不在本仓重写——
    复用映射见 README（指针纪律的仓库版：派生装配，不复制实现）。
  · 集群账本：holoaeon/c18_cluster.py（19×19 耦合矩阵+边 Schema）。
  · 纯标准库零依赖·独立可运行（clone 即跑）。
"""
from __future__ import annotations

import hashlib
import json
import sys
from typing import List

CANG_ID = "C17"
REPO = "holoaeon-c17-society"
DOMAIN = "社会"
QUESTION = "个体如何与制度文化互动"
PHASE_MAIN = "金"
PHASE_SUB = "火"
ROLE = "制度收敛"
TURTLE = "保存参与历史与制度认知"
HORSE = "推演公共表达与协作路径"
SEAL = "潮起开门，潮落闭嘴"

CHAIN = {
    "id": CANG_ID,
    "repo": REPO,
    "n19_anchor": "github.com/weideyouni/holoaeon",
    "cluster_ledger": "holoaeon/c18_cluster.py",
    "ring": 19,
    "batch": "V55",
}


class CangGate:
    """C17 总闸：注册完整性自检（同构骨架·S1/S2 可测）。"""

    def self_check(self) -> dict:
        fields_ok = all([CANG_ID, REPO, DOMAIN, QUESTION, PHASE_MAIN,
                         PHASE_SUB, ROLE, TURTLE, HORSE])
        return {
            "ok": fields_ok and CANG_ID.startswith("C") and
                  REPO.startswith("holoaeon-c"),
            "cang_id": CANG_ID, "domain": DOMAIN, "phase_main": PHASE_MAIN,
            "seal": SEAL,
        }


def probe() -> dict:
    return CangGate().self_check()


def fingerprint() -> dict:
    return {
        "cang": CANG_ID, "repo": REPO, "domain": DOMAIN,
        "sha256": hashlib.sha256(
            ("%s-v1:" % REPO + SEAL).encode("utf-8")).hexdigest(),
        "seal": SEAL,
    }


def _main(argv: List[str]) -> int:
    cmd = argv[1] if len(argv) > 1 else "probe"
    if cmd == "probe":
        out = probe()
    elif cmd == "fingerprint":
        out = fingerprint()
    else:
        print("usage: python -m holoaeon_c17_society [probe|fingerprint]",
              file=sys.stderr)
        return 2
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out.get("ok", True) else 1


if __name__ == "__main__":
    raise SystemExit(_main(["c17_society"] + sys.argv[1:]))
