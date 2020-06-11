alter table kudosbot.user_kudos alter column user_id type varchar(15) using user_id::varchar(15);
alter table kudosbot.user_kudos alter column giver_user_id type varchar(15) using giver_user_id::varchar(15);
