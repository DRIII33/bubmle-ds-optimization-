# Data Schema Specification: The "Kindness Graph" Model


**Data Scientist:** Daniel Rodriguez III

This document outlines the three-tier relational schema designed for high-performance behavioral analysis within the Bumble Core Data Science simulation.

## 1. dim_members (Member Dimension)
*   **Purpose:** Stores persistent user attributes and acquisition metadata.
*   **Row Constraint:** 50,000 unique records.

| Column Name | Data Type | Constraint | Description |
| :--- | :--- | :--- | :--- |
| `member_id` | UUID | Primary Key | Unique identifier for each member. |
| `signup_date` | TIMESTAMP | NOT NULL | Date and time of account creation. |
| `persona_segment` | STRING | CHECK (IN...) | {The Connector, The Selective, The Newbie, The Ghost}. |
| `is_premium` | BOOLEAN | DEFAULT FALSE | Current subscription status. |
| `acquisition_channel` | STRING | NOT NULL | {Paid Social, Organic, Referral}. |

## 2. fact_interactions (Interaction Fact)
*   **Purpose:** Captures high-frequency behavioral events between users.
*   **Row Constraint:** 50,000 records.

| Column Name | Data Type | Constraint | Description |
| :--- | :--- | :--- | :--- |
| `interaction_id` | INTEGER | Primary Key | Auto-incrementing interaction ID. |
| `actor_id` | UUID | Foreign Key | The member initiating the action. |
| `target_id` | UUID | Foreign Key | The member receiving the action. |
| `interaction_type` | STRING | NOT NULL | {Swipe_Right, Swipe_Left, Message, Block}. |
| `sentiment_score` | FLOAT | -1.0 to 1.0 | Normalized kindness/sentiment metric. |

## 3. fact_transactions (Financial Fact)
*   **Purpose:** Tracks monetization events and revenue attribution.
*   **Row Constraint:** 10,000 records.

| Column Name | Data Type | Constraint | Description |
| :--- | :--- | :--- | :--- |
| `transaction_id` | INTEGER | Primary Key | Unique transaction identifier. |
| `member_id` | UUID | Foreign Key | The member associated with the purchase. |
| `product_type` | STRING | NOT NULL | {Subscription, Spotlight, SuperSwipe}. |
| `amount_usd` | DECIMAL(10,2) | > 0 | Revenue generated from the transaction. |
| `is_refunded` | BOOLEAN | DEFAULT FALSE | Status of the financial transaction. |
