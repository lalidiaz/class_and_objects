from user import User
from post import Post

app_user_one = User("lala@lala.com", "Lala Martinez", "pwds", "Front-end Developer")
app_user_one.change_job_title("DevOps engineer")
app_user_one.get_user_info()

app_user_two = User("mimi@lala.com", "Mimi Gonzalez", "pwds2", "AI Engineer")
app_user_two.get_user_info()

new_post = Post("On a secret mission today", app_user_two.name)
new_post.get_post_info()