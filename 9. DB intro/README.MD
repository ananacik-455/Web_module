# European Football Databases

This repository contains two SQLite database files related to European football data:

- `european_database.sqlite`
- `football_db.sqlite`

These databases are excellent resources for practicing SQL queries, performing data analysis, and exploring real-world sports data structures.

---

## 1. `european_database.sqlite`

A simpler, cleaner dataset often used in tutorials and data science courses. It contains match results and league information.

### **Database Source**
This dataset is available on Kaggle under the name **"European Football Database"** by *groleo*.  
🔗 [Kaggle Link](https://www.kaggle.com/datasets/groleo/european-football-database)

### **Database Structure**
The file contains two primary tables:

#### **`divisions`**
| Column   | Description |
|----------|-------------|
| `division` | Unique identifier for the division (e.g., `E0`, `D1`). |
| `name`     | Full name of the division (e.g., "England Premier League"). |
| `country`  | Country where the division is played. |

#### **`matchs`**
| Column     | Description |
|------------|-------------|
| `Div`      | Division code (links to `divisions` table). |
| `Date`     | Match date. |
| `HomeTeam` | Home team name. |
| `AwayTeam` | Away team name. |
| `FTHG`     | Full-Time Home Team Goals. |
| `FTAG`     | Full-Time Away Team Goals. |
| `FTR`      | Full-Time Result (`H` = Home Win, `A` = Away Win, `D` = Draw). |

---

## 2. `football_db.sqlite`

A much larger and more comprehensive dataset containing detailed information about players, teams, matches, and countries across multiple European seasons.

### **Database Source**
This dataset is available on Kaggle under the name **"European Soccer Database"** by *hugomath*.  
🔗 [Kaggle Link](https://www.kaggle.com/datasets/hugomath/european-soccer-database)

### **Database Structure**
The file contains multiple interconnected tables. Key tables include:

#### **`Country`**
- Basic country information.

#### **`League`**
- League details linked to `Country`.

#### **`Match`**
- Detailed match data including:
  - Home/Away team IDs
  - Goals scored
  - Links to `League` and `Team`.

#### **`Team`**
- Team names and IDs.

#### **`Player`**
- Player details.

#### **`Player_Attributes`**
- Player attributes (e.g., speed, finishing, heading accuracy).

#### **`Team_Attributes`**
- Team attributes over different seasons.

---

## 📌 Usage
- Ideal for **SQL practice** and **data analysis projects**.
- Suitable for **data science learning** and **database structure exploration**.
- Great for **sports analytics** and **football statistics research**.

---

## 📜 License
Please refer to the Kaggle dataset pages for their respective licenses and usage terms.

