from datetime import datetime, timezone


class UserKudosRepository:

    def __init__(self, postgres_connection):
        super(UserKudosRepository, self).__init__()
        self.conn = postgres_connection

    def create(self, user, event_ts, channel, text, client_msg_id):
        try:
            cur = self.conn.cursor()
            cur.execute(
                """
                INSERT INTO
                    slack_bot.user_kudos
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
