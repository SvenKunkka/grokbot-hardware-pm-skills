# grokbot-hardware-pm-skills
硬件项目管理小工具：BOM 成本汇总、供应商报价加权对比、风险登记模板。

## 参考 / 可复用的上游
- [hwstar/BOMtools](https://github.com/hwstar/BOMtools)：KiCad/Eagle BOM 管理与 Octopart 询价
- [batuhngksl/procurement-rfq-toolkit](https://github.com/batuhngksl/procurement-rfq-toolkit)：加权比价思路
- [ctylerallen/BOM_Analyzer](https://github.com/ctylerallen/BOM_Analyzer)：分销商实时价格

上游都偏向特定 EDA 或分销商 API，本仓库实现的是**与数据源无关**的纯 CSV 版本（只依赖 Python 标准库）：
- `scripts/bom_rollup.py`：按数量 × 单价汇总，输出前 10 成本项与占比
- `scripts/rfq_compare.py`：多家报价按价格 / 交期 / 质量 / 账期加权打分
- `templates/risk_register.csv`：风险登记表模板

示例数据均为虚构。
