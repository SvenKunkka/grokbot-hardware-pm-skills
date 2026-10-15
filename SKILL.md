---
name: hardware-cost-and-sourcing
description: 需要汇总 BOM 成本、对比多家供应商报价或建立项目风险登记时使用。
---
# 步骤
1. 把 BOM / 报价整理成 CSV（列名见 README），去掉不需要的敏感字段。
2. `bom_rollup.py` 得到总成本、前 10 成本项、类别占比；`rfq_compare.py` 按约定权重排名。
3. 结论写明：成本驱动项、可降本方向、推荐供应商及理由、单一来源风险。
4. 风险写入 `templates/risk_register.csv`，得分 = 可能性 × 影响，≥12 标红跟踪。
