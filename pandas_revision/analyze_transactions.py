import pandas as pd
from datetime import datetime
from typing import List, Dict, Tuple


def analyze_transactions(transactions: List[Dict]) -> Dict:
    """
    Analyze customer transaction data

    Args:
        transactions: List of transaction dictionaries

    Returns:
        Dictionary with analysis results
    """
    if not transactions:
        return {"error": "No transactions provided"}

    try:
        df = pd.DataFrame(transactions)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['date'] = df['timestamp'].dt.date

        # 1. Top 3 spending customers
        spends = df.groupby('user_id')['price'].sum()
        top_3 = spends.sort_values(ascending=False).head(3).reset_index()
        top_3_dict = dict(zip(top_3['user_id'], top_3['price']))
        print(top_3_dict)

        # 2. Most popular category
        cats = df['category']
        popular_category = cats.value_counts().idxmax()
        print(popular_category)

        # 3. Average transaction value per day
        freq = {}
        days = {}
        for rec in transactions:
            day = rec['timestamp'].split(' ')[0]

            if not day in days:
                days[day] = rec['price']
                freq[day] = 1
            else:
                freq[day] += 1
                days[day] += rec['price']

        for day, val in days.items():
            days[day] = val / freq[day]

        print(days)

        # 4. Customers with consecutive day purchases
        df_sorted = df.sort_values(['user_id', 'timestamp'])
        df_sorted['days_since_last'] = df_sorted.groupby('user_id')['timestamp'].diff().dt.days
        consecutive_customers = df_sorted[df_sorted['days_since_last'] == 1]['user_id'].unique().tolist()
        print(consecutive_customers)

        # Convert string dates to datetime.date objects for return

        # IMPORTANT: Add return statement
        return {
            'top_customers': top_3_dict,
            'popular_category': popular_category,
            'average_transaction_daily': days
        }

    except Exception as e:
        return {"error": f"Processing error: {str(e)}"}


transactions = [
    {"user_id": 1, "product_id": "A", "price": 29.99, "timestamp": "2024-01-15 10:30:00", "category": "electronics"},
    {"user_id": 2, "product_id": "B", "price": 15.50, "timestamp": "2024-01-15 11:45:00", "category": "books"},
    {"user_id": 1, "product_id": "C", "price": 45.00, "timestamp": "2024-01-16 09:20:00", "category": "electronics"},
]

if __name__ == "__main__":
    result = analyze_transactions(transactions)
    print(result)
