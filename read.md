CREATE TABLE `users_follow` (
    `id` BIGINT AUTO_INCREMENT PRIMARY KEY,
    `follower_id` BIGINT NOT NULL,
    `following_id` BIGINT NOT NULL,
    `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`follower_id`) REFERENCES `users_user` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`following_id`) REFERENCES `users_user` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `unique_follow` (`follower_id`, `following_id`)
);
  (1146, "Table 'connectionhub.users_follow' doesn't exist")




drop table users_blocks;               
drop table users_follow;               
drop table users_followrequest;