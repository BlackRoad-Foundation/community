#!/usr/bin/env python3
"""BlackRoad Community — Member registry and activity feed."""
import sqlite3, json, datetime, os

DB = os.path.expanduser("~/.blackroad/community.db")

def init():
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    c = sqlite3.connect(DB)
    c.executescript("""
        CREATE TABLE IF NOT EXISTS members (
            id TEXT PRIMARY KEY, name TEXT, role TEXT,
            joined_at TEXT, contributions INTEGER DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id TEXT, action TEXT, detail TEXT, ts TEXT
        );
    """)
    c.commit()
    return c

def add_member(id, name, role="member"):
    c = init()
    c.execute("INSERT OR IGNORE INTO members VALUES (?,?,?,?,0)",
              (id, name, role, datetime.datetime.utcnow().isoformat()))
    c.commit()
    print(f"✓ Added {name} as {role}")

def log_activity(member_id, action, detail=""):
    c = init()
    c.execute("INSERT INTO activity(member_id,action,detail,ts) VALUES(?,?,?,?)",
              (member_id, action, detail, datetime.datetime.utcnow().isoformat()))
    c.execute("UPDATE members SET contributions=contributions+1 WHERE id=?", (member_id,))
    c.commit()

def leaderboard():
    c = init()
    rows = c.execute("SELECT name,role,contributions FROM members ORDER BY contributions DESC LIMIT 10").fetchall()
    print("\\n🏆 Community Leaderboard\\n")
    for i,(name,role,count) in enumerate(rows,1):
        medal = ["🥇","🥈","🥉"][i-1] if i<=3 else f" {i}."
        print(f"  {medal} {name:<20} [{role}] {count} contributions")

if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv)>1 else "board"
    if cmd == "add": add_member(sys.argv[2],sys.argv[3],sys.argv[4] if len(sys.argv)>4 else "member")
    elif cmd == "log": log_activity(sys.argv[2],sys.argv[3],sys.argv[4] if len(sys.argv)>4 else "")
    else: leaderboard()

