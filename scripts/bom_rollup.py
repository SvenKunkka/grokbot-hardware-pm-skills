#!/usr/bin/env python3
"""BOM 成本汇总。CSV 需含列：part, qty, unit_cost（可选 category）。"""
import argparse, csv

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("csv"); ap.add_argument("--top", type=int, default=10)
    a = ap.parse_args(); rows = []
    with open(a.csv, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            ext = float(r["qty"]) * float(r["unit_cost"]); rows.append((r["part"], r.get("category", ""), ext))
    total = sum(r[2] for r in rows)
    print(f"BOM 总成本：{total:.4f}（{len(rows)} 行）")
    print(f"前 {a.top} 成本项：")
    for p, c, e in sorted(rows, key=lambda r: -r[2])[:a.top]:
        print(f"  {p:<30} {c:<12} {e:>10.4f}  {e / total * 100 if total else 0:5.1f}%")
    cats = {}
    for _, c, e in rows: cats[c or "未分类"] = cats.get(c or "未分类", 0) + e
    print("按类别：")
    for c, e in sorted(cats.items(), key=lambda x: -x[1]): print(f"  {c:<12} {e:>10.4f}  {e / total * 100 if total else 0:5.1f}%")

if __name__ == "__main__":
    main()
