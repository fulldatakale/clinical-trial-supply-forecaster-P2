# Clinical Trial Supply Forecaster  
治験サプライチェーン需要予測ツール

> P2 – AI-Powered Clinical Trial Supply Forecaster (Portfolio Project)

---

## 🌍 Overview (EN)

This project is a **transparent, rule-based forecaster** for clinical trial drug supply.

Given **site-level weekly data** (patients on treatment, dropout rate, stock on hand, lead time, etc.), it calculates:

- **Weekly demand** per site (with a safety factor)
- **Weeks until shortage** based on current stock
- A simple **shortage risk flag** (`HIGH` / `LOW`)

The goal is to show, in a clear and auditable way, how **supply risk can be monitored and explained** to clinical teams, not to build a black-box ML model.

The tool exposes a **FastAPI** endpoint `/forecast_csv` that accepts a CSV upload and returns JSON with calculated metrics.

This project is inspired by real clinical supply work (e.g., Almac-type roles) but uses **synthetic sample data**.

---

## 🌏 概要（日本語）

本プロジェクトは、治験薬サプライチェーン向けの  
**シンプルで透明性の高い需要予測ツール** です。

サイト別・週次の入力データ（治療中患者数、ドロップアウト率、在庫、リードタイムなど）から：

- サイトごとの **週次必要量（安全係数込み）**
- 現在在庫で **何週間後に不足するか（weeks_until_shortage）**
- **不足リスクフラグ**（`HIGH` / `LOW`）

を計算します。

目的は、ブラックボックスなMLモデルではなく、  
**「なぜこのサイトがリスクなのか」を説明できるロジック** を提示することです。

FastAPI の `/forecast_csv` エンドポイントで **CSVファイルをアップロード** すると、  
計算結果を JSON で返却します。

実務の治験サプライ業務（例：Almacでの経験）を抽象化した、  
**ポートフォリオ用のサンプル実装** です。

---

## 🧩 Key Features / 特長

### EN

- **Rule-based logic** – easy to explain to supply managers and auditors
- Accepts **CSV** with site-level weekly data
- Calculates:
  - Weekly demand (with safety factor)
  - Weeks until shortage
  - Shortage risk flag (`HIGH` / `LOW`)
- Simple **FastAPI service**:
  - `/forecast_csv` for CSV upload → JSON response
- Clean, extensible structure (can be upgraded to ML or optimization later)

### JP

- **ルールベースロジック** で、サプライマネージャーや監査にも説明しやすい
- サイト別・週次データを **CSV** で入力可能
- 以下の指標を算出：
  - 安全係数込みの週次必要量
  - 不足までの推定週数
  - 不足リスクフラグ（`HIGH` / `LOW`）
- シンプルな **FastAPI サービス構成**：
  - `/forecast_csv` に CSV をアップロード → JSON で結果を返却
- 構成がシンプルなため、将来的に ML や最適化モデルへ発展させやすい

---

## 🗂 Project Structure / プロジェクト構成

```text
clinical-trial-supply-forecaster/
  README.md
  requirements.txt
  .gitignore
  .env.example           # (optional: reserved for API keys, etc.)

  data/
    site_enrollment_sample.csv

  src/
    forecast_core.py     # core rule-based calculation logic
    api.py               # FastAPI app exposing /forecast_csv
