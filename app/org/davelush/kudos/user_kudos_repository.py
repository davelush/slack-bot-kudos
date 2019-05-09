import logging
from datetime import datetime, timezone


class UserKudosRepository:

    def __init__(self, postgres_connection):
        self.conn = postgres_connection

    def create(self, user, event_ts, channel, text, client_msg_id, event_id):
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                INSERT INTO
                    kudosbot.user_kudos
                    (
                        user_id,
                        event_ts,
                        creation_ts,
                        channel,
                        text,
                        client_msg_id,
                        event_id
                    )
                    VALUES
                    (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                """,
                (user, event_ts, datetime.now(timezone.utc), channel, text, client_msg_id, event_id))
            self.conn.commit()
        finally:
            cur.close()

    def event_exists(self, event_id):
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                SELECT COUNT(*)
                FROM kudosbot.user_kudos
                WHERE event_id = %s
                """,
                (event_id,))
            if cur.fetchone()[0] == 0:
                return False
            else:
                return True
        finally:
            cur.close()

    def get_count(self, user_id):
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                SELECT COUNT(*)
                FROM kudosbot.user_kudos
                WHERE user_id = %s
                """,
                (user_id,))
            return cur.fetchone()[0]
        finally:
            cur.close()

    def get_count_this_month(self, user_id):
        cur = self.conn.cursor()
        try:
            print("")
        finally:
            cur.close()

    def get_kudos_amounts(self):
        resp_list = []
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                SELECT user_id,
                       count(*)
                FROM kudosbot.user_kudos
                GROUP BY user_id 
                ORDER BY count(*) DESC
                """,
            )
            for row in cur:
                resp_list.append({"user_id": row[0], "kudos_count": row[1]})
            return resp_list
        finally:
            cur.close()
