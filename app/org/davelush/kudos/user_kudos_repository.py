from datetime import datetime, timezone
import logging

class UserKudosRepository:

    def __init__(self, postgres_connection):
        self.conn = postgres_connection

    def create(self, user, sending_user, event_ts, channel, text, client_msg_id, event_id):
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                INSERT INTO
                    kudosbot.user_kudos
                    (
                        user_id,
                        giver_user_id,
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
                        %s,
                        %s
                    )
                """,
                (user, sending_user, event_ts, datetime.now(timezone.utc), channel, text, client_msg_id, event_id))
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
        except Exception as ex:
            logging.exception(ex)
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

    def get_kudos_amounts_for_month(self, year, month):
        resp_list = []
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                SELECT user_id,
                       COUNT(*)
                FROM kudosbot.user_kudos
                WHERE date_part('year', creation_ts) = %s
                AND date_part('month', creation_ts) = %s
                GROUP BY user_id
                ORDER BY count(*) DESC
                """,
                (year, month)
            )
            for row in cur:
                resp_list.append({"user_id": row[0], "kudos_count": row[1]})
            return resp_list
        finally:
            cur.close()

    def get_kudos_giver_amounts_for_month(self, year, month):
        resp_list = []
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                SELECT giver_user_id,
                       COUNT(*)
                FROM kudosbot.user_kudos
                WHERE date_part('year', creation_ts) = %s
                AND date_part('month', creation_ts) = %s
                GROUP BY giver_user_id
                ORDER BY count(*) DESC
                """,
                (year, month)
            )
            for row in cur:
                resp_list.append({"user_id": row[0], "kudos_count": row[1]})
            return resp_list
        finally:
            cur.close()

    def get_kudos_messages_for_month(self, year, month):
        resp_list = []
        cur = self.conn.cursor()
        try:
            cur.execute(
                """
                SELECT user_id,
                       giver_user_id,
                       text
                FROM kudosbot.user_kudos
                WHERE date_part('year', creation_ts) = %s
                AND date_part('month', creation_ts) = %s
                """,
                (year, month)
            )
            for row in cur:
                resp_list.append({"user_id": row[0], "giver_user_id": row[1], "text": row[2]})
            return resp_list
        finally:
            cur.close()
