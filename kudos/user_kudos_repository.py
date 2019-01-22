from datetime import datetime, timezone


class UserKudosRepository:

    def __init__(self, postgres_connection):
        super(UserKudosRepository, self).__init__()
        self.conn = postgres_connection

    def create(self, user):
        try:
            cur = self.conn.cursor()
            cur.execute(
                """
                INSERT INTO
                    slack_bot.user_kudos
                    (
                        user_id,
                        kudos_timestamp
                    )
                    VALUES
                    (
                        %s,
                        %s
                    )
                """,
                (user, datetime.now(timezone.utc)))
            self.conn.commit()
        finally:
            cur.close()
