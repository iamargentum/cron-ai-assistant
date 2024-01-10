create table tasks (
    id serial primary key,
    title text not null,
    status text not null default 'todo',
    created_at timestamp not null default now,
    updated_at timestamp not null default now,
    finished_at timestamp,
    deleted_at timestamp
);