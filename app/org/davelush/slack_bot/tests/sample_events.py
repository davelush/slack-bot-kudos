verification_token = "verification-token-1234"

app_mention_event = """ {
                            "token": "verification-token-1234",
                            "team_id": "team-id-1234",
                            "api_app_id": "api-app-id-1234",
                            "event": {
                                "client_msg_id": "80bdd163-beef-4a48-a257-bfb4c6950001",
                                "type": "app_mention",
                                "text": "Just making sure you're still working and ready to receive a :star: <@UDUR2T8UR>?",
                                "user": "U4DAVJG0Y",
                                "ts": "1556896019.000400",
                                "channel": "CDWEW9WBZ",
                                "event_ts": "1556896019.000400"
                            },
                            "type":"event_callback",
                            "event_id": "EvJD5HC06Q",
                            "event_time": 1556896019,
                            "authed_users": ["UDUR2T8UR"]
                        }"""

message_event = """     {
                            "token": "verification-token-1234",
                            "team_id": "team-id-1234",
                            "api_app_id": "api-app-id-1234",
                            "event": {
                                "client_msg_id": "80bdd163-beef-4a48-a257-bfb4c6950002",
                                "type": "message",
                                "text": "This is a message with a :star: for <@UDUR2T8UR>?",
                                "user": "U4DAVJG0Y",
                                "ts": "1556896019.000400",
                                "channel": "CDWEW9WBZ",
                                "event_ts": "1556896019.000400",
                                "channel_type": "channel"
                            },
                            "type": "event_callback",
                            "event_id": "EvJ27T6327",
                            "event_time": 1556896019,
                            "authed_users": ["UDUR2T8UR"]
                        }"""