
---

## 2️⃣ `clinical-trial-supply-forecaster/README.md`

```markdown
# Clinical Trial Supply Forecaster  
治験サプライチェーン需要予測ツール

## 🌍 Overview (EN)

This project is a **transparent, rule-based forecaster** for clinical trial drug supply.

Given site-level weekly data (patients on treatment, dropout rate, stock on hand, lead time), it estimates:

- Weekly demand (with safety factor)
- Weeks until shortage
- Shortage risk flag (HIGH / LOW)

It exposes a FastAPI endpoint `/forecast_csv` that accepts a CSV upload and returns JSON.

---

## 🌏 概要（日本語）

本プロジェクトは、治験薬サプライチェーン向けの **シンプルで透明性の高い需要予測ツール** です。

サイト別・週次のデータ（治療中患者数、ドロップアウト率、在庫、リードタイム）から

- 安全係数込みの週次必要量
- 何週間後に不足するか（weeks_until_shortage）
- 不足リスク（HIGH/LOW）

を計算し、FastAPI の `/forecast_csv` エンドポイントで CSV を受け取り、JSONで返却します。

---

## 🗂 Structure / 構成

```text
clinical-trial-supply-forecaster/
  README.md
  requirements.txt
  .gitignore
  .env.example
  data/
    site_enrollment_sample.csv
  src/
    forecast_core.py
    api.py
