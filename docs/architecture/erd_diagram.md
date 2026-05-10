erDiagram
    dim_members ||--o{ fact_interactions : "initiates (actor_id)"
    dim_members ||--o{ fact_interactions : "receives (target_id)"
    dim_members ||--o{ fact_transactions : "purchases"

    dim_members {
        uuid member_id PK
        timestamp signup_date
        string persona_segment
        boolean is_premium
        string acquisition_channel
    }

    fact_interactions {
        int interaction_id PK
        uuid actor_id FK
        uuid target_id FK
        string interaction_type
        float sentiment_score
    }

    fact_transactions {
        int transaction_id PK
        uuid member_id FK
        string product_type
        decimal amount_usd
        boolean is_refunded
    }
