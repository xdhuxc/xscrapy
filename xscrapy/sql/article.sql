use xscrapy;

create table if not exists article (
  title varchar(300) not null comment '文章标题',
  url varchar(300) not null comment '文章的url',
  url_object_id varchar(50) primary key comment '文章的url经过MD5散列后的值',
  date datetime not null comment '文章的发布日期',
  content longtext not null comment '文章正文',
  image_url varchar(300) comment '文章配图的url',
  image_path varchar(300) comment '文章配图本地存放路径',
  tags varchar(150) comment '文章分类信息',
  admiration_num int(11) not null default 0 comment '点赞数',
  collection_num int(11) not null default 0 comment '收藏数',
  comment_num int(11) not null default 0 comment '评论数'
);



