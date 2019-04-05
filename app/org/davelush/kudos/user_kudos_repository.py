from datetime import datetime, timezone


class UserKudosRepository:

    def __init__(self, postgres_connection):
        super(UserKudosRepository, self).__init__()
        self.conn = postgres_connection

    def create(self, user, event_ts, channel, text, client_msg_id):
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
                        client_msg_id
                    )
                    VALUES
                    (
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s
                    )
                """,
                (user, event_ts, datetime.now(timezone.utc), channel, text, client_msg_id))
            self.conn.commit()
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
