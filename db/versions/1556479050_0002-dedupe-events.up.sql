alter table kudosbot.user_kudos
	add event_id varchar not null;

create unique index user_kudos_event_id_uindex
	on kudosbot.user_kudos (event_id);
