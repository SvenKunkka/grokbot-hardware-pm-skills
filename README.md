<!-- SVENKUNKKA-README-NAV:BEGIN -->
[English overview](#project-overview-en) · [中文项目说明](#project-overview-zh) · [Maintainer on X / 维护者 X](https://x.com/Svenu1s5)
<!-- SVENKUNKKA-README-NAV:END -->

<!-- SVENKUNKKA-PROJECT-INFO:BEGIN -->

<a id="project-overview-en"></a>
## English project overview

A CSV-based toolkit for hardware project management: BOM quantity-times-price totals, top-ten cost contributors and shares, weighted supplier comparison, and a risk-register template, independent of specific EDA or distributor APIs.

**Getting started:** Use `scripts/bom_rollup.py` for BOM totals, `scripts/rfq_compare.py` for quotes, and `templates/risk_register.csv` for risks. See `SKILL.md` for the workflow.

**Scope:** Scripts use only the Python standard library. Sample data is fictional; rankings depend on input data and agreed weights.

**Repository maintainer / 仓库维护者:** [SvenKunkka](https://github.com/SvenKunkka) · [X / Twitter](https://x.com/Svenu1s5)

<a id="project-overview-zh"></a>
## 中文项目说明

面向硬件项目管理的 CSV 工具集，包含 BOM 数量乘单价汇总、前十成本项及占比分析、供应商报价加权比较和风险登记模板，不依赖特定 EDA 或分销商 API。

**使用入口：** 使用 `scripts/bom_rollup.py` 汇总 BOM，使用 `scripts/rfq_compare.py` 比较报价，风险模板位于 `templates/risk_register.csv`；流程见 `SKILL.md`。

**范围说明：** 脚本只依赖 Python 标准库；示例数据均为虚构，评分结果取决于输入与约定权重。

<!-- SVENKUNKKA-PROJECT-INFO:END -->

---



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


