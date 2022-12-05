create table genre
(
    name varchar(255) not null
        primary key
);

create table role
(
    name varchar(8) not null,
    id   int        not null
        primary key
);

create table status
(
    id   int          not null
        primary key,
    name varchar(255) not null
);

create table novel
(
    id          int auto_increment
        primary key,
    name        varchar(255) not null,
    image       varchar(255) null,
    description text         null,
    created     datetime     not null,
    modified    datetime     null,
    genre_name  varchar(255) not null,
    status_id   int          not null,
    view        int          null,
    constraint genre_name_fk
        foreign key (genre_name) references genre (name),
    constraint status_id_fk
        foreign key (status_id) references status (id)
);

create table chapter
(
    id       int auto_increment
        primary key,
    name     varchar(255) null,
    novel_id int          not null,
    content  text         not null,
    constraint novel_id
        foreign key (novel_id) references novel (id)
);

create table user
(
    id         int auto_increment
        primary key,
    username   varchar(255) not null,
    email      varchar(255) not null,
    password   char(60)     not null,
    last_login datetime     null,
    role_id    int          null,
    constraint email
        unique (email),
    constraint username
        unique (username),
    constraint role_id
        foreign key (role_id) references role (id)
);

create table bookmark
(
    user_id  int not null,
    novel_id int not null,
    constraint bookmark_user_id
        foreign key (user_id) references user (id)
);

