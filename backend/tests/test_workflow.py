import asyncio
import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.agents.graph import app_graph
from dotenv import load_dotenv

load_dotenv()


MOCK_DIFF = """
diff --git a/app/users.py b/app/users.py
index 83c1a2..b2a1c3 100644
--- a/app/users.py
+++ b/app/users.py
@@ -10,6 +10,15 @@ def get_user_stats(user_ids):
+    stats = []
+    # PERFORMANCE: Nested loop causing O(n^2)
+    for uid in user_ids:
+        for other_uid in user_ids:
+            if uid == other_uid:
+                continue
+            
+            # SECURITY: SQL Injection vulnerability
+            query = f"SELECT * FROM transactions WHERE user_id = {uid}"
+            db.execute(query)
+            
+            # LOGIC: 'result' is not defined before use
+            stats.append(result)
+            
+    return stats
"""

async def run_test():
    print("Starting Automated PR Review Agent Test...")
    print("-" * 50)
    
    initial_state = {"diff": MOCK_DIFF, "reviews": []}
    
    try:

        result = await app_graph.ainvoke(initial_state)
        
        print("\nReview Generation Complete!")
        print("-" * 50)
        

        final_review = result['reviews'][-1]
        print(final_review)
        
    except Exception as e:
        print(f"Error running test: {e}")
        print("Ensure you have set GOOGLE_API_KEY in backend/.env")

if __name__ == "__main__":
    asyncio.run(run_test())
