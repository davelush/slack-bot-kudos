alter table kudosbot.user_kudos alter column user_id type varchar(12) using user_id::varchar(12);
alter table kudosbot.user_kudos alter column giver_user_id type varchar(12) using giver_user_id::varchar(12);
